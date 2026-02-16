# Ansible Role: PgBouncer

An Ansible role for installing and configuring
[PgBouncer](https://www.pgbouncer.org/), a lightweight connection pooler for
PostgreSQL.

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)
* `pgdg_repository` role

## Table of Content

<!-- ANSIBLE DOCSMITH TOC START -->
* [Role variables](#variables)
  * [`pgbouncer_databases`](#variable-pgbouncer_databases)
  * [`pgbouncer_users`](#variable-pgbouncer_users)
  * [`pgbouncer_listen_addr`](#variable-pgbouncer_listen_addr)
  * [`pgbouncer_listen_port`](#variable-pgbouncer_listen_port)
  * [`pgbouncer_logfile`](#variable-pgbouncer_logfile)
  * [`pgbouncer_pidfile`](#variable-pgbouncer_pidfile)
  * [`pgbouncer_auth_type`](#variable-pgbouncer_auth_type)
  * [`pgbouncer_auth_file`](#variable-pgbouncer_auth_file)
  * [`pgbouncer_admin_users`](#variable-pgbouncer_admin_users)
  * [`pgbouncer_stats_users`](#variable-pgbouncer_stats_users)
  * [`pgbouncer_max_client_conn`](#variable-pgbouncer_max_client_conn)
  * [`pgbouncer_default_pool_size`](#variable-pgbouncer_default_pool_size)
  * [`pgbouncer_pool_mode`](#variable-pgbouncer_pool_mode)
  * [`pgbouncer_ignore_startup_parameters`](#variable-pgbouncer_ignore_startup_parameters)
  * [`pgbouncer_auth_users`](#variable-pgbouncer_auth_users)
  * [`pgbouncer_service_after`](#variable-pgbouncer_service_after)
<!-- ANSIBLE DOCSMITH TOC END -->
<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description (abstract) |
|----------|------|----------|---------|------------------------|
| `pgbouncer_databases` | `dict` | No | N/A | Dictionary of databases connections strings.<br><br>The key is the database name.<br><br>The value is the connection string.<br><br>See L(Section [databases],https://www.pgbouncer.org/config.html#section-databases). |
| `pgbouncer_users` | `dict` | No | N/A | Dictionary of users.<br><br>The key is the user name.<br><br>The value is the user settings.<br><br>See L(Section [users],https://www.pgbouncer.org/config.html#section-users). |
| `pgbouncer_listen_addr` | `list` | No | `['localhost']` | List of addresses to listen.<br><br>See L(listen_addr,https://www.pgbouncer.org/config.html#listen_addr). |
| `pgbouncer_listen_port` | `int` | No | `6432` | Which port to listen on.<br><br>See L(listen_port,https://www.pgbouncer.org/config.html#listen_port). |
| `pgbouncer_logfile` | `path` | No | `"/var/log/postgresql/pgbouncer.log"` | Path to the log file.<br><br>See L(logfile,https://www.pgbouncer.org/config.html#logfile). |
| `pgbouncer_pidfile` | `path` | No | `"/var/run/postgresql/pgbouncer.pid"` | Path to PID file.<br><br>See L(pidfile,https://www.pgbouncer.org/config.html#pidfile). |
| `pgbouncer_auth_type` | `str` | No | `"scram-sha-256"` | How to authenticate users.<br><br>See L(auth_type,https://www.pgbouncer.org/config.html#auth_type). |
| `pgbouncer_auth_file` | `path` | No | `"/etc/pgbouncer/userlist.txt"` | Path to the authentication file.<br><br>See L(auth_file,https://www.pgbouncer.org/config.html#auth_file). |
| `pgbouncer_admin_users` | `list` | No | N/A | List of database users that are allowed to connect and run all commands on the console.<br><br>See L(admin_users,https://www.pgbouncer.org/config.html#admin_users). |
| `pgbouncer_stats_users` | `list` | No | N/A | List of database users that are allowed to connect and run read-only queries on the console.<br><br>The list will be transformed to a coma separated list in the configuration file.<br><br>See […](#variable-pgbouncer_stats_users) |
| `pgbouncer_max_client_conn` | `int` | No | `100` | Maximum number of client connections allowed.<br><br>See L(max_client_conn,https://www.pgbouncer.org/config.html#max_client_conn). |
| `pgbouncer_default_pool_size` | `int` | No | `20` | How many server connections to allow per user/database pair.<br><br>See L(default_pool_size,https://www.pgbouncer.org/config.html#default_pool_size). |
| `pgbouncer_pool_mode` | `str` | No | N/A | Specifies when a server connection can be reused by other clients.<br><br>See L(pool_mode,https://www.pgbouncer.org/config.html#pool_mode). |
| `pgbouncer_ignore_startup_parameters` | `list` | No | N/A | List of parameters to ignore in startup packets.<br><br>The list will be transformed to a coma separated list in the configuration file.<br><br>See L(ignore_startup_parameters,https://www.pgbouncer.org/config.html#ignore_startup_parameters). |
| `pgbouncer_auth_users` | `dict` | No | N/A | Dictionary of authentication settings used to create the authentication file.<br><br>The key is the username.<br><br>The value is the password hash. |
| `pgbouncer_service_after` | `list` | No | N/A | List of systemd units to wait before starting the service. |

### `pgbouncer_databases`<a id="variable-pgbouncer_databases"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of databases connections strings.

The key is the database name.

The value is the connection string.

See L(Section [databases],https://www.pgbouncer.org/config.html#section-databases).

- **Type**: `dict`
- **Required**: No



### `pgbouncer_users`<a id="variable-pgbouncer_users"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of users.

The key is the user name.

The value is the user settings.

See L(Section [users],https://www.pgbouncer.org/config.html#section-users).

- **Type**: `dict`
- **Required**: No



### `pgbouncer_listen_addr`<a id="variable-pgbouncer_listen_addr"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of addresses to listen.

See L(listen_addr,https://www.pgbouncer.org/config.html#listen_addr).

- **Type**: `list`
- **Required**: No
- **Default**: `['localhost']`
- **List Elements**: `str`



### `pgbouncer_listen_port`<a id="variable-pgbouncer_listen_port"></a>

[*⇑ Back to ToC ⇑*](#toc)

Which port to listen on.

See L(listen_port,https://www.pgbouncer.org/config.html#listen_port).

- **Type**: `int`
- **Required**: No
- **Default**: `6432`



### `pgbouncer_logfile`<a id="variable-pgbouncer_logfile"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the log file.

See L(logfile,https://www.pgbouncer.org/config.html#logfile).

- **Type**: `path`
- **Required**: No
- **Default**: `"/var/log/postgresql/pgbouncer.log"`



### `pgbouncer_pidfile`<a id="variable-pgbouncer_pidfile"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to PID file.

See L(pidfile,https://www.pgbouncer.org/config.html#pidfile).

- **Type**: `path`
- **Required**: No
- **Default**: `"/var/run/postgresql/pgbouncer.pid"`



### `pgbouncer_auth_type`<a id="variable-pgbouncer_auth_type"></a>

[*⇑ Back to ToC ⇑*](#toc)

How to authenticate users.

See L(auth_type,https://www.pgbouncer.org/config.html#auth_type).

- **Type**: `str`
- **Required**: No
- **Default**: `"scram-sha-256"`



### `pgbouncer_auth_file`<a id="variable-pgbouncer_auth_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the authentication file.

See L(auth_file,https://www.pgbouncer.org/config.html#auth_file).

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/pgbouncer/userlist.txt"`



### `pgbouncer_admin_users`<a id="variable-pgbouncer_admin_users"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of database users that are allowed to connect and run all commands on the console.

See L(admin_users,https://www.pgbouncer.org/config.html#admin_users).

- **Type**: `list`
- **Required**: No



### `pgbouncer_stats_users`<a id="variable-pgbouncer_stats_users"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of database users that are allowed to connect and run read-only queries on the console.

The list will be transformed to a coma separated list in the configuration file.

See L(stats_users,https://www.pgbouncer.org/config.html#stats_users).

- **Type**: `list`
- **Required**: No



### `pgbouncer_max_client_conn`<a id="variable-pgbouncer_max_client_conn"></a>

[*⇑ Back to ToC ⇑*](#toc)

Maximum number of client connections allowed.

See L(max_client_conn,https://www.pgbouncer.org/config.html#max_client_conn).

- **Type**: `int`
- **Required**: No
- **Default**: `100`



### `pgbouncer_default_pool_size`<a id="variable-pgbouncer_default_pool_size"></a>

[*⇑ Back to ToC ⇑*](#toc)

How many server connections to allow per user/database pair.

See L(default_pool_size,https://www.pgbouncer.org/config.html#default_pool_size).

- **Type**: `int`
- **Required**: No
- **Default**: `20`



### `pgbouncer_pool_mode`<a id="variable-pgbouncer_pool_mode"></a>

[*⇑ Back to ToC ⇑*](#toc)

Specifies when a server connection can be reused by other clients.

See L(pool_mode,https://www.pgbouncer.org/config.html#pool_mode).

- **Type**: `str`
- **Required**: No
- **Choices**: `session`, `transaction`, `statement`



### `pgbouncer_ignore_startup_parameters`<a id="variable-pgbouncer_ignore_startup_parameters"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of parameters to ignore in startup packets.

The list will be transformed to a coma separated list in the configuration file.

See L(ignore_startup_parameters,https://www.pgbouncer.org/config.html#ignore_startup_parameters).

- **Type**: `list`
- **Required**: No



### `pgbouncer_auth_users`<a id="variable-pgbouncer_auth_users"></a>

[*⇑ Back to ToC ⇑*](#toc)

Dictionary of authentication settings used to create the authentication file.

The key is the username.

The value is the password hash.

- **Type**: `dict`
- **Required**: No



### `pgbouncer_service_after`<a id="variable-pgbouncer_service_after"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of systemd units to wait before starting the service.

- **Type**: `list`
- **Required**: No




<!-- ANSIBLE DOCSMITH MAIN END -->

## Example

```yaml
- hosts: all
  become: true
  roles:
    - hachyderm.general.pgbouncer
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
