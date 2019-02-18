---

title: ImmoTool starten
linktitle: Programmstart
description: Details zum Programmstart von OpenEstate-ImmoTool…
weight: 10

menu:
  main:
    parent: admin-client
    identifier: admin-client-startup

---

## ImmoTool starten {#admin_client_startup}

### ImmoTool unter Windows starten {#admin_client_startup_windows}

Bei der Installation unter Windows wird automatisch eine Verknüpfung auf dem Desktop erzeugt, über die das Programm gestartet werden kann. Alternativ finden Sie im Startmenü einen Ordner namens `OpenEstate-ImmoTool` mit verschiedenen Verknüpfungen.

Darüber hinaus können Sie das Programm auch über die Datei `ImmoTool.exe` / `ImmoTool.bat` im Verzeichnis `bin` des Programm-Verzeichnisses starten.


### ImmoTool unter macOS starten {#admin_client_startup_mac}

Führen Sie einen Doppelklick auf das Programmsymbol mit der Bezeichnung **OpenEstate-ImmoTool** aus. Es öffnet sich daraufhin der Finder mit den vom ImmoTool bereitgestellten Programmen.

{{< figure src="startup_mac.png" caption="Starter für ImmoTool im Finder" >}}

Wenn Sie in diesem Fenster auf das **ImmoTool**-Symbol klicken, wird das Programm gestartet.

{{< tip >}}
Bei Bedarf können Sie das ImmoTool-Symbol ins Dock integrieren, um das Programm später schnell und unkompliziert starten zu können (siehe ["Anleitung bei Apple"](https://support.apple.com/de-de/HT201730)).
{{< /tip >}}

Um ImmoTool unter macOS über das Terminal zu starten, kann das Skript `ImmoTool.sh` im Ordner `OpenEstate-ImmoTool.app/Contents/Resources/bin` verwendet werden.


### ImmoTool unter Linux starten {#admin_client_startup_linux}

Wenn das ImmoTool mit dem [**Debian**-Paket]({{< relref "../../intro/install_client.md#intro_install_client_setup_debian" >}}) installiert wurde, finden Sie im Startmenü die Einträge für den Start des Programms.

Wenn das ImmoTool mit dem [**TAR.GZ**-Paket]({{< relref "../../intro/install_client.md#intro_install_client_setup_linux" >}}) installiert wurde, müssen Sie ggf. vorher noch die Datei `StartMenuAdd.sh` im `bin`-Verzeichnis des Programms ausführen um die Einträge im Startmenü zu erzeugen.

Alternativ zum Startmenü kann das Programm über die Datei `ImmoTool.sh` im `bin`-Verzeichnis des Programms gestartet werden.


### Parameter zum Start des ImmoTools {#admin_client_startup_params}

Der Programmstart via `ImmoTool.exe` / `ImmoTool.bat` / `ImmoTool.sh` kann durch verschiedene Parameter beeinflusst werden.

-   **-help** \
    Stellt eine Zusammenfassung aller Parameter auf der Konsole dar und beendet das Programm.

-   **-noProject** \
    Startet das Programm ohne automatisch ein Projekt zu öffnen. Statt dessen wird der [Projektassistent]({{< relref "../../usage/general/projects.md#usage_general_projects_wizard" >}}) dargestellt.

-   **-project `<PROJEKT>`** \
    Das Projekt, welches im Ordner `<PROJEKT>` abgelegt ist, wird beim Programmstart automatisch geöffnet.

-   **-projectLogin `<BENUTZER>`** \
    Wenn das unter `-project` angegebene Projekt ein Mehrplatz-Projekt ist, meldet sich das ImmoTool beim Programmstart automatisch mit dem Benutzernamen `<BENUTZER>` an.

-   **-projectPass `<PASSWORT>`** \
    Wenn das unter `-project` angegebene Projekt ein Mehrplatz-Projekt ist, meldet sich das ImmoTool beim Programmstart automatisch mit dem Passwort `<PASSWORT>` an.
