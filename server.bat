@echo off
goto :TopOfCode

================================================================================

Start Hugo server.

Copyright 2009-2019 OpenEstate.org.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

================================================================================

:TopOfCode

set OPTIONS=
REM set OPTIONS=--buildDrafts --disableFastRender --disableLiveReload

set DIR=%~dp0
set DIR=%DIR:~0,-1%

echo.
echo ----------------------------------------
echo  Den Test-Server starten.
echo ----------------------------------------
echo.

cd %DIR%
cmd /c "apps\hugo.bat server %OPTIONS%"

echo.
echo ----------------------------------------
echo  Der Test-Server wurde beendet.
echo ----------------------------------------
echo.

pause
