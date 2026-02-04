# Variables

See [defaults/main.yml](defaults/main.yml) for the defaults.

### pgbackrest_role

Role of the pgBackRest instance on the server (default `standalone`).

List of supported roles:

* `standalone`: run everything locally
* `server`: start a TLS server and orchestrate backup policies
* `agent`: start a TLS server to receive operations from the server
* `both`: configure a server and an agent on the same host

### pgbackrest_settings

Dictionary of custom settings (default `{}`).

Example:

```yaml
pgbackrest_settings:
  compress-type: zst
  compress-level: 3
  process-max: 2
  start-fast: y
  delta: y
  archive-async: y
  log-level-console: info
  log-level-file: info
```

### pgbackrest_schedules

Dictionary of backup schedules (default `{}`).

Example:

```yaml
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

### pgbackrest_service_after

List of systemd units to wait before starting pgBackRest.

Example:

```yaml
pgbackrest_service_after:
  - tailscaled.service
```

### pgbackrest_notification_command

Command to execute when a pgBackRest backup command is performed.

The command takes two positional arguments:

* `pgBackRest`: the string `pgBackRest` to tell who's runing the command
* `message`: a message to tell what is happening (replaced by
  `pgbackrest_notification_message_start` and
  `pgbackrest_notification_message_stop`)

### pgbackrest_notification_message_start

Message sent to the notification command when a backup command is starting
(default `starting`).

### pgbackrest_notification_message_stop

Message sent to the notification command when a backup command is stopping
(default `done`).

### pgbackrest_full_install

Enable tasks that are part of a circular dependency with the `postgresql` role
(default `true`).

Checking configuration forces a WAL to be archived so a working PostgreSQL
instance is required. But, if PostgreSQL is deployed with the pgbackrest binary
for the restore command, the service may not start because it requires
pgBackRest to be fully working. Same for stanza creation. The
`pgbackrest_full_install` variable can be disabled to ignore all the tasks that
are part of the circular dependency issue.

### pgbackrest_additional_groups

List of groups to append to the operating system user (default `[]`).

### pgbackrest_user

Operating system user for a standalone deployment (default `postgres`).

### pgbackrest_group

Operating system group for a standalone deployment (default `postgres`).

### pgbackrest_repositories

List of repositories in a standalone deployment (default `[]`).

Example:

```yaml
pgbackrest_repositories:
  - path: /var/lib/pgbackrest
```

The repository index will be automatically generated.

See [Repository
Options](https://pgbackrest.org/configuration.html#section-repository).

### pgbackrest_stanzas

Dictionary of stanzas to create in a standalone deployment (default `{}`).

Example:

```yaml
pgbackrest_stanzas:
  main:
   - pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
     pg-host-port: 5432
   - pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
     pg-host-port: 5433
```

The server index will be automatically generated.

See [Stanza Options](https://pgbackrest.org/configuration.html#section-stanza).

### pgbackrest_agent_user

Operating system user for an agent (default `postgres`).

### pgbackrest_agent_group

Operating system group for an agent (default `postgres`).

### pgbackrest_agent_address

Address to listen for an agent (default `localhost`).

See [TLS Server Address
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-address).

### pgbackrest_agent_port

Port to listen for an agent (default `8432`).

See [TLS Server Port
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-port).

### pgbackrest_agent_tls_ca

Content of a Certificate Authority (CA) to verify the authenticity of TLS
certificates for an agent (default `null`).

Use the same CA for agent and server.

If defined, the content will be written in `pgbackrest_agent_tls_ca_file`.

See [TLS Server Certificate Authorities
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file).

How to generate a self-signed CA:

> [!WARNING]
>
> For testing purpose only

```
openssl req -new -x509 -days 3650 -nodes -out ca.crt -keyout ca.key -subj "/CN=ca"
```

### pgbackrest_agent_tls_ca_file

Path to the TLS server certificate authorities for an agent (default
`/etc/pgbackrest/ca.crt`).

For certificates signed by a trusted CA (like Let's Encrypt), use
`/etc/ssl/certs/ca-certificates.crt`.

See [TLS Server Certificate Authorities
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file).

### pgbackrest_agent_tls_cert

Content of the TLS server certificate for an agent (default `null`).

If defined, the content will be written in `pgbackrest_agent_tls_cert_file`.

See [TLS Server Certificate
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).

How to generate a self-signed cert (and key):

> [!WARNING]
>
> For testing purpose only

```
openssl req -new -nodes -out primary.csr -keyout primary.key -subj "/CN=primary"
openssl x509 -req -in primary.csr -days 3650 -CA ca.crt -CAkey ca.key -CAcreateserial -out primary.crt
```

Where `primary` is the resolvable hostname of the agent.

### pgbackrest_agent_tls_cert_file

Path to the TLS server certificate for an agent (default
`/etc/pgbackrest/server.crt`).

See [TLS Server Certificate
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).

### pgbackrest_agent_tls_key

Content of the TLS server key for an agent (default `null`).

If defined, the content will be written in `pgbackrest_agent_tls_key_file`.

See [TLS Server Key
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file).

### pgbackrest_agent_tls_key_file

Path to the TLS server key file for an agent (default
`/etc/pgbackrest/server.key`).

See [TLS Server Key
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file).

### pgbackrest_agent_stanzas

Dictionary of stanzas supported by an agent (default `{}`).

Example:

```yaml
pgbackrest_agent_stanzas:
  main:
   - pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"
