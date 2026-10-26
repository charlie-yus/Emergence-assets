#!/usr/bin/env python3
"""Copy an anonymous thesis starter into a new, nonexistent directory."""
import argparse,pathlib,shutil
p=argparse.ArgumentParser(description=__doc__);p.add_argument('destination',type=pathlib.Path);a=p.parse_args()
target=a.destination.expanduser().resolve()
if target.exists():p.error('Destination exists; refusing to overwrite any existing project')
root=pathlib.Path(__file__).resolve().parents[1]
shutil.copytree(root/'assets/template',target)
shutil.copy2(root/'scripts/build.py',target/'build.py')
print(target)
