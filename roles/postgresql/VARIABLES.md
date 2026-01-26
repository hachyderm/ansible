# Variables

See [defaults/main.yml](defaults/main.yml) for the defaults.

### postgresql_version

Version of the PostgreSQL binaries (default `15`).

Upgrading this version will deploy a new independent cluster without upgrading
an existing one.

### postgresql_cluster_name

Name of the cluster (default `main`).

Useful when multiple clusters are deployed on the same server.

### postgresql_initdb_args

Arguments passed to `initdb` to create a new cluster (default `-k` to enable
checksums).

See [initdb](https://www.postgresql.org/docs/current/app-initdb.html).

### postgresql_data_directory

See
[data_directory](https://www.postgresql.org/docs/current/runtime-config-file-locations.html#GUC-DATA-DIRECTORY).

### postgresql_listen_addresses

List of addresses PostgreSQL will listen to (default `["localhost"]`).

This list will be transformed to a coma separated list by the role.

See
[listen_addresses](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-LISTEN-ADDRESSES).

### postgresql_archive_mode

Enable or disable WAL archiving (default `"on"`).

Because this mode can only be at server start, it is a good idea to enable it
then use an archive command that does nothing so you can change the archive
command later without a restart.

See
[archive_mode](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-ARCHIVE-MODE).

### postgresql_archive_command

See
[archive_command](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-ARCHIVE-COMMAND).

### postgresql_restore_command

See
[restore_command](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-RESTORE-COMMAND).

### postgresql_logging_collector

See
[logging_collector](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOGGING-COLLECTOR).

### postgresql_log_timezone

See
[log_timezone](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-TIMEZONE)
for more details.

### postgresql_log_destination

See
[log_destination](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-DESTINATION)
for more details.

### postgresql_log_directory

See
[log_directory](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-DIRECTORY)
for more details.

### postgresql_log_filename

See
[log_filename](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-FILENAME)
for more details.

### postgresql_log_file_mode

See
[log_file_mode](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-FILE-MODE)
for more details.

### postgresql_settings

Dictionary of custom settings where the key is the name of the setting and
value is the value of the setting.

Example:

```yaml
postgresql_settings:
  max_connections: 1024
  shared_buffers: 25GB
```

### postgresql_hba_rules

List of host-based authentication rules.

Defaults:

```yaml
postgresql_hba_rules:
  - "local all all scram-sha-256      # allow local connections with secure password"
  - "host  all all all scram-sha-256  # allow host (with and without TLS) with secure password"
```

See [The pg_hba.conf
File](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html).

### postgresql_manage_pgpass

Create `.pgpass` files for `root` and `postgres` or not (default `false`).

See [The Password
File](https://www.postgresql.org/docs/current/libpq-pgpass.html).

Required for [pgBackRest](https://pgbackrest.org/).

### postgresql_manage_replication

Configure replication on a replica (default `false`).

This operation will **remove the current data directory** to synchronize with a
primary.

### postgresql_wal_level

See
[wal_level](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-WAL-LEVEL).

### postgresql_replication_username

Name of the replication user (default `repl`).

### postgresql_replication_password

Password of the replication user.

### postgresql_replication_network

IP range of the network used for the replication to allow in the pg_hba.conf to
setup the replication.

### postgresql_max_number_of_replicas

Defines
[max_wal_senders](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS)
and
[max_replication_slots](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS).

### postgresql_instance_role

Configure the instance to be a `primary` or a `replica` (default `primary`).

This variable does not promote a replica to primary.

### postgresql_replication_slot_name

Name of the replication slot (default `{{ inventory_hostname }}`).

### postgresql_primary_host

In a replication setup, define where to find the primary host.

### postgresql_primary_port

In a replication setup, define where to find the primary port.

### postgresql_users

List of users to create.

Example:

```yaml
postgresql_users:
- name: monitoring
  password: ***
  roles:
    - pg_monitor
```

### postgresql_service_after

List of systemd units to wait before starting PostgreSQL.

Example:

```yaml
postgresql_service_after:
  - tailscaled.service
```

### postgresql_upgrade_from_version

Used to perform major upgrades. Tell Ansible what version the cluster to
upgrade is running. Required for
[pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html).

### postgresql_upgrade_drop_cluster

Once upgraded, remove the old cluster (default `true`).

### postgresql_upgrade_remove_packages

Once upgraded, remove the old packages (default `true`).
