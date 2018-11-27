#!/usr/bin/env bash
#
# Create the website bundle.
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
NAME="$( basename "$DIR" )"

# Anwendungen ggf. herunterladen.
#"$DIR/apps/init.sh"

# Leeres Ausgabeverzeichnis erzeugen.
BUNDLE_DIR="$DIR/bundle"
rm -Rf "$BUNDLE_DIR"
mkdir -p "$BUNDLE_DIR"
cd "$DIR/.."

# ZIP-Archiv erzeugen.
zip -9 -r \
  --exclude=$NAME/.git/\* \
  --exclude=$NAME/.gitattributes \
  --exclude=$NAME/.gitignore \
  --exclude=$NAME/apps/downloads/\* \
  --exclude=$NAME/apps/init.sh \
  --exclude=$NAME/bundle/\* \
  --exclude=$NAME/bundle.sh \
  --exclude=$NAME/public/\* \
  --exclude=$NAME/resources/\* \
  --exclude=$NAME/DOCUMENTATION.md \
  --exclude=$NAME/README.md \
  "$BUNDLE_DIR/$NAME.zip" "$NAME"

# TAR.GZ-Archiv erzeugen.
tar cvfz "$BUNDLE_DIR/$NAME.tar.gz" \
  --exclude=$NAME/.git \
  --exclude=$NAME/.gitattributes \
  --exclude=$NAME/.gitignore \
  --exclude=$NAME/apps/downloads \
  --exclude=$NAME/apps/init.sh \
  --exclude=$NAME/bundle \
  --exclude=$NAME/bundle.sh \
  --exclude=$NAME/public \
  --exclude=$NAME/resources \
  --exclude=$NAME/DOCUMENTATION.md \
  --exclude=$NAME/README.md \
  "$NAME"
