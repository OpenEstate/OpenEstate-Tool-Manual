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

import os
import re
import sys


def parse(filePath, contentDir):
    title = '//\n// ID\'s from \'%s\'\n//' % filePath[len(contentDir) + 1:]
    with open(filePath, 'r') as myfile:
        data = myfile.read()
        for line in data.split('\n'):
            if parseLine(line, title):
                title = None
    if title is None:
        print()


def parseLine(line, title):
    # print line
    match = re.search('^#{1,3} (.*) \{#([\w]*)\}$', line)
    if match:
        if title:
            print()
            print(title)
            print()

        title = match.group(1)
        key = match.group(2)
        print('/** %s */' % title.strip())
        # print('String %s = "%s";' % (key.upper(), key))
        print('%s,' % key.upper())
        return True
    return False


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No directory was specified as parameter!')
        sys.exit(1)

    contentDir = os.path.abspath(sys.argv[1])
    # print 'Searching for markdown files in \'%s\'...' % contentDir

    paths = []
    for root, dirs, files in os.walk(contentDir):
        path = root.split(os.sep)
        # print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            if not file.endswith('.md'): continue
            paths.append(os.path.join(root, file))

    paths.sort()
    for path in paths:
        parse(path, contentDir)
