#!/usr/bin/env python3
#
# Extract ID's from available contents in PHP format.
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


def parse(md_file, base_path):
    html_path = '%s.html' % md_file[len(base_path) + 1:-3]

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
        parse_line(line, html_path)


def parse_line(line, html_path):
    # print line
    match = re.search('^#{1,3}\s+(.*)\s*\{#([\w]*)\}\s*$', line)
    if match:
        # title = match.group(1)
        key = match.group(2)
        print('\'%s\' => \'%s\',' % (key, html_path))


def main(base_path):
    # print('Searching for markdown files in \'%s\'...' % contentDir)
    print('<?php')
    print('return array(')

    md_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    md_files.sort()
    for md_file in md_files:
        parse(md_file, base_path)

    print(');')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No directory was specified as parameter!')
        sys.exit(1)

    main(os.path.abspath(sys.argv[1]))
