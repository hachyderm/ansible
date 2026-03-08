# Contributing

We follow the [Hachyderm Code of
Conduct](https://community.hachyderm.io/docs/rule-explainer/) in all our
contributions and interactions within this repository.

If you encounter a bug using the collection, you should first check the [opened
issues](https://github.com/hachyderm/ansible/issues) to see if somebody else
has reported the same bug before creating a fix. This could save a lot of time
and effort. If not, feel free to open an issue to describe your bug. It's even
better if you can open a pull request with a patch.

If you want to contribute but don't know where to start, you should check the
issues with the [good first
issue](https://github.com/hachyderm/ansible/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)
label.

You can also look the [pull
requests](https://github.com/hachyderm/ansible/pulls) and help by reviewing
them.

# Creating new roles, plugins or modules

We will not accept new roles, plugins or modules unless they are used and
maintained by the Hachyderm infrastructure team. Feel free to open an issue to
suggest new roles, plugins or modules to replace existing ones that are
obsolete.

This collection supports only the Debian operating system because the Hachyderm
infrastructure runs on Debian only.

# Open pull requests

Pull requests to improve existing roles, plugins or modules are welcome.

Please read the [Contributing to
collections](https://docs.ansible.com/projects/ansible/devel/dev_guide/developing_collections_contributing.html#contributing-to-collections)
guide.

Lint your code with `ansible-lint`.

If needed, update the `argument_specs.yml` file and run `ansible-docsmith
generate path/to/role` command to update the README.md file. The expected
format is reStructuredText (RST) to generate the
[website](https://hachyderm.github.io/ansible/branch/main/).

Make sure to add `molecule` tests.
