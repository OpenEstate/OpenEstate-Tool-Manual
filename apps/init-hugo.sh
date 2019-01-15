#!/usr/bin/env bash
#
# Download Hugo.
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

#
# Hugo für Linux & Windows
#
# bereitgestellt von
# https://github.com/gohugoio/hugo/releases
#

HUGO_VERSION="0.53"
HUGO_DOWNLOAD_LINUX="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz"
HUGO_DOWNLOAD_WINDOWS="https://github.com/gohugoio/hugo/releases/download/v$HUGO_VERSION/hugo_${HUGO_VERSION}_Windows-32bit.zip"


#
# Start der Verarbeitung
#

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

TEMP_DIR="$DIR/downloads"
mkdir -p "$TEMP_DIR"

TEMP_HUGO_LINUX="$TEMP_DIR/hugo-${HUGO_VERSION}-linux.tar.gz"
if [ ! -f "$TEMP_HUGO_LINUX" ]; then
  echo ""
  echo "Downloading Hugo ${HUGO_VERSION} for Linux …"
  wget -O "$TEMP_HUGO_LINUX" "$HUGO_DOWNLOAD_LINUX"
fi

TEMP_HUGO_WINDOWS="$TEMP_DIR/hugo-${HUGO_VERSION}-windows.zip"
if [ ! -f "$TEMP_HUGO_WINDOWS" ]; then
  echo ""
  echo "Downloading Hugo ${HUGO_VERSION} for Windows …"
  wget -O "$TEMP_HUGO_WINDOWS" "$HUGO_DOWNLOAD_WINDOWS"
fi

echo ""
echo "Extracting Linux software …"
LINUX_DIR="$DIR/linux"
rm -Rf "$LINUX_DIR"
mkdir -p "${LINUX_DIR}/bin"
tar xvfz "$TEMP_HUGO_LINUX" -C "${LINUX_DIR}/bin" "hugo"
find "${LINUX_DIR}/bin" -type f -exec chmod ugo+x {} \;

echo ""
echo "Extracting Windows software …"
WINDOWS_DIR="$DIR/windows"
rm -Rf "$WINDOWS_DIR"
mkdir -p "$WINDOWS_DIR"
unzip "$TEMP_HUGO_WINDOWS" "hugo.exe" -d "${WINDOWS_DIR}/bin"
find "$WINDOWS_DIR" -type f -exec chmod ugo-x {} \;

echo ""
echo "Extracting licenses …"
LICENSES_DIR="$DIR/licenses"
rm -Rf "$LICENSES_DIR"
mkdir -p "$LICENSES_DIR"
unzip -p "$TEMP_HUGO_WINDOWS" "LICENSE" > "${LICENSES_DIR}/hugo.txt"
unix2dos "${LICENSES_DIR}/hugo.txt"
