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

## Table of Content

<!-- ANSIBLE DOCSMITH TOC START -->
* [Role variables](#variables)
  * [`postgresql_version`](#variable-postgresql_version)
  * [`postgresql_port`](#variable-postgresql_port)
  * [`postgresql_cluster_name`](#variable-postgresql_cluster_name)
  * [`postgresql_initdb_args`](#variable-postgresql_initdb_args)
  * [`postgresql_data_directory`](#variable-postgresql_data_directory)
  * [`postgresql_listen_addresses`](#variable-postgresql_listen_addresses)
  * [`postgresql_archive_mode`](#variable-postgresql_archive_mode)
  * [`postgresql_archive_command`](#variable-postgresql_archive_command)
  * [`postgresql_restore_command`](#variable-postgresql_restore_command)
  * [`postgresql_logging_collector`](#variable-postgresql_logging_collector)
  * [`postgresql_log_timezone`](#variable-postgresql_log_timezone)
  * [`postgresql_log_destination`](#variable-postgresql_log_destination)
  * [`postgresql_log_directory`](#variable-postgresql_log_directory)
  * [`postgresql_log_filename`](#variable-postgresql_log_filename)
  * [`postgresql_log_file_mode`](#variable-postgresql_log_file_mode)
  * [`postgresql_settings`](#variable-postgresql_settings)
  * [`postgresql_hba_rules`](#variable-postgresql_hba_rules)
  * [`postgresql_manage_pgpass`](#variable-postgresql_manage_pgpass)
  * [`postgresql_manage_replication`](#variable-postgresql_manage_replication)
  * [`postgresql_wal_level`](#variable-postgresql_wal_level)
  * [`postgresql_replication_username`](#variable-postgresql_replication_username)
  * [`postgresql_replication_password`](#variable-postgresql_replication_password)
  * [`postgresql_replication_network`](#variable-postgresql_replication_network)
  * [`postgresql_max_number_of_replicas`](#variable-postgresql_max_number_of_replicas)
  * [`postgresql_instance_role`](#variable-postgresql_instance_role)
  * [`postgresql_replication_slot_name`](#variable-postgresql_replication_slot_name)
  * [`postgresql_primary_host`](#variable-postgresql_primary_host)
  * [`postgresql_primary_port`](#variable-postgresql_primary_port)
  * [`postgresql_users`](#variable-postgresql_users)
  * [`postgresql_service_after`](#variable-postgresql_service_after)
  * [`postgresql_upgrade_from_version`](#variable-postgresql_upgrade_from_version)
  * [`postgresql_upgrade_drop_cluster`](#variable-postgresql_upgrade_drop_cluster)
  * [`postgresql_upgrade_remove_packages`](#variable-postgresql_upgrade_remove_packages)
<!-- ANSIBLE DOCSMITH TOC END -->
<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description (abstract) |
|----------|------|----------|---------|------------------------|
| `postgresql_version` | `str` | No | `15` | Version of the PostgreSQL binaries.<br><br>Upgrading this version will deploy a new independent cluster without upgrading one.<br><br>See C(postgresql_upgrade_from_version) for upgrades. |
| `postgresql_port` | `int` | No | `5432` | The TCP port the server listens on. |
| `postgresql_cluster_name` | `str` | No | `"main"` | Name of the cluster.<br><br>Useful when multiple clusters are deployed on the same server. |
| `postgresql_initdb_args` | `str` | No | `"-k"` | Arguments passed to C(initdb) to create a new cluster.<br><br>See L(initdb,https://www.postgresql.org/docs/current/app-initdb.html). |
| `postgresql_data_directory` | `str` | No | N/A | Specifies the directory to use for data storage.<br><br>See L(data_directory,https://www.postgresql.org/docs/current/runtime-config-file-locations.html#GUC-DATA-DIRECTORY). |
| `postgresql_listen_addresses` | `list` | No | `['localhost']` | List of addresses PostgreSQL will listen to.<br><br>This list will be transformed to a coma separated list by the role.<br><br>See L(listen_addresses,https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-LISTEN-ADDRESSES). |
| `postgresql_archive_mode` | `str` | No | `"on"` | Enable or disable WAL archiving.<br><br>Because this mode can only be at server start, it is a good idea to enable it then use an archive command that does nothing so you can change the archive command later without a restart.<br><br>See […](#variable-postgresql_archive_mode) |
| `postgresql_archive_command` | `str` | No | N/A | Command to archive WAL files.<br><br>See L(archive_command,https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-ARCHIVE-COMMAND). |
| `postgresql_restore_command` | `str` | No | N/A | Command to restore WAL files.<br><br>See L(restore_command,https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-RESTORE-COMMAND). |
| `postgresql_logging_collector` | `str` | No | `"on"` | Enable or disable the logging collector.<br><br>See L(logging_collector,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOGGING-COLLECTOR). |
| `postgresql_log_timezone` | `str` | No | N/A | Sets the time zone used for timestamps written in the server log.<br><br>See L(log_timezone,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-TIMEZONE). |
| `postgresql_log_destination` | `str` | No | N/A | Sets the destination of the logs.<br><br>See L(log_destination,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-DESTINATION). |
| `postgresql_log_directory` | `str` | No | N/A | When C(postgresql_logging_collector) is enabled, this parameter determines the directory in which log files will be created.<br><br>See L(log_directory,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-DIRECTORY). |
| `postgresql_log_filename` | `str` | No | N/A | When C(postgresql_logging_collector) is enabled, this parameter sets the file names of the created log files.<br><br>See L(log_filename,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-FILENAME). |
| `postgresql_log_file_mode` | `str` | No | N/A | On Unix systems this parameter sets the permissions for log files when C(postgresql_logging_collector) is enabled.<br><br>See L(log_file_mode,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-FILE-MODE). |
| `postgresql_settings` | `dict` | No | N/A | Dictionary of custom settings.<br><br>The key is the name of the setting.<br><br>The value is the value of the setting. |
| `postgresql_hba_rules` | `list` | No | `['local all all scram-sha-256      # allow local connections with secure password', 'host  all all all scram-sha-256  # allow host (with and without TLS) with secure password']` | List of host-based authentication rules.<br><br>See L(The pg_hba.conf File,https://www.postgresql.org/docs/current/auth-pg-hba-conf.html). |
| `postgresql_manage_pgpass` | `bool` | No | `false` | Create the C(.pgpass) files for C(root) and C(postgres) or not.<br><br>See L(The Password File,https://www.postgresql.org/docs/current/libpq-pgpass.html). |
| `postgresql_manage_replication` | `bool` | No | `false` | Configure replication on a replica.<br><br>This operation will REMOVE THE DATA DIRECTORY to synchronize with a primary. |
| `postgresql_wal_level` | `str` | No | N/A | Determines how much information is written to the WAL.<br><br>See L(wal_level,https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-WAL-LEVEL). |
| `postgresql_replication_username` | `str` | No | `"repl"` | Name of the replication user. |
| `postgresql_replication_password` | `str` | No | N/A | Password of the replication user. |
| `postgresql_replication_network` | `str` | No | `"127.0.0.1/32"` | IP range of the network used for the replication to allow in the C(pg_hba.conf) to setup the replication. |
| `postgresql_max_number_of_replicas` | `int` | No | `10` | Defines L(max_wal_senders,https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS) and L(max_replication_slots,https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS). |
| `postgresql_instance_role` | `str` | No | `"primary"` | Role of the instance.<br><br>Configure replication settings.<br><br>This variable does not promote a replica to primary. |
| `postgresql_replication_slot_name` | `str` | No | `"{{ inventory_hostname }}"` | In a replication setup, define the name of the replication slot. |
| `postgresql_primary_host` | `str` | No | N/A | In a replication setup, define where to find the primary host. |
| `postgresql_primary_port` | `str` | No | `5432` | In a replication setup, define where to find the primary port. |
| `postgresql_users` | `list` | No | N/A | List of users to create.<br><br>The key of the dict in the list must have a C(name) and a C(password).<br><br>The key of the dict in the list can have a list of C(roles). |
| `postgresql_service_after` | `list` | No | N/A | List of systemd units to wait before starting the service. |
| `postgresql_upgrade_from_version` | `str` | No | N/A | Used to perform major upgrades.<br><br>Tell what version the cluster to upgrade is running.<br><br>Required for L(pg_upgrade,https://www.postgresql.org/docs/current/pgupgrade.html). |
| `postgresql_upgrade_drop_cluster` | `bool` | No | `true` | Once upgraded, remove the old cluster. |
| `postgresql_upgrade_remove_packages` | `bool` | No | `true` | Once upgraded, remove the old packages. |

### `postgresql_version`<a id="variable-postgresql_version"></a>

[*⇑ Back to ToC ⇑*](#toc)

Version of the PostgreSQL binaries.

Upgrading this version will deploy a new independent cluster without upgrading one.

See C(postgresql_upgrade_from_version) for upgrades.

- **Type**: `str`
- **Required**: No
- **Default**: `15`



### `postgresql_port`<a id="variable-postgresql_port"></a>

[*⇑ Back to ToC ⇑*](#toc)

The TCP port the server listens on.

- **Type**: `int`
- **Required**: No
- **Default**: `5432`



### `postgresql_cluster_name`<a id="variable-postgresql_cluster_name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Name of the cluster.

Useful when multiple clusters are deployed on the same server.

- **Type**: `str`
- **Required**: No
- **Default**: `"main"`



### `postgresql_initdb_args`<a id="variable-postgresql_initdb_args"></a>

[*⇑ Back to ToC ⇑*](#toc)

Arguments passed to C(initdb) to create a new cluster.

See L(initdb,https://www.postgresql.org/docs/current/app-initdb.html).

- **Type**: `str`
- **Required**: No
- **Default**: `"-k"`



### `postgresql_data_directory`<a id="variable-postgresql_data_directory"></a>

[*⇑ Back to ToC ⇑*](#toc)

Specifies the directory to use for data storage.

See L(data_directory,https://www.postgresql.org/docs/current/runtime-config-file-locations.html#GUC-DATA-DIRECTORY).

- **Type**: `str`
- **Required**: No



### `postgresql_listen_addresses`<a id="variable-postgresql_listen_addresses"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of addresses PostgreSQL will listen to.

This list will be transformed to a coma separated list by the role.

See L(listen_addresses,https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-LISTEN-ADDRESSES).

- **Type**: `list`
- **Required**: No
- **Default**: `['localhost']`
- **List Elements**: `str`



### `postgresql_archive_mode`<a id="variable-postgresql_archive_mode"></a>

[*⇑ Back to ToC ⇑*](#toc)

Enable or disable WAL archiving.

Because this mode can only be at server start, it is a good idea to enable it then use an archive command that does nothing so you can change the archive command later without a restart.

See L(archive_mode,https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-ARCHIVE-MODE).

- **Type**: `str`
- **Required**: No
- **Default**: `"on"`
- **Choices**: `on`, `off`



### `postgresql_archive_command`<a id="variable-postgresql_archive_command"></a>

[*⇑ Back to ToC ⇑*](#toc)

Command to archive WAL files.

See L(archive_command,https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-ARCHIVE-COMMAND).

- **Type**: `str`
- **Required**: No



### `postgresql_restore_command`<a id="variable-postgresql_restore_command"></a>

[*⇑ Back to ToC ⇑*](#toc)

Command to restore WAL files.

See L(restore_command,https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-RESTORE-COMMAND).

- **Type**: `str`
- **Required**: No



### `postgresql_logging_collector`<a id="variable-postgresql_logging_collector"></a>

[*⇑ Back to ToC ⇑*](#toc)

Enable or disable the logging collector.

See L(logging_collector,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOGGING-COLLECTOR).

- **Type**: `str`
- **Required**: No
- **Default**: `"on"`
- **Choices**: `on`, `off`



### `postgresql_log_timezone`<a id="variable-postgresql_log_timezone"></a>

[*⇑ Back to ToC ⇑*](#toc)

Sets the time zone used for timestamps written in the server log.

See L(log_timezone,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-TIMEZONE).

- **Type**: `str`
- **Required**: No



### `postgresql_log_destination`<a id="variable-postgresql_log_destination"></a>

[*⇑ Back to ToC ⇑*](#toc)

Sets the destination of the logs.

See L(log_destination,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-DESTINATION).

- **Type**: `str`
- **Required**: No



### `postgresql_log_directory`<a id="variable-postgresql_log_directory"></a>

[*⇑ Back to ToC ⇑*](#toc)

When C(postgresql_logging_collector) is enabled, this parameter determines the directory in which log files will be created.

See L(log_directory,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-DIRECTORY).

- **Type**: `str`
- **Required**: No



### `postgresql_log_filename`<a id="variable-postgresql_log_filename"></a>

[*⇑ Back to ToC ⇑*](#toc)

When C(postgresql_logging_collector) is enabled, this parameter sets the file names of the created log files.

See L(log_filename,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-FILENAME).

- **Type**: `str`
- **Required**: No



### `postgresql_log_file_mode`<a id="variable-postgresql_log_file_mode"></a>

[*⇑ Back to ToC ⇑*](#toc)

On Unix systems this parameter sets the permissions for log files when C(postgresql_logging_collector) is enabled.

See L(log_file_mode,https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-FILE-MODE).

- **Type**: `str`
- **Required**: No



### `postgresql_settings`<a id="variable-postgresql_settings"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of custom settings.

The key is the name of the setting.

The value is the value of the setting.

- **Type**: `dict`
- **Required**: No



### `postgresql_hba_rules`<a id="variable-postgresql_hba_rules"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of host-based authentication rules.

See L(The pg_hba.conf File,https://www.postgresql.org/docs/current/auth-pg-hba-conf.html).

- **Type**: `list`
- **Required**: No
- **Default**: `['local all all scram-sha-256      # allow local connections with secure password', 'host  all all all scram-sha-256  # allow host (with and without TLS) with secure password']`
- **List Elements**: `str`



### `postgresql_manage_pgpass`<a id="variable-postgresql_manage_pgpass"></a>

[*⇑ Back to ToC ⇑*](#toc)

Create the C(.pgpass) files for C(root) and C(postgres) or not.

See L(The Password File,https://www.postgresql.org/docs/current/libpq-pgpass.html).

- **Type**: `bool`
- **Required**: No
- **Default**: `false`



### `postgresql_manage_replication`<a id="variable-postgresql_manage_replication"></a>

[*⇑ Back to ToC ⇑*](#toc)

Configure replication on a replica.

This operation will REMOVE THE DATA DIRECTORY to synchronize with a primary.

- **Type**: `bool`
- **Required**: No
- **Default**: `false`



### `postgresql_wal_level`<a id="variable-postgresql_wal_level"></a>

[*⇑ Back to ToC ⇑*](#toc)

Determines how much information is written to the WAL.

See L(wal_level,https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-WAL-LEVEL).

- **Type**: `str`
- **Required**: No
- **Choices**: `replica`, `minimal`, `logical`



### `postgresql_replication_username`<a id="variable-postgresql_replication_username"></a>

[*⇑ Back to ToC ⇑*](#toc)

Name of the replication user.

- **Type**: `str`
- **Required**: No
- **Default**: `"repl"`



### `postgresql_replication_password`<a id="variable-postgresql_replication_password"></a>

[*⇑ Back to ToC ⇑*](#toc)

Password of the replication user.

- **Type**: `str`
- **Required**: No



### `postgresql_replication_network`<a id="variable-postgresql_replication_network"></a>

[*⇑ Back to ToC ⇑*](#toc)

IP range of the network used for the replication to allow in the C(pg_hba.conf) to setup the replication.

- **Type**: `str`
- **Required**: No
- **Default**: `"127.0.0.1/32"`



### `postgresql_max_number_of_replicas`<a id="variable-postgresql_max_number_of_replicas"></a>

[*⇑ Back to ToC ⇑*](#toc)

Defines L(max_wal_senders,https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS) and L(max_replication_slots,https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS).

- **Type**: `int`
- **Required**: No
- **Default**: `10`



### `postgresql_instance_role`<a id="variable-postgresql_instance_role"></a>

[*⇑ Back to ToC ⇑*](#toc)

Role of the instance.

Configure replication settings.

This variable does not promote a replica to primary.

- **Type**: `str`
- **Required**: No
- **Default**: `"primary"`
- **Choices**: `primary`, `replica`



### `postgresql_replication_slot_name`<a id="variable-postgresql_replication_slot_name"></a>

[*⇑ Back to ToC ⇑*](#toc)

In a replication setup, define the name of the replication slot.

- **Type**: `str`
- **Required**: No
- **Default**: `"{{ inventory_hostname }}"`



### `postgresql_primary_host`<a id="variable-postgresql_primary_host"></a>

[*⇑ Back to ToC ⇑*](#toc)

In a replication setup, define where to find the primary host.

- **Type**: `str`
- **Required**: No



### `postgresql_primary_port`<a id="variable-postgresql_primary_port"></a>

[*⇑ Back to ToC ⇑*](#toc)

In a replication setup, define where to find the primary port.

- **Type**: `str`
- **Required**: No
- **Default**: `5432`



### `postgresql_users`<a id="variable-postgresql_users"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of users to create.

The key of the dict in the list must have a C(name) and a C(password).

The key of the dict in the list can have a list of C(roles).

- **Type**: `list`
- **Required**: No
- **List Elements**: `dict`



### `postgresql_service_after`<a id="variable-postgresql_service_after"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of systemd units to wait before starting the service.

- **Type**: `list`
- **Required**: No



### `postgresql_upgrade_from_version`<a id="variable-postgresql_upgrade_from_version"></a>

[*⇑ Back to ToC ⇑*](#toc)

Used to perform major upgrades.

Tell what version the cluster to upgrade is running.

Required for L(pg_upgrade,https://www.postgresql.org/docs/current/pgupgrade.html).

- **Type**: `str`
- **Required**: No



### `postgresql_upgrade_drop_cluster`<a id="variable-postgresql_upgrade_drop_cluster"></a>

[*⇑ Back to ToC ⇑*](#toc)

Once upgraded, remove the old cluster.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`



### `postgresql_upgrade_remove_packages`<a id="variable-postgresql_upgrade_remove_packages"></a>

[*⇑ Back to ToC ⇑*](#toc)

Once upgraded, remove the old packages.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`




<!-- ANSIBLE DOCSMITH MAIN END -->

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
