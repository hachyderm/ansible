# Ansible Role: PgBouncer

An Ansible role for installing and configuring
[PgBouncer](https://www.pgbouncer.org/), a lightweight connection pooler for
PostgreSQL.

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)
* `pgdg_repository` role

## Role Variables

See [VARIABLES](VARIABLES.md).

## Example

```yaml
- hosts: all
  become: true
  roles:
    - hachyderm.general.pgbouncer
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
