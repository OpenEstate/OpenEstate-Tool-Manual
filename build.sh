#!/usr/bin/env bash
#
# Create the website with Hugo.
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

OPTIONS="--gc --minify"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PUBLIC_DIR="$DIR/public"

echo ""
echo "----------------------------------------"
echo " Erzeugung der Webseite."
echo "----------------------------------------"

rm -Rf "$PUBLIC_DIR"
cd "$DIR"
"$DIR/apps/hugo.sh" ${OPTIONS}

echo ""
echo "----------------------------------------"
echo " Die Webseite wurde erzeugt."
echo ""
echo " Im Verzeichnis:"
echo " $PUBLIC_DIR"
echo "----------------------------------------"
echo ""
