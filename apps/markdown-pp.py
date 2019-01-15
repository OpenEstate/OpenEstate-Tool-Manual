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
    # Pattern to extract internal links (relref shortcode).
    # example: {{< relref "settings.md#usage_general_settings_updates" >}}
    pattern_relref = re.compile("{{<\s+relref\s+\"([^\"]*)\"\s+>}}")

    # Pattern to extract images (figure shortcode).
    # example: {{< figure src="java_check_terminal-01.jpg" caption="Ausgabe der Java-Version" >}}
    pattern_figure = re.compile("{{<\s+([^>]*)\s+>}}")
    pattern_figure_src = re.compile("src\s*=\s*\"([^\"]*)\"")
    pattern_figure_caption = re.compile("caption\s*=\s*\"([^\"]*)\"")

    def include_file(self, filename, pwd="", shift=0):

        # print 'INCLUDE FILE %s at %s' % (filename, pwd,)
        # return super(CustomInclude).include_file(filename, pwd, shift)

        fileDir = os.path.dirname(os.path.join(os.getcwd(), filename))
        # print fileDir

        tempPath = tempfile.mktemp()
        try:

            with open(tempPath, 'w') as tempFile:
                with open(filename, 'r') as mdFile:
                    state = 0
                    for line in mdFile:

                        # Ignore any lines until the YAML header of the file was passed.
                        if state < 2:
                            if line.strip() == '---': state = state + 1
                            continue

                        # Replace any relref shortcodes.
                        relrefs = self.pattern_relref.finditer(line)
                        for relref in relrefs:
                            # print(relref.group(0))
                            # print(relref.group(1))
                            link = relref.group(1).split('#', 2)
                            if not len(link) == 2:
                                print 'WARNING: Invalid relref link "%s" in %s' % (relref.group(1), filename,)
                                continue
                            line = line.replace(relref.group(0), '#%s' % link[1])

                        # Replace any figure shortcodes.
                        figures = self.pattern_figure.finditer(line)
                        for figure in figures:
                            # print(figure.group(0))
                            # print(figure.group(1))

                            # args = figure_parser.parse_args(figure.group(1).replace('=', ' ').split(' '))
                            # print(args)

                            # figure_src = self.pattern_figure_src.finditer(figure.group(1)).next().group(1)
                            try:
                                figure_src = self.pattern_figure_src.finditer(figure.group(0)).next().group(1)
                            except StopIteration:
                                print 'WARNING: Figure "%s" without src attribute in %s' % (figure.group(0), filename,)
                                continue

                            try:
                                figure_caption = self.pattern_figure_caption.finditer(figure.group(0)).next().group(1)
                            except StopIteration:
                                figure_caption = ''

                            # print('%s / %s' % (figure_src, figure_caption))

                            figure_src_absolute = os.path.join(fileDir, figure_src)
                            line = line.replace(figure.group(0), '![%s](%s)' % (figure_caption, figure_src_absolute,))

                        tempFile.write(line)
                        # tempFile.write('\n')

            return Include.include_file(self, tempPath, pwd, shift)

        finally:
            if os.path.isfile(tempPath):
                os.remove(tempPath)


"""
class BookLinks(Module):

  linkre = re.compile("\[([^\]]*)\]\([\w]*\.md#(\w*)\)")

  def transform(self, data):
    transforms = []

    linenum = 0
    for line in data:

      new_line = line
      results = self.linkre.finditer(line)
      for result in results:
        old_link = result.group(0)
        new_link = '[%s](#%s)' % (result.group(1), result.group(2),)
        #print 'REPLACE LINK'
        #print '> old: %s' % old_link
        #print '> new: %s' % new_link
        new_line = new_line.replace(old_link, new_link, 1)

      if not line == new_line:
        print 'LINE : %s' % line
        print 'CONV : %s' % line
        transform = Transform(linenum=linenum, oper="swap", data=new_line)
        transforms.append(transform)

      linenum += 1

    return transforms
"""

if len(sys.argv) > 2:
    mdpp = open(sys.argv[1], "r")
    md = open(sys.argv[2], "w")

elif len(sys.argv) > 1:
    mdpp = open(sys.argv[1], "r")
    md = sys.stdout

else:
    sys.exit(1)

try:
    pp = Processor()
    pp.register(CustomInclude())
    # pp.register(Include())
    # pp.register(BookLinks())
    pp.input(mdpp)
    pp.process()
    pp.output(md)
finally:
    mdpp.close()
    md.close()
