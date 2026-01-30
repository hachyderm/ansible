# Ansible Role: PgBouncer Exporter

An Ansible role for installing and configuring [PgBouncer
Exporter](https://github.com/prometheus-community/pgbouncer_exporter).

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)

## Role Variables

See [VARIABLES](VARIABLES.md).

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
