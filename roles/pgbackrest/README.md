# Ansible Role: pgBackRest

An Ansible role for installing and configuring
[pgBackRest](https://pgbackrest.org/), a reliable backup and restore solution
for PostgreSQL.

Supported features:

* Standalone deployment
* Distributed deployments (with TLS server)
* PostgreSQL major upgrades

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)
* `pgdg_repository` role
* `postgresql` role (optional but recommended)

## Role Variables

See [VARIABLES](VARIABLES.md).

## Example

### Standalone

PostgreSQL and pgBackRest on the same host.

Variables:

```yaml
postgresql_version: 18
postgresql_superuser_password: CHANGEME
postgresql_manage_pgpass: true
postgresql_archive_command: 'pgbackrest --stanza=main --log-level-console=warn archive-push %p'
postgresql_restore_command: 'pgbackrest --stanza=main --log-level-console=warn archive-get %f "%p"'

pgbackrest_repositories:
  - path: /var/lib/pgbackrest
    cipher-pass: CHANGEME
    cipher-type: aes-256-cbc
    retention-full-type: time
    retention-full: 14
    retention-diff: 3
    bundle: y
pgbackrest_stanzas:
  main:
   - pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
     pg-host-port: 5432
pgbackrest_schedules:
  full:
    OnCalendar: "Mon *-*-* 4:30:00"
    RandomizedDelaySec: 1800
    FixedRandomDelay: false
    Persistent: false
  diff:
    OnCalendar: "Tue..Sun *-*-* 4:30:00"
    RandomizedDelaySec: 1800
    FixedRandomDelay: false
    Persistent: false
```

Playbook:

```yaml
- name: Install minimal pgBackRest and PostgreSQL
  hosts: all
  become: true
  roles:
    - hachyderm.general.pgbackrest
    - hachyderm.general.postgresql
  vars:
    pgbackrest_full_install: false

- name: Finalize pgBackRest configuration
  hosts: all
  become: true
  roles:
    - hachyderm.general.pgbackrest
```

### Two nodes

PostgreSQL primary replicating to a replica with pgBackRest repository deployed
on the replica.

Configure PostgreSQL replication (see [PostgreSQL
role](../postgresql/README.md]).

Common PostgreSQL variables:

```yaml
postgresql_version: 18
postgresql_superuser_password: CHANGEME
postgresql_listen_addresses:
  - '*'
postgresql_manage_replication: true
postgresql_replication_username: repl
postgresql_replication_password: CHANGEME
postgresql_replication_network: 192.168.0.0/24
postgresql_manage_pgpass: true
postgresql_archive_command: 'pgbackrest --stanza=main --log-level-console=warn archive-push %p'
postgresql_restore_command: 'pgbackrest --stanza=main --log-level-console=warn archive-get %f "%p"'
```

PostgreSQL variables for the replica:

```yaml
postgresql_instance_role: replica
postgresql_primary_host: 192.168.0.1
```

Generate TLS certificates:

> [!WARNING]
>
> For testing purpose only

```
openssl req -new -x509 -days 3650 -nodes -out ca.crt -keyout ca.key -subj "/CN=ca"
openssl req -new -nodes -out primary.csr -keyout primary.key -subj "/CN=primary"
openssl x509 -req -in primary.csr -days 3650 -CA ca.crt -CAkey ca.key -CAcreateserial -out primary.crt
openssl req -new -nodes -out replica.csr -keyout replica.key -subj "/CN=replica"
openssl x509 -req -in replica.csr -days 3650 -CA ca.crt -CAkey ca.key -CAcreateserial -out replica.crt
```

Common variables:

```yaml
pgbackrest_agent_address: 0.0.0.0
pgbackrest_agent_port: 8433
pgbackrest_agent_allowed_users:
  replica: main
pgbackrest_agent_repositories:
  - host: replica
    port: 8432
    user: pgbackrest
    config: /etc/pgbackrest-server/pgbackrest.conf
pgbackrest_agent_stanzas:
  main:
    - pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
```

Variables for the primary:

```yaml
pgbackrest_role: agent
pgbackrest_agent_tls_ca: |
  [content of ca.crt]
pgbackrest_agent_tls_cert: |
  [content of primary.crt]
pgbackrest_agent_tls_key: |
  [content of primary.key]
```

Variables for the replica:

```yaml
pgbackrest_role: both
pgbackrest_server_tls_ca: &pgbackrest_ca |
  [content of ca.crt]
pgbackrest_server_tls_cert: &pgbackrest_cert |
  [content of replica.crt]
pgbackrest_server_tls_key: &pgbackrest_key |
  [content of replica.key]
pgbackrest_agent_tls_ca: *pgbackrest_ca
pgbackrest_agent_tls_cert: *pgbackrest_cert
pgbackrest_agent_tls_key: *pgbackrest_key
pgbackrest_server_address: 0.0.0.0
pgbackrest_server_port: 8432
pgbackrest_server_allowed_users:
  primary: main
  replica: main
pgbackrest_server_repositories:
  - path: /var/lib/pgbackrest
    cipher-pass: CHANGEME
    cipher-type: aes-256-cbc
    retention-full-type: time
    retention-full: 14
    retention-diff: 3
    bundle: y
pgbackrest_server_stanzas:
  main:
    - pg-host: primary
      pg-host-port: 8433
      pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
    - pg-host: replica
      pg-host-port: 8433
      pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
pgbackrest_schedules:
  full:
    OnCalendar: "Mon *-*-* 4:30:00"
    RandomizedDelaySec: 1800
    FixedRandomDelay: false
    Persistent: false
  diff:
    OnCalendar: "Tue..Sun *-*-* 4:30:00"
    RandomizedDelaySec: 1800
    FixedRandomDelay: false
    Persistent: false
```

Playbook:

```yaml
- name: Prepare servers
  hosts: all
  become: true
  tasks:
    - name: Add entries to /etc/hosts
      ansible.builtin.blockinfile:
        path: /etc/hosts
        block: |
          192.168.0.1 primary
          192.168.0.2 replica

- name: Install minimal pgBackRest and PostgreSQL
  hosts: all
  become: true
  roles:
    - hachyderm.general.pgbackrest
    - hachyderm.general.postgresql
  vars:
    pgbackrest_full_install: false

- name: Finalize pgBackRest configuration
  hosts: all
  become: true
  roles:
    - hachyderm.general.pgbackrest
```

Create a backup and verify on the replica:

```
systemctl start pgbackrest-full.service
su - pgbackrest -c 'pgbackrest --config /etc/pgbackrest-server/pgbackrest.conf info'
```

Example:

```
stanza: main
    status: ok
    cipher: aes-256-cbc

    db (current)
        wal archive min/max (18): 000000010000000000000001/000000010000000000000007

        full backup: 20251227-083056F
            timestamp start/stop: 2025-12-27 08:30:56+01 / 2025-12-27 08:30:58+01
            wal start/stop: 000000010000000000000007 / 000000010000000000000007
            database size: 22.6MB, database backup size: 22.6MB
            repo1: backup set size: 2.9MB, backup size: 2.9MB
```

## Local Testing

The prefered way of locally testing the role is to use
[Podman](https://podman.io/) and
[molecule](https://docs.ansible.com/projects/molecule/).

List scenarios:

```
molecule list
```

Install dependencies:

```
molecule dependency [--scenario-name=default]
```

Run a single scenario:

```
molecule test [--scenario-name=default]
```

Run all scenarios:

```
molecule test --all
```
