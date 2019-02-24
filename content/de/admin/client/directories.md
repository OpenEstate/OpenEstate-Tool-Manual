---

title: Verzeichnisse des ImmoTools
linktitle: Verzeichnisse
description: Wo OpenEstate-ImmoTool seine Daten speichert…
weight: 20

menu:
  main:
    parent: admin-client
    identifier: admin-client-directories

---

## Verzeichnisse des ImmoTools {#admin_client_directories}

Für den Betrieb des ImmoTools werden verschiedene Verzeichnisse auf der Festplatte verwendet.


### Programm-Verzeichnis des ImmoTools {#admin_client_directories_application}

Das Programm-Verzeichnis enthält die installierten Dateien des ImmoTools.

-   Unter Windows lautet das Verzeichnis standardmäßig **`C:\Programme\OpenEstate-ImmoTool`**. Bei der Installation kann jedoch bei Bedarf ein anderes Verzeichnis gewählt werden.

-   Unter macOS hängt es davon ab, wohin das Programm bei der Installation kopiert wurde. Standardmäßig befindet sich das Programm-Paket unter dem Pfad **`/Applications/OpenEstate-ImmoTool.app`**. Das Programm-Verzeichnis selbst befindet sich im Unterordner **`Contents/Resources`** des Programm-Pakets.

-   Wenn unter Debian, Ubuntu, Linux Mint & Co. das [**Debian**-Paket]({{< relref "../../intro/install_client.md#intro_install_client_setup_debian" >}}) (bzw. Debian-Repository) zur Installation verwendet wurde, wird das Programm unter **`/opt/OpenEstate-ImmoTool`** installiert.

-   Wenn unter Linux das [**TAR.GZ**-Paket]({{< relref "../../intro/install_client.md#intro_install_client_setup_linux" >}}) zur Installation verwendet wurde, hängt es davon ab wohin Sie das entpackte Verzeichnis während der Installation verschoben haben.

Im Programm-Verzeichnis finden Sie einen Unterordner namens **`bin`**, der diverse Skripte und Programme für das ImmoTool enthält.

Das ImmoTool schreibt **keine** Dateien in das Programm-Verzeichnis. Aus diesem Verzeichnis wird nur gelesen.

{{< tip >}}
Es bietet sich an, das Programm-Verzeichnis für normale Betriebssystem-Benutzer nicht beschreibbar zu machen. Es ist ausreichend, wenn der Betriebssystem-Administrator Schreibrechte auf diesem Verzeichnis besitzt um Aktualisierungen vornehmen zu können. 
{{< /tip >}}


### Daten-Verzeichnis des ImmoTools {#admin_client_directories_data}

Wenn ein Benutzer das ImmoTool startet, wird automatisch in seinem persönlichen Benutzer-Verzeichnis ein Ordner namens **`OpenEstate-Files`** erzeugt. Dieser Ordner enthält die Daten und Einstellungen des ImmoTools **exklusiv** für den Betriebssystem-Benutzer.

In dieses Verzeichnis speichert das ImmoTool diverse Daten während der Ausführung (z.B. Protokolle oder temporäre Dateien).


### Projekt-Verzeichnis des ImmoTools {#admin_client_directories_project}

Beim Erstellen eines Projekts im ImmoTool kann ein beliebiger Speicherort für das Projekt-Verzeichnis gewählt werden. Standardmäßig speichert das Programm das Projekt-Verzeichnis im Unterordner **`projects`** des [Daten-Verzeichnisses]({{< relref "directories.md#admin_client_directories_data" >}}) des aktuellen Benutzers. 

{{< info >}}
Jedes im ImmoTool erstellte Projekt wird in einem eigenen / separaten Verzeichnis gespeichert. Somit können die Daten eines Projekts schnell und unkompliziert gesichert, verschoben oder ausgetauscht werden.
{{< /info >}}

{{< info >}}
Es ist theoretisch möglich, dass sich mehrere Benutzer ein gemeinsames Projekt-Verzeichnis teilen (z.B. über einen gemeinsam erreichbaren Ordner). Jedoch können [Einzelplatz-Projekte]({{< relref "../../intro/install_types.md#intro_install_types_local" >}}) niemals gleichzeitig von zwei Benutzern geöffnet werden.
{{< /info >}}

{{< warning >}}
Das Projekt-Verzeichnis sollte **unter keinen Umständen** von einem instabilen Laufwerk (z.B. Netzlaufwerk oder Cloud-Speicher) mit dem ImmoTool geöffnet werden. Kurzfristige Netzwerk-Probleme können zu einer fehlerhaften Datenbank führen. Wer diesen Weg dennoch gehen will / muss, sollte umso häufiger Datensicherungen durchführen.
{{< /warning >}}


### Plugin-Verzeichnis des ImmoTools {#admin_client_directories_plugins}

Im Plugin-Verzeichnis werden Erweiterungen (Add-Ons) für das ImmoTool als ZIP-Dateien hinterlegt. Es gibt zwei Orte an denen Add-Ons hinterlegt werden können:

1.  Im [Programm-Verzeichnis]({{< relref "directories.md#admin_client_directories_application" >}}) finden Sie einen Unterordner namens **`plugins`**. Der Betriebssystem-Administrator kann hier Add-Ons hinterlegen, die für alle Betriebssystem-Benutzer verfügbar sind.

2.  Im [Daten-Verzeichnis]({{< relref "directories.md#admin_client_directories_data" >}}) eines jeden Betriebssystem-Benutzers finden Sie ebenfalls einen Unterordner namens **`plugins`**. Der Benutzer kann hier Add-Ons hinterlegen, die nur für ihn verfügbar sind.

Beim Programmstart gleicht das ImmoTool beide Plugin-Verzeichnisse miteinander ab. Wenn in beiden Ordnern das gleiche Plugin in einer unterschiedlichen Version vorhanden ist, wird das Add-On mit der jeweils aktuelleren Version ins Programm geladen.

{{< warning >}}
Unter macOS sollte man im Plugin-Verzeichnis des Programms (innerhalb des Programm-Pakets **"OpenEstate-ImmoTool"**) keine eigenen Änderungen vornehmen. Andernfalls wird die Signatur des Programm-Pakets ungültig und es kann zu Problemen mit [Gatekeeper](https://support.apple.com/de-de/HT202491) kommen. Daher sollten unter macOS weitere Add-Ons grundsätzlich nur im Unterordner **`plugins`** des [Daten-Verzeichnisses]({{< relref "directories.md#admin_client_directories_data" >}}) hinterlegt werden.
{{< /warning >}}
