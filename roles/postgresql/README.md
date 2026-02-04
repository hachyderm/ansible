# Ansible Role: PostgreSQL

An Ansible role for installing and configuring
[PostgreSQL](https://www.postgresql.org/), an open source object-relational
database system.

What the role does:

* Installation of the official binaries
* Prepare for point-in-time recovery (optional)
* Logging (optional)
* Replication (optional)
* Create additional users (optional)
* Major upgrades

What the role does NOT:

* Non-Debian distributions
* Connection pooling
* Automated failovers
* Switchovers
* Minor upgrades
* Backup and restores policies

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)
* `community.postgresql` collection
* `pgdg_repository` role

## Role Variables

See [VARIABLES](VARIABLES.md).

## Example

### Standalone

```yaml
- hosts: all
  become: true
  roles:
    - hachyderm.general.postgresql
  vars:
    postgresql_superuser_password: CHANGEME
```

### Replication

On primary and replicas:

```yaml
- hosts: all
  become: true
  roles:
    - hachyderm.general.postgresql
  vars:
    postgresql_superuser_password: CHANGEME
    postgresql_manage_replication: true
    postgresql_listen_addresses:
      - '*'
    postgresql_replication_username: repl
    postgresql_replication_password: CHANGEME
    postgresql_replication_network: 192.168.0.0/24
```

On replicas:

```yaml
  vars:
    [...]
    postgresql_instance_role: replica
    postgresql_primary_host: 192.168.0.1
```


### Major upgrades

> [!WARNING]
>
> **No rollback.**
>
> You should test the upgrade on a separate environment to ensure everything is
> fine before executing the playbook on production.

The role can upgrade a PostgreSQL cluster by running
[pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html) on the
primary then reconfigure the replication on the upgraded version.

First deploy a PostgreSQL cluster (standalone or replicated).

```yaml
  vars:
    postgresql_version: 15
```

Then copy the version to `postgresql_upgrade_from_version` and configure the
desired `postgresql_version`:

```yaml
  vars:
    postgresql_upgrade_from_version: 15
    postgresql_version: 18
```

Run the playbook.

At this point, you can remove the previous version from the variables:

```yaml
  vars:
    postgresql_version: 18
```

## Local Testing

The preferred way of locally testing the role is to use
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
