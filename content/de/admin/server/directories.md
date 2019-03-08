---

title: Verzeichnisse des ImmoTool-Servers
linktitle: Verzeichnisse
description: Welche Verzeichnisse von OpenEstate-ImmoServer verwendet werden…
weight: 20

menu:
  main:
    parent: admin-server
    identifier: admin-server-directories

---

## Verzeichnisse des ImmoTool-Servers {#admin_server_directories}

Für den Betrieb des ImmoTool-Servers werden verschiedene Verzeichnisse auf der Festplatte verwendet.


### Programm-Verzeichnis des ImmoTool-Servers {#admin_server_directories_application}

Das Programm-Verzeichnis enthält die installierten Dateien des ImmoTool-Servers.

-   Unter Windows lautet das Verzeichnis standardmäßig **`C:\Programme\OpenEstate-ImmoServer`**. Bei der Installation kann jedoch bei Bedarf ein anderes Verzeichnis gewählt werden.

-   Unter macOS hängt es davon ab, wohin das Programm bei der Installation kopiert wurde. Standardmäßig befindet sich das Programm-Paket unter dem Pfad **`/Applications/OpenEstate-ImmoServer.app`**. Das Programm-Verzeichnis selbst befindet sich im Unterordner **`Contents/Resources`** des Programm-Pakets.

-   Wenn unter Debian, Ubuntu, Linux Mint & Co. das [**Debian**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) (bzw. Debian-Repository) zur Installation verwendet wurde, wird das Programm unter **`/opt/OpenEstate-ImmoServer`** installiert.

-   Wenn unter Linux das [**TAR.GZ**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}}) zur Installation verwendet wurde, hängt es davon ab wohin Sie das entpackte Verzeichnis während der Installation verschoben haben.

Im Programm-Verzeichnis finden Sie einen Unterordner namens **`bin`**, der diverse Skripte und Programme für den ImmoTool-Server enthält.

Der ImmoTool-Server schreibt **keine** Dateien in das Programm-Verzeichnis. Aus diesem Verzeichnis wird nur gelesen.

{{< tip >}}
Es bietet sich an, das Programm-Verzeichnis für normale Betriebssystem-Benutzer nicht beschreibbar zu machen. Es ist ausreichend, wenn der Betriebssystem-Administrator Schreibrechte auf diesem Verzeichnis besitzt um Aktualisierungen vornehmen zu können. 
{{< /tip >}}


### Daten-Verzeichnis des ImmoTool-Servers {#admin_server_directories_data}

Im Daten-Verzeichnis speichert der ImmoTool-Server standardmäßig die verwalteten Datenbanken sowie automatisch erzeugte Datensicherungen.

-   Wenn unter Debian, Ubuntu, Linux Mint & Co. das [**Debian**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) (bzw. Debian-Repository) zur Installation verwendet wurde, wird das Verzeichnis **`/var/lib/OpenEstate-ImmoServer`** als Daten-Verzeichnis verwendet.

-   Bei allen anderen Installationen (Windows, macOS, Linux via [**TAR.GZ**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}})) wird im persönlichen Benutzer-Verzeichnis des ausführenden Benutzers ein Ordner namens **`OpenEstate-Files`** erzeugt und als Daten-Verzeichnis verwendet.


### Protokoll-Verzeichnis des ImmoTool-Servers {#admin_server_directories_log}

Im Protokoll-Verzeichnis speichert der ImmoTool-Server verschiedene Protokolle mit Meldungen, die während der Ausführung des Programms auftreten können.

-   Wenn unter Debian, Ubuntu, Linux Mint & Co. das [**Debian**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) (bzw. Debian-Repository) zur Installation verwendet wurde, wird das Verzeichnis **`/var/log/OpenEstate-ImmoServer`** als Protokoll-Verzeichnis verwendet.

-   Bei allen anderen Installationen (Windows, macOS, Linux via [**TAR.GZ**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}})) wird der Unterordner **`logs`** im [Daten-Verzeichnis]({{< relref "directories.md#admin_server_directories_data" >}}) des ausführenden Benutzers verwendet.


### Konfigurations-Verzeichnis des ImmoTool-Servers {#admin_server_directories_etc}

Aus dem Konfigurations-Verzeichnis lädt der ImmoTool-Server seine Konfigurationen.

-   Unter Windows wird der Unterordner **`etc`** des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) als Konfigurations-Verzeichnis verwendet.

-   Unter macOS wird beim ersten Programmstart im [Daten-Verzeichnis]({{< relref "directories.md#admin_server_directories_data" >}}) des ausführenden Benutzers ein Unterordner **`etc`** erzeugt. Die Konfigurations-Dateien werden in diesen Ordner kopiert. 

