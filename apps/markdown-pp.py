#
# Launch customized markdown preprocessor.
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
import tempfile
from MarkdownPP.Module import Module
from MarkdownPP.Modules.Include import Include
from MarkdownPP.Processor import Processor
from MarkdownPP.Transform import Transform


class CustomInclude(Include):
    mode = None
    lang = None

    # Pattern to extract internal links (relref shortcode).
    # example: {{< relref "settings.md#usage_general_settings_updates" >}}
    pattern_relref = re.compile(r'{{<\s+relref\s+\"([^\"]*)\"\s+>}}')

    # Pattern to extract images (figure shortcode).
    # example: {{< figure src="java_check_terminal-01.jpg" caption="Ausgabe der Java-Version" >}}
    pattern_figure = re.compile(r'{{<\s+figure\s+([^>]*)\s+>}}')
    pattern_figure_src = re.compile(r'src\s*=\s*\"([^\"]*)\"')
    pattern_figure_caption = re.compile(r'caption\s*=\s*\"([^\"]*)\"')
    pattern_figure_width = re.compile(r'width\s*=\s*\"([^\"]*)\"')
    pattern_figure_height = re.compile(r'height\s*=\s*\"([^\"]*)\"')

    # Pattern to extract info messages (info shortcode).
    # example: {{< info >}}My message.{{< /info >}}
    pattern_info = re.compile(r'{{<\s+info\s+>}}(.*?){{<\s+/info\s+>}}', re.MULTILINE | re.DOTALL)

    # Pattern to extract warning messages (warning shortcode).
    # example: {{< warning >}}My message.{{< /warning >}}
    pattern_warning = re.compile(r'{{<\s+warning\s+>}}(.*?){{<\s+/warning\s+>}}', re.MULTILINE | re.DOTALL)

    # Pattern to extract open tasks (todo shortcode).
    # example: {{< todo >}}My message.{{< /todo >}}
    pattern_todo = re.compile(r'{{<\s+todo\s+>}}(.*?){{<\s+/todo\s+>}}', re.MULTILINE | re.DOTALL)

    def __init__(self, mode, lang):
        self.mode = mode
        self.lang = lang

    def include_file(self, filename, pwd="", shift=0):
        # print('INCLUDE FILE %s at %s' % (filename, pwd,))
        fileDir = os.path.dirname(os.path.join(os.getcwd(), filename))
        tempPath = tempfile.mktemp()
        try:
            # Extract file contents below the YAML header.
            data = ''
            with open(filename, 'r') as mdFile:
                state = 0
                for line in mdFile.readlines():
                    if state < 2:
                        if line.strip() == '---':
                            state = state + 1
                    else:
                        data += line

            # Replace Hugo shortcodes to make it work with pandoc.
            data = self.replace_info(data)
            data = self.replace_warning(data)
            data = self.replace_todo(data)
            data = self.replace_relref(data, filename)
            data = self.replace_figure(data, filename, fileDir)

            # Write data into a temporary file.
            with open(tempPath, 'w') as tempFile:
                tempFile.write(data)

            # Include temporary file.
            return Include.include_file(self, tempPath, pwd, shift)

        finally:
            if os.path.isfile(tempPath):
                os.remove(tempPath)

    # Replace info shortcodes.
    def replace_info(self, data):
        if self.lang == 'de':
            title = 'Hinweis'
        else:
            title = 'Notice'

        for info in self.pattern_info.finditer(data):
            body = info.group(1).strip()
            if mode == 'pdf':
                content = '::: info :::\n%s\n::::::::::::' % body
            else:
                content = '> **%s**\n>' % title
                for i in body.splitlines():
                    content = content + '\n%s' % i
            data = data.replace(info.group(0), content)

        return data

    # Replace warning shortcodes.
    def replace_warning(self, data):
        if self.lang == 'de':
            title = 'Achtung'
        else:
            title = 'Warning'

        for warning in self.pattern_warning.finditer(data):
            body = warning.group(1).strip()
            if mode == 'pdf':
                content = '::: warning :::\n%s\n:::::::::::::::' % body
            else:
                content = '> **%s**\n>' % title
                for i in body.splitlines():
                    content = content + '\n%s' % i
            data = data.replace(warning.group(0), content)

        return data

    # Replace todo shortcodes.
    def replace_todo(self, data):
        if self.lang == 'de':
            title = 'Zu erledigen'
        else:
            title = 'To-Do'

        for todo in self.pattern_todo.finditer(data):
            body = todo.group(1).strip()
            if mode == 'pdf':
                content = '::: todo :::\n%s\n::::::::::::' % body
            else:
                content = '> **%s**\n>' % title
                for i in body.splitlines():
                    content = content + '\n%s' % i
            data = data.replace(todo.group(0), content)

        return data

    # Replace relref shortcodes.
    def replace_relref(self, data, fileName):
        for relref in self.pattern_relref.finditer(data):
            link = relref.group(1).split('#', 2)
            if not len(link) == 2:
                print('WARNING: Invalid relref link "%s" in %s' % (relref.group(1), fileName,))
                continue
            data = data.replace(relref.group(0), '#%s' % link[1])

        return data

    # Replace figure shortcodes.
    def replace_figure(self, data, fileName, fileDir):
        for figure in self.pattern_figure.finditer(data):
            try:
                figure_src = next(self.pattern_figure_src.finditer(figure.group(0))).group(1)
            except StopIteration:
                print('WARNING: Figure "%s" without src attribute in %s' % (figure.group(0), fileName,))
                continue

            try:
                figure_caption = next(self.pattern_figure_caption.finditer(figure.group(0))).group(1)
            except StopIteration:
                figure_caption = ''

            try:
                figure_width = next(self.pattern_figure_width.finditer(figure.group(0))).group(
                    1)
            except StopIteration:
                figure_width = False

            try:
                figure_height = next(self.pattern_figure_height.finditer(figure.group(0))).group(
                    1)
            except StopIteration:
                figure_height = False

            figure_attribs = []
            if self.mode == 'pdf':
                if figure_width:
                    figure_attribs.append('width=%s' % figure_width)
                if figure_height:
                    figure_attribs.append('height=%s' % figure_height)

            figure_src_absolute = os.path.join(fileDir, figure_src)
            replacement = '![%s](%s){%s}' % (
                figure_caption,
                figure_src_absolute,
                ' '.join(figure_attribs),
            )
            replacement = '%s' % replacement
            data = data.replace(figure.group(0), replacement)

        return data


if __name__ == '__main__':
    if len(sys.argv) > 2:
        mdpp = open(sys.argv[1], "r")
        md = open(sys.argv[2], "w")

    elif len(sys.argv) > 1:
        mdpp = open(sys.argv[1], "r")
        md = sys.stdout

    else:
        sys.exit(1)

    if len(sys.argv) > 3:
        mode = sys.argv[3]
    else:
        mode = None

    if len(sys.argv) > 4:
        lang = sys.argv[4]
    else:
        lang = None

    try:
        pp = Processor()
        pp.register(CustomInclude(mode, lang))
        # pp.register(Include())
        # pp.register(BookLinks())
        pp.input(mdpp)
        pp.process()
        pp.output(md)
    finally:
        mdpp.close()
        md.close()
