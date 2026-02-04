# Variables

See [defaults/main.yml](defaults/main.yml) for the defaults.

### pgbouncer_databases

Dictionary of databases connections strings (default `{}`). They key is the
database name. The value is the connection string.

Example:

```yaml
pgbouncer_databases:
  mastodon_production: host=127.0.0.1 port=5432 dbname=mastodon_production
```

See [Section
[databases]](https://www.pgbouncer.org/config.html#section-databases) for
details.

### pgbouncer_users

Dictionary of users (default `{}`). The key is the user name. The value is the
user settings.

Example:

```yaml
pgbouncer_users
  mastodon: query_timeout=30
```

### pgbouncer_listen_addr

List of addresses to listen (default `["localhost"]`).

The list will be transformed to a coma separated list in the configuration
file.

Example:

```yaml
pgbouncer_listen_addr:
  - 127.0.0.1
  - "{{ ansible_tailscale0.ipv4.address }}"
```

See [listen_addr](https://www.pgbouncer.org/config.html#listen_addr) for
details.

### pgbouncer_listen_port

Which port to listen on (default `6432`).

See [listen_port](https://www.pgbouncer.org/config.html#listen_port) for details.

### pgbouncer_logfile

Path to the log file (default `/var/log/postgresql/pgbouncer.log`).

See [logfile](https://www.pgbouncer.org/config.html#logfile) for details.

### pgbouncer_pidfile

Path to PID file (default `/var/run/postgresql/pgbouncer.pid`).

See [pidfile](https://www.pgbouncer.org/config.html#pidfile) for details.

### pgbouncer_auth_type

How to authenticate users (default `scram-sha-256`).

See [auth_type](https://www.pgbouncer.org/config.html#auth_type) for details.

### pgbouncer_auth_file

Path to the authentication file (default `/etc/pgbouncer/userlist.txt`).

See [auth_file](https://www.pgbouncer.org/config.html#auth_file) for details.

### pgbouncer_admin_users

List of database users that are allowed to connect and run all commands on the
console (default `[]`).

The list will be transformed to a coma separated list in the configuration
file.

Example:

```yaml
pgbouncer_admin_users:
  - pgbouncer
```

See [admin_users](https://www.pgbouncer.org/config.html#admin_users) for
details.

### pgbouncer_stats_users

List of database users that are allowed to connect and run read-only queries on
the console.

The list will be transformed to a coma separated list in the configuration
file.

Example:

```yaml
pgbouncer_stats_users:
  - monitoring
```

See [stats_users](https://www.pgbouncer.org/config.html#stats_users) for
details.

### pgbouncer_max_client_conn

Maximum number of client connections allowed (default `100`).

See [max_client_conn](https://www.pgbouncer.org/config.html#max_client_conn)
for details.

### pgbouncer_default_pool_size

How many server connections to allow per user/database pair (default `20`).

See
[default_pool_size](https://www.pgbouncer.org/config.html#default_pool_size)
for details.

### pgbouncer_pool_mode

Specifies when a server connection can be reused by other clients (not
specified by default).

See [pool_mode](https://www.pgbouncer.org/config.html#pool_mode) for details.

### pgbouncer_ignore_startup_parameters

List of parameters to ignore in startup packets (default `[]`).

The list will be transformed to a coma separated list in the configuration
file.

Example:

```yaml
pgbouncer_ignore_startup_parameters:
  - extra_float_digits
```

See
[ignore_startup_parameters](https://www.pgbouncer.org/config.html#ignore_startup_parameters)
for details.

### pgbouncer_auth_users

Dictionary of authentication settings used to create the authentication file
(default `{}`). The key is the username. The value is the password hash.

Example:

```yaml
pgbouncer_auth_users:
  test: >-
    SCRAM-SHA-256$4096:OvAMtQRBpRRUh0rWqL92TQ==$Ib2aGliOfl49+FV5QLtF0F3fEy3794fDkvG66Vums60=:lGAPGbTbzhnr5ms6FmTgm6fZ6CNxInzVdaHnw43IgMQ=
```

See [Authentication file
format](https://www.pgbouncer.org/config.html#authentication-file-format) for
details.

### pgbouncer_service_after

List of systemd units to wait before starting PgBouncer.

Example:

```yaml
pgbouncer_service_after:
  - tailscaled.service
```
