#!/usr/bin/env bash
#
# Create book in German language.
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

set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

rm -Rf "$DIR/book/de"
mkdir "$DIR/book/de"

cd "$DIR/content/de"

echo "Merging files into $DIR/book/de/book.md…"
"$DIR/apps/markdown-pp.sh" "$DIR/book/de.mdpp" "$DIR/book/de/book.md"

echo "Creating $DIR/book/de/book.epub…"
pandoc -o "$DIR/book/de/book.epub" "$DIR/book/de/book.md"

echo "Creating $DIR/book/de/book.pdf…"
pandoc -o "$DIR/book/de/book.pdf" "$DIR/book/de/book.md"
#pandoc -o "$DIR/book/de/book.pdf" --pdf-engine=xelatex -V CJKmainfont="DejaVu Sans" "$DIR/book/de/book.md"
#pandoc -o "$DIR/book/de/book.pdf" --pdf-engine=xelatex -V mainfont="DejaVu Serif" "$DIR/book/de/book.md"

echo "Creating $DIR/book/de/book.odt…"
pandoc -o "$DIR/book/de/book.odt" "$DIR/book/de/book.md"

echo "Creating $DIR/book/de/book.docx…"
pandoc -o "$DIR/book/de/book.docx" "$DIR/book/de/book.md"

echo "Creating $DIR/book/de/book.html…"
pandoc --self-contained -o "$DIR/book/de/book.html" "$DIR/book/de/book.md"
