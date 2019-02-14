#!/usr/bin/env bash
#
# Create the German book in different target formats via Pandoc.
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
LANG="de"
DATE_FORMAT="+%d.%m.%Y"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

set -e
rm -f "$DIR/$LANG.md"
rm -Rf "$DIR/book/$LANG"
mkdir "$DIR/book/$LANG"

cd "$DIR/content/$LANG"

echo "Merging Markdown files…"

PDF_MD="$DIR/book/$LANG.pdf.md"
"$DIR/apps/markdown-pp.sh" "$DIR/book/$LANG.mdpp" "$PDF_MD" "pdf" "$LANG"
sed -i -e "s/\${date}/$(date "$DATE_FORMAT")/g" "$PDF_MD"

OTHER_MD="$DIR/book/$LANG.other.md"
"$DIR/apps/markdown-pp.sh" "$DIR/book/$LANG.mdpp" "$OTHER_MD" "other" "$LANG"
sed -i -e "s/\${date}/$(date "$DATE_FORMAT")/g" "$OTHER_MD"

echo "Creating $NAME.$LANG.pdf…"
pandoc \
    -F "$DIR/apps/pandoc-latex-admonition.sh" \
    -F "$DIR/apps/pandoc-latex-tip.sh" \
    -o "$DIR/book/$LANG/$NAME.$LANG.pdf" \
    "$PDF_MD"

echo "Creating $NAME.$LANG.epub…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.epub" \
    --epub-embed-font "$DIR/share/fonts/*.ttf" \
    --css "$DIR/share/epub.css" \
    "$OTHER_MD"

echo "Creating $NAME.$LANG.odt…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.odt" \
    "$OTHER_MD"

echo "Creating $NAME.$LANG.docx…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.docx" \
    "$OTHER_MD"

echo "Creating $NAME.$LANG.html…"
pandoc -o "$DIR/book/$LANG/$NAME.$LANG.html" \
    --self-contained \
    "$OTHER_MD"
