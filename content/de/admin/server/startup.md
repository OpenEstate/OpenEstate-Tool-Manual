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

Die einfachste Form den ImmoTool-Server zu starten ist die manuelle Ausführung **im "Vordergrund"**. 

Wenn das Programm erfolgreich eingerichtet wurde und von den Arbeitsplätzen erfolgreich auf den ImmoTool-Server zugegriffen werden kann, empfiehlt sich die Einrichtung eines Dienstes, sodass der ImmoTool-Server automatisch beim Hochfahren des Rechners **im "Hintergrund"** gestartet wird.

{{< todo >}}
Link zur Einrichtung als Dienst hinterlegen.
{{< /todo >}}


### ImmoTool-Server unter Windows starten {#admin_server_startup_windows}

Bei der Installation unter Windows wird automatisch im Startmenü einen Ordner namens **"OpenEstate-ImmoTool"** mit verschiedenen Verknüpfungen erzeugt. Wählen Sie die Verknüpfung **"ImmoServer manuell starten"** aus dem Startmenü aus, um den ImmoTool-Server manuell zu starten.

Darüber hinaus können Sie das Programm auch über die Datei `Start.exe` / `Start.bat` im Verzeichnis `bin` des Programm-Verzeichnisses manuell starten.


### ImmoTool-Server unter macOS starten {#admin_server_startup_mac}

Führen Sie einen Doppelklick auf das Programmsymbol mit der Bezeichnung **OpenEstate-ImmoServer** aus. Es öffnet sich daraufhin der Finder mit den vom ImmoTool-Server bereitgestellten Programmen.

{{< figure src="startup_mac.png" caption="Starter für ImmoTool-Server im Finder" >}}

Wenn Sie in diesem Fenster auf das **Start**-Symbol klicken, wird das Programm gestartet.


### ImmoTool-Server unter Linux starten {#admin_server_startup_linux}

Wenn der ImmoTool-Server mit dem [**Debian**-Paket]({{< relref "install_server.md#intro_install_server_setup_debian" >}}) installiert wurde, ist auf dem Betriebssystem bereits ein Dienst für den ImmoTool-Server eingerichtet und gestartet worden. Sie müssen in diesem Falle keine weiteren Schritte durchführen um das Programm zu starten.

Bei allen Installations-Varianten für Linux kann der ImmoTool-Server über das Skript `Start.sh` im `bin`-Verzeichnis des Programms gestartet werden.
