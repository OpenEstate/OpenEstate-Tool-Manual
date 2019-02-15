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

BOOK_NAME="OpenEstate-ImmoTool-Manual"
BOOK_LANG="de"
DATE_FORMAT="+%d.%m.%Y"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

set -e
rm -f "$DIR/$BOOK_LANG.md"
rm -Rf "$DIR/book/$BOOK_LANG"
mkdir "$DIR/book/$BOOK_LANG"

cd "$DIR/content/$BOOK_LANG"

echo "Merging Markdown files…"

PDF_MD="$DIR/book/$BOOK_LANG.pdf.md"
"$DIR/apps/markdown-pp.sh" "$DIR/book/$BOOK_LANG.mdpp" "$PDF_MD" "pdf" "$BOOK_LANG"
sed -i -e "s/\${date}/$(date "$DATE_FORMAT")/g" "$PDF_MD"

OTHER_MD="$DIR/book/$BOOK_LANG.other.md"
"$DIR/apps/markdown-pp.sh" "$DIR/book/$BOOK_LANG.mdpp" "$OTHER_MD" "other" "$BOOK_LANG"
sed -i -e "s/\${date}/$(date "$DATE_FORMAT")/g" "$OTHER_MD"

echo "Creating $BOOK_NAME.$BOOK_LANG.pdf…"
pandoc \
    -F "$DIR/apps/pandoc-latex-admonition.sh" \
    -F "$DIR/apps/pandoc-latex-tip.sh" \
    -o "$DIR/book/$BOOK_LANG/$BOOK_NAME.$BOOK_LANG.pdf" \
    "$PDF_MD"

echo "Creating $BOOK_NAME.$BOOK_LANG.epub…"
pandoc -o "$DIR/book/$BOOK_LANG/$BOOK_NAME.$BOOK_LANG.epub" \
    --epub-embed-font "$DIR/share/fonts/*.ttf" \
    --css "$DIR/share/epub.css" \
    "$OTHER_MD"

echo "Creating $BOOK_NAME.$BOOK_LANG.odt…"
pandoc -o "$DIR/book/$BOOK_LANG/$BOOK_NAME.$BOOK_LANG.odt" \
    "$OTHER_MD"

echo "Creating $BOOK_NAME.$BOOK_LANG.docx…"
pandoc -o "$DIR/book/$BOOK_LANG/$BOOK_NAME.$BOOK_LANG.docx" \
    "$OTHER_MD"

echo "Creating $BOOK_NAME.$BOOK_LANG.html…"
pandoc -o "$DIR/book/$BOOK_LANG/$BOOK_NAME.$BOOK_LANG.html" \
    --self-contained \
    "$OTHER_MD"
