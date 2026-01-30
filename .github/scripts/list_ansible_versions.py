#!/usr/bin/env python

import yaml
import json
from packaging.version import Version
from packaging.specifiers import SpecifierSet


if __name__ == "__main__":
    with open("meta/runtime.yml", "r") as fd:
        runtime = yaml.safe_load(fd)

    requires_ansible = runtime["requires_ansible"]

    specifier_set = SpecifierSet(requires_ansible)

    min_version, max_version = requires_ansible.split(",")
    min_version = Version(min_version.strip(">="))
    max_version = Version(max_version.strip("<"))

    version = min_version
    versions = []
    while version in specifier_set and version < max_version:
        versions.append(f"{version.release[0]}.{version.release[1]}")
        version = Version(f"{version.release[0]}.{version.release[1] + 1}")

    print(json.dumps(versions))
