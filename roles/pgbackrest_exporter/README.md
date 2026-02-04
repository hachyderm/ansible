# Ansible Role: pgBackRest Exporter

An Ansible role for installing and configuring [pgBackRest
Exporter](https://github.com/woblerr/pgbackrest_exporter).

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)
* pgBackRest binary and configuration file

## Role Variables

See [VARIABLES](VARIABLES.md).

## Example

```yaml
- hosts: all
  roles:
    - hachyderm.general.pgbackrest_exporter
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
