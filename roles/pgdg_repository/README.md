# Ansible Role: PGDG repository

An Ansible role for configuring [PGDG Apt
repository](https://wiki.postgresql.org/wiki/Apt).

## Requirements

* Ansible 2.18+
* Python 3
* Debian 12 (bookworm)

## Table of Content
<!-- ANSIBLE DOCSMITH TOC START -->
* [Role variables](#variables)
<!-- ANSIBLE DOCSMITH TOC END -->
<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

No variables are defined for this role.

<!-- ANSIBLE DOCSMITH MAIN END -->

## Example

```yaml
- hosts: all
  become: true
  roles:
    - hachyderm.general.pgdg_repository
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