-   Wenn unter Debian, Ubuntu, Linux Mint & Co. das [**Debian**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) (bzw. Debian-Repository) zur Installation verwendet wurde, wird das Verzeichnis **`/etc/OpenEstate-ImmoServer`** als Konfigurations-Verzeichnis verwendet.

-   Wenn unter Linux das [**TAR.GZ**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}}) zur Installation verwendet wurde, werden die Konfigurationen aus dem **`etc`** Unterordner des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) geladen.

{{< info >}}
Im Kapitel ["ImmoTool-Server konfigurieren"]({{< relref "setup.md#admin_server_setup" >}}) finden Sie weitere Informationen, wie der ImmoTool-Server über die Dateien im Konfigurations-Verzeichnis auf Ihre Bedürfnisse hin angepasst werden kann.
{{< /info >}}


### Verzeichnisse des ImmoTool-Servers konfigurieren {#admin_server_directories_setup}

Bei Bedarf können die vom ImmoTool-Server verwendeten Verzeichnisse konfiguriert werden.

{{< info >}}
Der Betriebssystem-Benutzer, welcher den ImmoTool-Server startet, muss Schreibrechte auf dem Protokoll- und Daten-Verzeichnis haben. Auf dem Konfigurations-Verzeichnis benötigt der Benutzer mindestens Leserechte.
{{< /info >}}


#### Verzeichnisse unter Linux & macOS konfigurieren {#admin_server_directories_setup_unix}

Unter Linux und macOS kann eine Datei **`/etc/default/OpenEstate-ImmoServer`** mit folgendem Inhalt angelegt werden:

```bash
# Pfad zum Konfigurations-Verzeichnis
SERVER_ETC_DIR="/etc/OpenEstate-ImmoServer"

# Pfad zum Protokoll-Verzeichnis
SERVER_LOG_DIR="/var/log/OpenEstate-ImmoServer"

# Pfad zum Daten-Verzeichnis
SERVER_VAR_DIR="/var/lib/OpenEstate-ImmoServer"
```

In den Variablen können die Pfade entsprechend hinterlegt werden. Beim nächsten Start des ImmoTool-Servers werden diese Verzeichnisse verwendet.


#### Verzeichnisse unter Windows konfigurieren {#admin_server_directories_setup_windows}

Unter Windows hängt es davon ab, wie die einzelnen Programme des ImmoTool-Servers gestartet werden.

-   Falls **EXE**-Dateien verwendet werden, können die gleichnamigen **`l4j.ini`** Dateien mit einem Texteditor bearbeitet werden. Folgende Zeilen können darin geändert werden:

    ```ini
    # Pfad zum Konfigurations-Verzeichnis
    -Dopenestate.server.etcDir=D:\OpenEstate-ImmoServer\etc
    
    # Pfad zum Protokoll-Verzeichnis
    -Dopenestate.server.logDir=D:\OpenEstate-ImmoServer\logs
    
    # Pfad zum Daten-Verzeichnis
    -Dopenestate.server.varDir=D:\OpenEstate-ImmoServer
    ```

-   Falls **BAT**-Dateien verwendet werden, können diese mit einem Texteditor bearbeitet werden. Folgende Zeilen können darin geändert werden:

    ```batch
    :: Pfad zum Konfigurations-Verzeichnis
    set "SERVER_ETC_DIR=D:\OpenEstate-ImmoServer\etc"
    
    :: Pfad zum Protokoll-Verzeichnis
    set "SERVER_LOG_DIR=D:\OpenEstate-ImmoServer\logs"
    
    :: Pfad zum Daten-Verzeichnis
    set "SERVER_VAR_DIR=D:\OpenEstate-ImmoServer"
    ```
    
-   Falls ein Dienst unter Windows eingerichtet wurde, können die Pfade über die Dienst-Verwaltung angepasst werden (siehe ["Dienst unter Windows verwalten"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

    {{< figure src="directories_setup_windows_service.png" caption="Pfade in der Dienst-Verwaltung von Windows konfigurieren" >}}
    
    Wählen Sie in der Dienst-Verwaltung den Tab **"Java"** und tragen Sie im Textfeld **"Java Options"** die gewünschten Pfade hinter den folgenden Variablen ein:
    
    -   Hinter **`-Dopenestate.server.etcDir=`** kann der Pfad des [Konfigurations-Verzeichnisses]({{< relref "directories.md#admin_server_directories_etc" >}}) eingetragen werden.
    -   Hinter **`-Dopenestate.server.logDir=`** kann der Pfad des [Protokoll-Verzeichnisses]({{< relref "directories.md#admin_server_directories_log" >}}) eingetragen werden.
    -   Hinter **`-Dopenestate.server.varDir=`** kann der Pfad des [Daten-Verzeichnisses]({{< relref "directories.md#admin_server_directories_data" >}}) eingetragen werden.

