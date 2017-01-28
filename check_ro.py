#!/usr/bin/env python

import re
import os
import argparse
import random
import string
import errno


def get_random_name(length=8):
    alphabet = string.ascii_letters + string.digits
    result = ''

    for _ in range(length):
        result += random.choice(alphabet)

    return result


def check(filename):
    has_error = False

    with open(filename) as opened:
        file_systems = re.findall(r'[ ]\/[\w\/-]*\s', opened.read())

    file_systems = [fs.strip() for fs in file_systems]

    for fs in file_systems:
        path_to_file = os.path.join(fs, get_random_name())

        try:
            open(path_to_file, 'a').close()
        except IOError as err:
            has_error = True

            if err.errno == errno.EROFS:
                print('{0} is read-only file system'.format(fs))
            else:
                print('Unexpected error: {0}'.format(err))
        else:
            os.remove(path_to_file)

    if not has_error:
        print('ok')


def main():
    parser = argparse.ArgumentParser(
        description='Check whether the mounted partition readable or writable'
    )
    parser.add_argument('-f', '--file',
        help='File with mounted partitions to check. If not specified, ' \
            '/proc/mounts will be used'
    )

    args = parser.parse_args()

    if args.file:
        check(args.file)
    else:
        check('/proc/mounts')


if __name__ == '__main__':
    main()
