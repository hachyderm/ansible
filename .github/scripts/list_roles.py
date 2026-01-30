#!/usr/bin/env python

import json
import glob

if __name__ == "__main__":
    roles = list(set([d.split("/")[1] for d in glob.glob("roles/*/molecule")]))
    print(json.dumps(roles))
