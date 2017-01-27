#!/usr/bin/env python
import re
import os

def check_ro():
    FILE_MOUNTS = 'mounts.txt'
    XFILE = 'djfwegsk34523TEST'
    has_error = False

    with open(FILE_MOUNTS, 'r') as file:
        data = file.read()

    paths = re.findall(r'[ ]\/[\w\/-]*\s', data)

    for idx, path in enumerate(paths):
        path = path.strip()
        if path[len(path) - 1] != '/':
            path = path + '/'
        paths[idx] = path

    for path in paths:
        path_to_file = os.path.join(path, XFILE)
        try:
            open(path_to_file, 'a').close()
        except IOError as error:
            has_error = True
            print(error)
        else:
            os.remove(path_to_file)
    if not has_error:
        print('ok')

if __name__ == '__main__':
    check_ro()
