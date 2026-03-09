# Ansible Hachyderm General Collection

This repository contains the `hachyderm.general` Ansible Collection.

You can find the documenation for this collection on [this
website](https://hachyderm.github.io/ansible/branch/main).

## Using this collection

Install the collection with Ansible Galaxy:

```
ansible-galaxy collection install hachyderm.general
```

You can also include a `requirements.yml` file and install it via
`ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: hachyderm.general
```

You can upgrade the collection with:

```
ansible-galaxy collection install hachyderm.general --upgrade
```

Or install a specific version with:

```
ansible-galaxy collection install hachyderm.general==X.Y.Z
```

Where `X.Y.Z` is a [published
version](https://galaxy.ansible.com/ui/repo/published/hachyderm/general/).

See [Using Ansible
collections](https://docs.ansible.com/projects/ansible/latest/collections_guide/index.html)
for more details.

## Contributing to this collection

Contributions are welcome.

Please read the [contributing](CONTRIBUTING.md) guide.
