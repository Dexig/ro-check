#!/usr/bin/env python
import re
import os

FILE_MOUNTS = 'mounts.txt'
XFILE = 'djfwegsk34523TEST'

with open(FILE_MOUNTS, 'r') as file:
    DATA = file.read()

PATHS = re.findall(r'[ ]\/[\w\/-]*\s', DATA)

for idx, path in enumerate(PATHS):
    path = path.strip()
    if path[len(path) - 1] != '/':
        path = path + '/'
    PATHS[idx] = path

for path in PATHS:
    path_to_file = os.path.join(path, XFILE)
    try:
        open(path_to_file, 'a').close()
    except IOError as error:
        print(error)
    else:
        os.remove(path_to_file)
