#!/usr/bin/env python3
#
# Extract ID's from available contents in Java format.
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

import html
import os
import re
import sys


def parse(md_file, base_path):
    title = '//\n// ID\'s from \'%s\'\n//' % md_file[len(base_path) + 1:]

    # Extract file contents below the YAML header.
    lines = []
    with open(md_file, 'r') as md_content:
        state = 0
        for line in md_content.readlines():
            line_normalized = line.strip().lower()

            # ignore drafts
            if state == 1 and line_normalized.startswith('draft:') and line_normalized.endswith('true'):
                return

            if state < 2:
                if line_normalized == '---':
                    state = state + 1
            else:
                lines.append(line)

    # Process contents.
    for line in lines:
        if parse_line(line, title):
            title = None

    if title is None:
        print()


def parse_line(line, title):
    # print line
    match = re.search('^#{1,3}\s+(.*)\s*\{#([\w]*)\}\s*$', line)
    if match:
        if title:
            print()
            print(title)
            print()

        title = match.group(1)
        key = match.group(2)
        print('/** %s */' % html.escape(title.strip(), False))
        # print('String %s = "%s";' % (key.upper(), key))
        print('%s,' % key.upper())
        return True
    return False


def main(base_path):
    # print('Searching for markdown files in \'%s\'...' % base_path)

    md_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    md_files.sort()
    for md_file in md_files:
        parse(md_file, base_path)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No directory was specified as parameter!')
        sys.exit(1)

    main(os.path.abspath(sys.argv[1]))