```

The server index will be automatically generated.

See [Stanza Options](https://pgbackrest.org/configuration.html#section-stanza).

### pgbackrest_agent_allowed_users

Dictionary of allowed users (server) on the agent (default `{}`).

The key is the hostname. The value is the stanza name.

Names must be included in the **TLS certificate** and **resolvable** by DNS.

Example:

```yaml
pgbackrest_agent_allowed_users:
  server: stanza
```

See [TLS Server Authorized Clients
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-auth).

### pgbackrest_agent_repositories

List of agent to repositories (server) communication.

All repositories must be declared. If pgBackRest is supposed to send backups to
multiple object storage or filesystems, create a list of the size of the number
of server repositories (`pgbackrest_server_repositories`). Even if the content
is repeated.

Default:

```yaml
pgbackrest_agent_repositories:
  - host: localhost
    port: 8432
    user: pgbackrest
    config: /etc/pgbackrest-server/pgbackrest.conf
```

Example:

```yaml
pgbackrest_agent_repositories:
  # repo1 to filesystem
  - host: repository-hostname.fqdn
    port: 8432
    user: pgbackrest
    config: /etc/pgbackrest-server/pgbackrest.conf
  # repo2 to object storage
  - host: repository-hostname.fqdn
    port: 8432
    user: pgbackrest
    config: /etc/pgbackrest-server/pgbackrest.conf
```

The repository index will be automatically genetated.

See [Repository
Options](https://pgbackrest.org/configuration.html#section-repository).

### pgbackrest_server_user

Operating system user for a server (default `pgbackrest`).

### pgbackrest_server_user_home

Home of the operating system user for a server (default `/var/lib/pgbackrest`).

### pgbackrest_server_group

Operating system group for a server (default `pgbackrest`).

### pgbackrest_server_address

Address to listen for a server (default `localhost`).

See [TLS Server Address
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-address).

### pgbackrest_server_port

Port to listen for a server (default `8432`).

See [TLS Server Port
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-port).

### pgbackrest_server_tls_ca

Content of a Certificate Authority (CA) to verify the authenticity of TLS
certificates for a server (default `null`).

Use the same CA for agent and server.

If defined, the content will be written in `pgbackrest_server_tls_ca_file`.

See [TLS Server Certificate Authorities
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file).

### pgbackrest_server_tls_ca_file

Path to the TLS server certificate authorities for a server (default
`/etc/pgbackrest-server/ca.crt`).

See [TLS Server Certificate Authorities
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-ca-file).


### pgbackrest_server_tls_cert

Content of the TLS server certificate for a server (default `null`).

When `pgbackrest_role` is `both`, use the same TLS cert for agent and server.

If defined, the content will be written in `pgbackrest_server_tls_cert_file`.

See [TLS Server Certificate
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).

How to generate a self-signed cert (and key):

> [!WARNING]
>
> For testing purpose only

```
openssl req -new -nodes -out server.csr -keyout server.key -subj "/CN=server"
openssl x509 -req -in server.csr -days 3650 -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt
```

Where `server` is the resolvable hostname of the backup server.

### pgbackrest_server_tls_cert_file

Path to the TLS server certificate for a server (default
`/etc/pgbackrest-server/server.crt`).

See [TLS Server Certificate
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-cert-file).

### pgbackrest_server_tls_key

Content of the TLS server key for a server (default `null`).

When `pgbackrest_role` is `both`, use the same TLS key for agent and server.

If defined, the content will be written in `pgbackrest_server_tls_key_file`.

See [TLS Server Key
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file).

### pgbackrest_server_tls_key_file

Path to the TLS server key file for a server (default
`/etc/pgbackrest-server/server.key`).

See [TLS Server Key
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-key-file).

### pgbackrest_server_repositories

List of repositories (default `[]`).

Example:

```yaml
pgbackrest_server_repositories:
  - path: /var/lib/pgbackrest
```

See [Repository
Options](https://pgbackrest.org/configuration.html#section-repository).

### pgbackrest_server_stanzas

Dictionary of stanzas to create on a server (default `{}`).

Example:

```yaml
pgbackrest_server_stanzas:
  main:
    - pg-host: primary    # agent host
      pg-host-port: 8433  # agent port
      pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"  # agent path
    - pg-host: replica    # agent host
      pg-host-port: 8433  # agent port
      pg-path: "/var/lib/postgresql/{{ postgresql_version }}/main"  # agent path
```

The server index will be automatically generated.

See [Stanza Options](https://pgbackrest.org/configuration.html#section-stanza).

### pgbackrest_server_allowed_users

Dictionary of allowed users (agents) on the server (default `{}`).

The key is the hostname. The value is the stanza name.

Names must be included in the **TLS certificate** and **resolvable** by DNS.

Example:

```yaml
pgbackrest_server_allowed_users:
  primary: stanza
  replica: stanza
```

See [TLS Server Authorized Clients
Option](https://pgbackrest.org/configuration.html#section-server/option-tls-server-auth).

### pgbackrest_server_lock_path

Path where lock files are stored on the server (default `/tmp/pgbackrest-server`).

See [Lock Path
Option](https://pgbackrest.org/configuration.html#section-general/option-lock-path).
