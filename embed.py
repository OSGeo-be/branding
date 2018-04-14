#!/usr/bin/env python
import base64
import re
import sys

in_filename = sys.argv[1]
out_filename = sys.argv[2]
with open(in_filename, 'r') as f:
    base_file = f.read()
for match in re.findall("{{[^}]*}}", base_file):
    sub_filename = match[2:-2]
    print("embedding {} in {}".format(sub_filename, out_filename))
    with open(sub_filename, 'rb') as sub:
        b64str = base64.b64encode(sub.read()).decode()
    base_file = base_file.replace(match, b64str)
    
with open(out_filename, 'w') as f:
    f.write(base_file)
