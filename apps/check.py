#!/usr/bin/env python3
#
# Check contents for validity.
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


# Check headlines in markdown files.
def check_headlines(markdown_files):
    counter = 0
    for markdown_file in markdown_files:
        counter = counter + check_headlines_file(markdown_file)

    return counter


# Check headlines in a markdown file.
def check_headlines_file(markdown_file):
    with open(markdown_file, 'r') as md:
        data = md.read()

    counter = 0
    line_nr = 0
    error_found = False
    in_code_block = False
    for line in data.split('\n'):
        line_nr = line_nr + 1
        if line.startswith('```'):
            if in_code_block:
                in_code_block = False
            else:
                in_code_block = True

        if not line.startswith('#') or in_code_block:
            continue

        match = re.search('^#+\s+(.*)\s*\{#([\w]*)\}\s*$', line)
        if match:
            continue

        if not error_found:
            error_found = True
            print()
            cprint_green('-' * 70, True)
            cprint_green(' Invalid headlines in %s' % markdown_file, True)
            cprint_green('-' * 70, True)

        print()
        cprint_green('at line %s:' % line_nr)
        print(line)
        counter = counter + 1

    return counter


# Check images in markdown files.
def check_images(markdown_files):
    counter = 0
    for markdown_file in markdown_files:
        counter = counter + check_images_file(markdown_file)

    return counter


# Check images in a markdown file.
def check_images_file(markdown_file):
    with open(markdown_file, 'r') as md:
        data = md.read()

    counter = 0
    line_nr = 0
    error_found = False
    in_code_block = False
    figure_pattern = re.compile(r'{{<\s+figure\s+([^>]*)\s+>}}')
    figure_pattern_src = re.compile(r'src\s*=\s*\"([^\"]*)\"')
    for line in data.split('\n'):
        line_nr = line_nr + 1
        if line.startswith('```'):
            if in_code_block:
                in_code_block = False
            else:
                in_code_block = True

        if in_code_block:
            continue

        errors = []
        for figure in figure_pattern.finditer(line):
            group = figure.group(0)
            try:
                image = next(figure_pattern_src.finditer(group)).group(1)
            except StopIteration:
                errors.append([group, 'missing src attribute'])
                continue

            if image is None or image.strip() == '':
                errors.append([group, 'empty src attribute'])
                continue

            image_path = os.path.normpath(os.path.join(os.path.dirname(markdown_file), image))
            if not os.path.isfile(image_path):
                errors.append([group, 'image "%s" not found' % os.path.basename(image_path)])

        # show errors for the current line
        if len(errors) > 0:
            if not error_found:
                error_found = True
                print()
                cprint_green('-' * 70, True)
                cprint_green(' Invalid images in %s' % markdown_file, True)
                cprint_green('-' * 70, True)

            for error in errors:
                print()
                cprint_green('at line %s (%s):' % (line_nr, error[1]))
                print(error[0])
                counter = counter + 1

    return counter


# Check links in markdown files.
def check_links(markdown_files):
    counter = 0
    for markdown_file in markdown_files:
        counter = counter + check_links_file(markdown_file)

    return counter


# Check links in a markdown file.
def check_links_file(markdown_file):
    with open(markdown_file, 'r') as md:
        data = md.read()

    counter = 0
    line_nr = 0
    error_found = False
    in_code_block = False
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
    for line in data.split('\n'):
        line_nr = line_nr + 1
        if line.startswith('```'):
            if in_code_block:
                in_code_block = False
            else:
                in_code_block = True

        if in_code_block:
            continue

        errors = []
        for link in link_pattern.finditer(line):
            # print(link.group(0))
            # print(link.group(1))
            group = link.group(0)
            target = link.group(1)

            # don't validate external links
            if target.startswith('http://') or target.startswith('https://'):
                continue

            # validate internal links on the same document
            elif target.startswith('#'):
                lookup = '{%s}' % target
                if lookup not in data:
                    errors.append([group, 'headline "%s" not found' % target])

            # validate references
            elif target.startswith('{'):
                if not target.startswith('{{< relref "') or not target.endswith('" >}}'):
                    errors.append([group, 'invalid syntax'])
                else:
                    reference = target[12:-5]
                    reference_error = check_links_reference(reference, markdown_file)
                    if reference_error is not None:
                        errors.append([group, reference_error])

            # unsupported links
            else:
                errors.append([group, 'unsupported link'])

        # show errors for the current line
        if len(errors) > 0:
            if not error_found:
                error_found = True
                print()
                cprint_green('-' * 70, True)
                cprint_green(' Invalid links in %s' % markdown_file, True)
                cprint_green('-' * 70, True)

            for error in errors:
                print()
                cprint_green('at line %s (%s):' % (line_nr, error[1]))
                print(error[0])
                counter = counter + 1

    return counter


# Check internal reference link.
def check_links_reference(reference, src_file):
    # The reference should point to a headline.
    if '#' not in reference:
        return 'headline not specified'

    # The target file should exist.
    ref = reference.split('#', 2)
    target_file = os.path.normpath(os.path.join(os.path.dirname(src_file), ref[0]))
    # print(target_file)
    if not os.path.isfile(target_file):
        return 'file not found'

    # The target file should contain the referenced headline.
    with open(target_file, 'r') as md:
        data = md.read()
    lookup = '{#%s}' % ref[1]
    if lookup not in data:
        return 'headline "#%s" not found in %s' % (ref[1], os.path.basename(ref[0]))

    return None


# Start application.
def main(path):
    # fetch available markdown files
    markdown_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.md'):
                continue
            markdown_files.append(os.path.join(root, file))

    markdown_files.sort()

    # Check headlines in markdown files.
    count_headline_errors = check_headlines(markdown_files)

    # Check images in markdown files.
    count_image_errors = check_images(markdown_files)

    # Check links in markdown files.
    count_link_errors = check_links(markdown_files)

    # Print summary.
    count_total_errors = count_headline_errors + count_image_errors + count_link_errors
    print('')
    cprint_white('=' * 70, True)
    cprint_white(' Found %s errors in headlines.' % count_headline_errors, True)
    cprint_white(' Found %s errors in images.' % count_image_errors, True)
    cprint_white(' Found %s errors in links.' % count_link_errors, True)
    cprint_white(' Found %s errors in total.' % count_total_errors, True)
    cprint_white('=' * 70, True)
    print('')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No directory was specified as parameter!')
        sys.exit(1)

    main(sys.argv[1])
