---

title: ImmoTool-Server starten
linktitle: Server starten
description: Administration von OpenEstate-ImmoTool…
weight: 10

menu:
  main:
    parent: admin-server
    identifier: admin-server-startup

---

## ImmoTool-Server starten {#admin_server_startup}

Die Dateien zum Start des ImmoTool-Servers sind im Unterverzeichnis `bin` des Programm-Verzeichnisses abgelegt - z.B.: `C:\Programme\OpenEstate-ImmoServer\bin`.


### ImmoTool-Server unter Windows starten {#admin_server_startup_windows}

Starten Sie den ImmoTool-Server unter **Windows** durch Doppelklick auf die Datei `start.exe` oder `start.bat` im Unterordner `bin`.


### ImmoTool-Server unter Mac OS X starten {#admin_server_startup_mac}

Starten Sie den ImmoTool-Server unter **Mac OS X** durch Doppelklick auf das *Datenbank*-Symbol im Unterordner `bin`.


### ImmoTool-Server unter Linux / Unix starten {#admin_server_startup_unix}

Starten Sie den ImmoTool-Server unter **Linux**, **Unix** oder **Mac OS X** durch Ausführung der Datei `start.sh` im Unterordner `bin`.


### Start-Dateien des ImmoTool-Servers {#admin_server_startup_files}

Das `bin`-Verzeichnis des ImmoTool-Servers enthält diverse Start-Dateien für verschiedene Zwecke und Betriebssysteme.

-   **manager-backup.bat** (Windows)
    **manager-backup.app** (Mac OS X)
    **manager-backup.sh** (Linux / Unix / Mac OS X)
    Öffnet eine Verbindung zu einem gestarteten ImmoTool-Server und führt einen Befehl zur Datensicherung aus. Die erzeugte Sicherungsdatei wird standardmäßig im Verzeichnis `var/backup` abgelegt.

-   **manager-console.bat** (Windows)
    **manager-console.exe** (Windows)
    **manager-console.sh** (Linux / Unix / Mac OS X)
    Öffnet eine Administrator-Konsole, die Steuerbefehle oder SQL-Anfragen auf der Datenbank ausführen kann.

-   **manager-gui.bat** (Windows)
    **manager-gui.exe** (Windows)
    **manager-gui.app** (Mac OS X)
    **manager-gui.sh** (Linux / Unix / Mac OS X)
    Öffnet eine grafische Administrations-Anwendung, die Steuerbefehle oder SQL-Anfragen auf der Datenbank ausführen kann.

-   **manager-shutdown.bat** (Windows)
    **manager-shutdown.app** (Mac OS X)
    **manager-shutdown.sh** (Linux / Unix / Mac OS X)
    Öffnet eine Verbindung zu einem gestarteten ImmoTool-Server und führt einen Befehl zum Herunterfahren der Datenbank aus.

-   **server-console.bat** (Windows)
    **server-console.sh** (Linux / Unix / Mac OS X)
    ImmoTool-Server im Vordergrund ausführen.

-   **server-daemon-install.bat** (Windows)
    **server-daemon-install.sh** (Linux / Unix / Mac OS X)
    ImmoTool-Server als Dienst im Betriebssystem installieren.

-   **server-daemon-query.bat** (Windows)
    **server-daemon-query.sh** (Linux / Unix / Mac OS X)
    Überprüfung ob der ImmoTool-Server-Dienst installiert und/oder gestartet ist.

-   **server-daemon-start.bat** (Windows)
    **server-daemon-start.sh** (Linux / Unix / Mac OS X)
    Installierten ImmoTool-Server als Dienst im Hintergrund starten.

-   **server-daemon-stop.bat** (Windows)
    **server-daemon-stop.sh** (Linux / Unix / Mac OS X)
    Gestarteten ImmoTool-Server-Dienst beenden.

-   **server-daemon-uninstall.bat** (Windows)
    **server-daemon-uninstall.sh** (Linux / Unix / Mac OS X)
    Installierten ImmoTool-Server-Dienst aus dem Betriebssystem entfernen.

-   **server-daemon-setenv.bat** (Windows)
    **server-daemon-setenv.sh** (Linux / Unix / Mac OS X)
    Diese Datei konfiguriert verschiedene Umgebungsvariablen für die `server-*`-Skripte und kann nicht direkt gestartet werden.

-   **server-daemon-wrapper.bat** (Windows)
    **server-daemon-wrapper.sh** (Linux / Unix / Mac OS X)
    Diese Datei wird von den `server-*`-Skripten verwendet um den ImmoTool-Server auszuführen und kann nicht direkt gestartet werden.

-   **start.bat** (Windows)
    **start.exe** (Windows)
    **start.app** (Mac OS X)
    **start.sh** (Linux / Unix / Mac OS X)
    ImmoTool-Server im Vordergrund ausführen.


> **Hinweis**
>
> Die Skripte beginnend mit `server-*` werden mit Hilfe des Projektes [YAJSW](http://yajsw.sourceforge.net/) bereitgestellt. Weitere Informationen zur Konfiguration dieser Skripte finden Sie auf der Webseite dieses Projektes.

