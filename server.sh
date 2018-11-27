#!/usr/bin/env bash
#
# Start Hugo server.
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

OPTIONS=""
#OPTIONS="--buildDrafts --disableFastRender --disableLiveReload"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo ""
echo "----------------------------------------"
echo " Test-Server für die Webseite starten."
echo "----------------------------------------"

cd "$DIR"
"$DIR/apps/hugo.sh" server ${OPTIONS}

echo ""
echo "----------------------------------------"
echo " Der Test-Server wurde beendet."
echo "----------------------------------------"
echo ""
