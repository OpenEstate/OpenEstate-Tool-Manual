#!/usr/bin/env bash
#
# Create the English book in different target formats via Pandoc.
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

NAME="OpenEstate-ImmoTool-Manual"
LANG="en"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

set -e
rm -f "$DIR/$LANG.md"
rm -Rf "$DIR/book/$LANG"
mkdir "$DIR/book/$LANG"

cd "$DIR/content/$LANG"

echo "Merging Markdown files…"
"$DIR/apps/markdown-pp.sh" "$DIR/book/$LANG.mdpp" "$DIR/book/$LANG.md"
sed -i -e "s/\${date}/$(date "+%d.%m.%Y")/g" "$DIR/book/$LANG.md"
#sed -i -e "s/\${version}/$VERSION/g" "$DIR/book/$LANG.md"

echo "Creating $NAME.$LANG.epub…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.epub" \
  --epub-embed-font "$DIR/share/fonts/*.ttf" \
  --css "$DIR/share/epub.css" \
  "$DIR/book/$LANG.md"

echo "Creating $NAME.$LANG.pdf…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.pdf" \
  "$DIR/book/$LANG.md"

echo "Creating $NAME.$LANG.odt…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.odt" \
  "$DIR/book/$LANG.md"

echo "Creating $NAME.$LANG.docx…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.docx" \
  "$DIR/book/$LANG.md"

echo "Creating $NAME.$LANG.html…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.html" \
  --self-contained \
  "$DIR/book/$LANG.md"
