#!/usr/bin/env python3
#
# Extract to-do entries from markdown files.
#
# Copyright 2009-2019 OpenEstate.org.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import re
import sys

pattern_todo = re.compile(r'{{<\s+todo\s+>}}(.*?){{<\s+/todo\s+>}}', re.MULTILINE | re.DOTALL)


# noinspection SpellCheckingInspection
def cprint(msg, color=None, bold=False):
    output = msg
    if color is not None:
        output = color + output
    if bold:
        output = '\033[1m' + output
    if color is not None or bold:
        output += '\033[0m'
    print(output)


# noinspection SpellCheckingInspection
def cprint_blue(msg, bold=False):
    cprint(msg, '\033[94m', bold)


# noinspection SpellCheckingInspection
def cprint_green(msg, bold=False):
    cprint(msg, '\033[92m', bold)


# noinspection SpellCheckingInspection
def cprint_red(msg, bold=False):
    cprint(msg, '\033[91m', bold)


# noinspection SpellCheckingInspection
def cprint_yellow(msg, bold=False):
    cprint(msg, '\033[93m', bold)


# noinspection SpellCheckingInspection
def cprint_white(msg, bold=False):
    cprint(msg, '\033[97m', bold)


def parse(path):
    if not os.path.exists(path):
        print('ERROR: The provided path %s does not exist!' % path)
        return -1
    elif os.path.isfile(path):
        return parse_file(path)
    elif os.path.isdir(path):
        count = 0
        md_files = []
        for root, dirs, files in os.walk(path):
            for f in files:
                md_files.append(os.path.join(root, f))
        for md_file in sorted(md_files):
            count = count + parse_file(md_file)
        return count
    else:
        print('ERROR: The provided path %s is invalid!' % path)
        return -1


def parse_file(path):
    if not path.endswith('.md'):
        return 0

    with open(path, 'r') as f:
        data = f.read()

    lengths = []
    for line in data.splitlines(True):
        lengths.append(len(line))

    count = 0
    for todo in pattern_todo.finditer(data):
        if count == 0:
            print('')
            cprint_green('-' * 70, True)
            cprint_green(' todo entries in %s' % path, True)
            cprint_green('-' * 70, True)

        body = todo.group(1).strip()
        print('')
        cprint_green('at line %s:' % get_line_number(todo.start(), lengths))
        print(body.strip())
        count = count + 1

    return count


def get_line_number(pos, lengths):
    i = 0
    line = 0
    while i < pos and line < len(lengths):
        i = i + lengths[line]
        line = line + 1

    return line + 1


def main(path):
    total_count = parse(path)
    if total_count < 0:
        exit(2)
    else:
        print('')
        cprint_white('=' * 70, True)
        cprint_white(' Found %s todo entries in total.' % total_count, True)
        cprint_white('=' * 70, True)
        print('')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('ERROR: No file or directory was specified as first argument!')
        exit(1)

    main(sys.argv[1])
