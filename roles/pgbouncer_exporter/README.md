# Ansible Role: PgBouncer Exporter

An Ansible role for installing and configuring [PgBouncer
Exporter](https://github.com/prometheus-community/pgbouncer_exporter).

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)

## Table of content

<!-- ANSIBLE DOCSMITH TOC START -->
* [Role variables](#variables)
  * [`pgbouncer_exporter_version`](#variable-pgbouncer_exporter_version)
  * [`pgbouncer_exporter_os`](#variable-pgbouncer_exporter_os)
  * [`pgbouncer_exporter_arch`](#variable-pgbouncer_exporter_arch)
  * [`pgbouncer_exporter_download_url`](#variable-pgbouncer_exporter_download_url)
  * [`pgbouncer_exporter_checksum`](#variable-pgbouncer_exporter_checksum)
  * [`pgbouncer_exporter_bin`](#variable-pgbouncer_exporter_bin)
  * [`pgbouncer_exporter_user`](#variable-pgbouncer_exporter_user)
  * [`pgbouncer_exporter_group`](#variable-pgbouncer_exporter_group)
  * [`pgbouncer_exporter_port`](#variable-pgbouncer_exporter_port)
  * [`pgbouncer_exporter_telemetry_path`](#variable-pgbouncer_exporter_telemetry_path)
  * [`pgbouncer_exporter_connection_string`](#variable-pgbouncer_exporter_connection_string)
<!-- ANSIBLE DOCSMITH TOC END -->
<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description (abstract) |
|----------|------|----------|---------|------------------------|
| `pgbouncer_exporter_version` | `str` | No | `"0.11.0"` | Version of the exporter. |
| `pgbouncer_exporter_os` | `str` | No | `"linux"` | Operating system of where the exporter will be installed. |
| `pgbouncer_exporter_arch` | `str` | No | `"amd64"` | Architecture of the system where the exporter will be installed. |
| `pgbouncer_exporter_download_url` | `str` | No | `"https://github.com/prometheus-community/pgbouncer_exporter/releases/download/v{{ pgbouncer_exporter_version }}/ pgbouncer_exporter-{{ pgbouncer_exporter_version }}.{{ pgbouncer_exporter_os }}-{{ pgbouncer_exporter_arch }}.tar.gz"` | URL used to download the exporter archive. |
| `pgbouncer_exporter_checksum` | `str` | No | `"de95a3d22141c0f84ac33de07e793c4993410f43d7c10e8ba281559381e031da"` | Checksum of the downloaded archive to avoid supply-chain attack. |
| `pgbouncer_exporter_bin` | `path` | No | `"/usr/local/bin/pgbouncer_exporter"` | Path to the exporter binary. |
| `pgbouncer_exporter_user` | `str` | No | `"pgbouncer-exp"` | User to create to run the exporter. |
| `pgbouncer_exporter_group` | `str` | No | `"{{ pgbouncer_exporter_user }}"` | Group to create for the user to run the exporter. |
| `pgbouncer_exporter_port` | `int` | No | `9127` | Port to listen for the exporter. |
| `pgbouncer_exporter_telemetry_path` | `str` | No | `"/metrics"` | Route to scrap metrics on the exporter. |
| `pgbouncer_exporter_connection_string` | `str` | No | `"postgres://postgres:@localhost:6543/pgbouncer?sslmode=disable"` | URI to connect to PgBouncer. |

### `pgbouncer_exporter_version`<a id="variable-pgbouncer_exporter_version"></a>

[*⇑ Back to ToC ⇑*](#toc)

Version of the exporter.

- **Type**: `str`
- **Required**: No
- **Default**: `"0.11.0"`



### `pgbouncer_exporter_os`<a id="variable-pgbouncer_exporter_os"></a>

[*⇑ Back to ToC ⇑*](#toc)

Operating system of where the exporter will be installed.

- **Type**: `str`
- **Required**: No
- **Default**: `"linux"`



### `pgbouncer_exporter_arch`<a id="variable-pgbouncer_exporter_arch"></a>

[*⇑ Back to ToC ⇑*](#toc)

Architecture of the system where the exporter will be installed.

- **Type**: `str`
- **Required**: No
- **Default**: `"amd64"`



### `pgbouncer_exporter_download_url`<a id="variable-pgbouncer_exporter_download_url"></a>

[*⇑ Back to ToC ⇑*](#toc)

URL used to download the exporter archive.

- **Type**: `str`
- **Required**: No
- **Default**: `"https://github.com/prometheus-community/pgbouncer_exporter/releases/download/v{{ pgbouncer_exporter_version }}/ pgbouncer_exporter-{{ pgbouncer_exporter_version }}.{{ pgbouncer_exporter_os }}-{{ pgbouncer_exporter_arch }}.tar.gz"`



### `pgbouncer_exporter_checksum`<a id="variable-pgbouncer_exporter_checksum"></a>

[*⇑ Back to ToC ⇑*](#toc)

Checksum of the downloaded archive to avoid supply-chain attack.

- **Type**: `str`
- **Required**: No
- **Default**: `"de95a3d22141c0f84ac33de07e793c4993410f43d7c10e8ba281559381e031da"`



### `pgbouncer_exporter_bin`<a id="variable-pgbouncer_exporter_bin"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the exporter binary.

- **Type**: `path`
- **Required**: No
- **Default**: `"/usr/local/bin/pgbouncer_exporter"`



### `pgbouncer_exporter_user`<a id="variable-pgbouncer_exporter_user"></a>

[*⇑ Back to ToC ⇑*](#toc)

User to create to run the exporter.

- **Type**: `str`
- **Required**: No
- **Default**: `"pgbouncer-exp"`



### `pgbouncer_exporter_group`<a id="variable-pgbouncer_exporter_group"></a>

[*⇑ Back to ToC ⇑*](#toc)

Group to create for the user to run the exporter.

- **Type**: `str`
- **Required**: No
- **Default**: `"{{ pgbouncer_exporter_user }}"`



### `pgbouncer_exporter_port`<a id="variable-pgbouncer_exporter_port"></a>

[*⇑ Back to ToC ⇑*](#toc)

Port to listen for the exporter.

- **Type**: `int`
- **Required**: No
- **Default**: `9127`



### `pgbouncer_exporter_telemetry_path`<a id="variable-pgbouncer_exporter_telemetry_path"></a>

[*⇑ Back to ToC ⇑*](#toc)

Route to scrap metrics on the exporter.

- **Type**: `str`
- **Required**: No
- **Default**: `"/metrics"`



### `pgbouncer_exporter_connection_string`<a id="variable-pgbouncer_exporter_connection_string"></a>

[*⇑ Back to ToC ⇑*](#toc)

URI to connect to PgBouncer.

- **Type**: `str`
- **Required**: No
- **Default**: `"postgres://postgres:@localhost:6543/pgbouncer?sslmode=disable"`




<!-- ANSIBLE DOCSMITH MAIN END -->

## Example

Define a monitoring user on PostgreSQL:

> [!WARNING]
>
> The username and password described below are designed to be used For testing
> purpose only. You should update and encrypt those credentials to match your
> infrastructure.


```yaml
postgresql_users:
  - name: test
    password: test
```

Declare the monitoring user on PgBouncer:

```yaml
pgbouncer_auth_users:
  test: >-
    SCRAM-SHA-256$4096:K37HilrXKnHdsyvV+rljnA==$ZBT3gxWDJqqhG48uiEF+2cP0RnZRNkRcScsqNVzzUoE=:6iE872/7PWXTOqzRtLQ1SS3PD8pf+GnkLxqNC+jccuQ=
pgbouncer_stats_users:
  - test
pgbouncer_ignore_startup_parameters:
  - extra_float_digits
```

Deploy the exporter:

```yaml
- hosts: all
  roles:
    - hachyderm.general.pgbouncer_exporter
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
