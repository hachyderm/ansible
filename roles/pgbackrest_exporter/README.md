# Ansible Role: pgBackRest Exporter

An Ansible role for installing and configuring [pgBackRest
Exporter](https://github.com/woblerr/pgbackrest_exporter).

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)
* pgBackRest binary and configuration file

## Table of Content

<!-- ANSIBLE DOCSMITH TOC START -->
* [Role variables](#variables)
  * [`pgbackrest_exporter_version`](#variable-pgbackrest_exporter_version)
  * [`pgbackrest_exporter_os`](#variable-pgbackrest_exporter_os)
  * [`pgbackrest_exporter_arch`](#variable-pgbackrest_exporter_arch)
  * [`pgbackrest_exporter_download_url`](#variable-pgbackrest_exporter_download_url)
  * [`pgbackrest_exporter_checksum`](#variable-pgbackrest_exporter_checksum)
  * [`pgbackrest_exporter_bin`](#variable-pgbackrest_exporter_bin)
  * [`pgbackrest_exporter_user`](#variable-pgbackrest_exporter_user)
  * [`pgbackrest_exporter_group`](#variable-pgbackrest_exporter_group)
  * [`pgbackrest_exporter_config_file`](#variable-pgbackrest_exporter_config_file)
  * [`pgbackrest_exporter_port`](#variable-pgbackrest_exporter_port)
  * [`pgbackrest_exporter_telemetry_path`](#variable-pgbackrest_exporter_telemetry_path)
<!-- ANSIBLE DOCSMITH TOC END -->
<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description (abstract) |
|----------|------|----------|---------|------------------------|
| `pgbackrest_exporter_version` | `str` | No | `"0.22.0"` | Version of the exporter. |
| `pgbackrest_exporter_os` | `str` | No | `"linux"` | Operating system of where the exporter will be installed. |
| `pgbackrest_exporter_arch` | `str` | No | `"x86_64"` | Architecture of the system where the exporter will be installed. |
| `pgbackrest_exporter_download_url` | `str` | No | `"https://github.com/woblerr/pgbackrest_exporter/releases/download/v{{ pgbackrest_exporter_version }}/pgbackrest_exporter-{{ pgbackrest_exporter_version }}-{{ pgbackrest_exporter_os }}-{{ pgbackrest_exporter_arch }}.tar.gz"` | URL used to download the exporter archive. |
| `pgbackrest_exporter_checksum` | `str` | No | `"1562febbb006e96236e30ad0098757724614b2f29f87c1d210fed9083c4c31b5"` | Checksum of the downloaded archive to avoid supply-chain attack. |
| `pgbackrest_exporter_bin` | `path` | No | `"/usr/local/bin/pgbackrest_exporter"` | Path to the exporter binary. |
| `pgbackrest_exporter_user` | `str` | No | `"pgbackrest-exp"` | User to create to run the exporter. |
| `pgbackrest_exporter_group` | `str` | No | `"{{ pgbackrest_exporter_user }}"` | Group to create for the user to run the exporter. |
| `pgbackrest_exporter_config_file` | `path` | No | `"/etc/pgbackrest/pgbackrest.conf"` | Path to the configuration file of pgBackRest. |
| `pgbackrest_exporter_port` | `int` | No | `9854` | Port to listen for the exporter. |
| `pgbackrest_exporter_telemetry_path` | `str` | No | `"/metrics"` | Route to scrap metrics on the exporter. |

### `pgbackrest_exporter_version`<a id="variable-pgbackrest_exporter_version"></a>

[*⇑ Back to ToC ⇑*](#toc)

Version of the exporter.

- **Type**: `str`
- **Required**: No
- **Default**: `"0.22.0"`



### `pgbackrest_exporter_os`<a id="variable-pgbackrest_exporter_os"></a>

[*⇑ Back to ToC ⇑*](#toc)

Operating system of where the exporter will be installed.

- **Type**: `str`
- **Required**: No
- **Default**: `"linux"`



### `pgbackrest_exporter_arch`<a id="variable-pgbackrest_exporter_arch"></a>

[*⇑ Back to ToC ⇑*](#toc)

Architecture of the system where the exporter will be installed.

- **Type**: `str`
- **Required**: No
- **Default**: `"x86_64"`



### `pgbackrest_exporter_download_url`<a id="variable-pgbackrest_exporter_download_url"></a>

[*⇑ Back to ToC ⇑*](#toc)

URL used to download the exporter archive.

- **Type**: `str`
- **Required**: No
- **Default**: `"https://github.com/woblerr/pgbackrest_exporter/releases/download/v{{ pgbackrest_exporter_version }}/pgbackrest_exporter-{{ pgbackrest_exporter_version }}-{{ pgbackrest_exporter_os }}-{{ pgbackrest_exporter_arch }}.tar.gz"`



### `pgbackrest_exporter_checksum`<a id="variable-pgbackrest_exporter_checksum"></a>

[*⇑ Back to ToC ⇑*](#toc)

Checksum of the downloaded archive to avoid supply-chain attack.

- **Type**: `str`
- **Required**: No
- **Default**: `"1562febbb006e96236e30ad0098757724614b2f29f87c1d210fed9083c4c31b5"`



### `pgbackrest_exporter_bin`<a id="variable-pgbackrest_exporter_bin"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the exporter binary.

- **Type**: `path`
- **Required**: No
- **Default**: `"/usr/local/bin/pgbackrest_exporter"`



### `pgbackrest_exporter_user`<a id="variable-pgbackrest_exporter_user"></a>

[*⇑ Back to ToC ⇑*](#toc)

User to create to run the exporter.

- **Type**: `str`
- **Required**: No
- **Default**: `"pgbackrest-exp"`



### `pgbackrest_exporter_group`<a id="variable-pgbackrest_exporter_group"></a>

[*⇑ Back to ToC ⇑*](#toc)

Group to create for the user to run the exporter.

- **Type**: `str`
- **Required**: No
- **Default**: `"{{ pgbackrest_exporter_user }}"`



### `pgbackrest_exporter_config_file`<a id="variable-pgbackrest_exporter_config_file"></a>

[*⇑ Back to ToC ⇑*](#toc)

Path to the configuration file of pgBackRest.

- **Type**: `path`
- **Required**: No
- **Default**: `"/etc/pgbackrest/pgbackrest.conf"`



### `pgbackrest_exporter_port`<a id="variable-pgbackrest_exporter_port"></a>

[*⇑ Back to ToC ⇑*](#toc)

Port to listen for the exporter.

- **Type**: `int`
- **Required**: No
- **Default**: `9854`



### `pgbackrest_exporter_telemetry_path`<a id="variable-pgbackrest_exporter_telemetry_path"></a>

[*⇑ Back to ToC ⇑*](#toc)

Route to scrap metrics on the exporter.

- **Type**: `str`
- **Required**: No
- **Default**: `"/metrics"`




<!-- ANSIBLE DOCSMITH MAIN END -->

## Example

```yaml
- hosts: all
  roles:
    - hachyderm.general.pgbackrest_exporter
```

## Local Testing

The preferred way of locally testing the role is to use
(Podman,https://podman.io/) and
L(molecule,https://docs.ansible.com/projects/molecule/).

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
