#!/usr/bin/env bash
#
# Create book in English language.
#
# Copyright 2009-2018 OpenEstate.org.
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

LANG="en"
VERSION="1.0-SNAPSHOT"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

set -e
rm -f "$DIR/$LANG.md"
rm -Rf "$DIR/book/$LANG"
mkdir "$DIR/book/$LANG"

cd "$DIR/content/$LANG"

echo "Merging files into $DIR/book/$LANG.md…"
"$DIR/apps/markdown-pp.sh" "$DIR/book/$LANG.mdpp" "$DIR/book/$LANG.md"
sed -i -e "s/\${date}/$(date "+%m\/%d\/%Y")/g" "$DIR/book/$LANG.md"
sed -i -e "s/\${version}/$VERSION/g" "$DIR/book/$LANG.md"

echo "Creating $DIR/book/$LANG/book.epub…"
pandoc -o "$DIR/book/$LANG/book.epub" --epub-embed-font "$DIR/share/*.ttf" --css "$DIR/share/epub.css" "$DIR/book/$LANG.md"

echo "Creating $DIR/book/$LANG/book.pdf…"
pandoc -o "$DIR/book/$LANG/book.pdf" "$DIR/book/$LANG.md"
#pandoc -o "$DIR/book/$LANG/book.pdf" --pdf-engine=xelatex -V CJKmainfont="DejaVu Sans" "$DIR/book/$LANG.md"
#pandoc -o "$DIR/book/$LANG/book.pdf" --pdf-engine=xelatex -V mainfont="DejaVu Serif" "$DIR/book/$LANG.md"

echo "Creating $DIR/book/$LANG/book.odt…"
pandoc -o "$DIR/book/$LANG/book.odt" "$DIR/book/$LANG.md"

echo "Creating $DIR/book/$LANG/book.docx…"
pandoc -o "$DIR/book/$LANG/book.docx" "$DIR/book/$LANG.md"

echo "Creating $DIR/book/$LANG/book.html…"
pandoc --self-contained -o "$DIR/book/$LANG/book.html" "$DIR/book/$LANG.md"
