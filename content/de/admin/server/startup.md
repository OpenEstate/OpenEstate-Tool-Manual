---

title: ImmoTool-Server starten
linktitle: Server starten
description: Wie OpenEstate-ImmoServer gestartet werden kann…
weight: 10

menu:
  main:
    parent: admin-server
    identifier: admin-server-startup

---

## ImmoTool-Server starten {#admin_server_startup}

Die einfachste Form den ImmoTool-Server zu starten ist die manuelle Ausführung **im Vordergrund**. 

Wenn das Programm erfolgreich eingerichtet wurde und von den Arbeitsplätzen erfolgreich auf den ImmoTool-Server zugegriffen werden kann, empfiehlt sich die Einrichtung eines Dienstes, sodass der ImmoTool-Server automatisch beim Hochfahren des Rechners **im Hintergrund** gestartet wird (siehe ["ImmoTool-Server als Dienst einrichten"]({{< relref "service.md#admin_server_service" >}})).


### ImmoTool-Server unter Windows starten {#admin_server_startup_windows}

Bei der Installation unter Windows wird automatisch im Startmenü einen Ordner namens **"OpenEstate-ImmoTool"** mit verschiedenen Verknüpfungen erzeugt. Wählen Sie die Verknüpfung **"ImmoServer manuell starten"** aus dem Startmenü aus, um den ImmoTool-Server manuell (bzw. im Vordergrund) zu starten.

Darüber hinaus können Sie das Programm auch über die Datei **`Start.exe`** (bzw. **`Start.bat`**) im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) manuell (bzw. im Vordergrund) starten.

Beim ersten Start des ImmoTool-Servers werden Sie vom Betriebssystem eventuell gefragt, ob eingehende Verbindungen akzeptiert werden sollen. Diese Frage sollte mit **"Zugriff zulassen"** beantwortet werden.

{{< figure src="startup_windows_firewall.png" caption="Freigabe in der Firewall unter Windows erteilen" >}}


### ImmoTool-Server unter macOS starten {#admin_server_startup_mac}

Führen Sie einen Doppelklick auf das Programmsymbol mit der Bezeichnung **"OpenEstate-ImmoServer"** aus. Es öffnet sich daraufhin der Finder mit den vom ImmoTool-Server bereitgestellten Programmen.

{{< figure src="startup_mac_folder.png" caption="Starter für ImmoTool-Server im Finder" >}}

Wenn Sie in diesem Fenster auf das Programmsymbol **"Start"** klicken, wird der ImmoTool-Server manuell (bzw. im Vordergrund) gestartet.

Beim ersten Start des ImmoTool-Servers werden Sie vom Betriebssystem eventuell gefragt, ob eingehende Verbindungen akzeptiert werden sollen. Diese Frage sollte mit **"Erlauben"** beantwortet werden.

{{< figure src="startup_mac_firewall.png" caption="Freigabe in der Firewall unter macOS erteilen" >}}


### ImmoTool-Server unter Linux starten {#admin_server_startup_linux}

Wenn der ImmoTool-Server mit dem [**Debian**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) installiert wurde, ist auf dem Betriebssystem bereits ein Dienst für den ImmoTool-Server eingerichtet und gestartet worden. Sie müssen in diesem Falle keine weiteren Schritte durchführen um das Programm zu starten.

Bei allen Installations-Varianten für Linux kann der ImmoTool-Server über das Skript **`Start.sh`** im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) manuell (bzw. im Vordergrund) gestartet werden.
