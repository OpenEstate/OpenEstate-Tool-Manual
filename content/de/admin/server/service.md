---

title: ImmoTool-Server als Dienst einrichten
linktitle: Dienst einrichten
description: Wie OpenEstate-ImmoServer als Dienst im Betriebssystem eingerichtet werden kann…
weight: 40

menu:
  main:
    parent: admin-server
    identifier: admin-server-service

---

## ImmoTool-Server als Dienst einrichten {#admin_server_service}

Für den alltäglichen Betrieb ist es sinnvoll, den ImmoTool-Server als Dienst in das Betriebssystem zu integrieren. Der ImmoTool-Server kann damit **automatisch** beim Hochfahren des Betriebssystems im Hintergrund gestartet werden. Der Administrator den Dienst von außen unkompliziert steuern (Start / Stopp / Neustart).


### Dienst unter Windows einrichten {#admin_server_service_windows}

Zur Einrichtung des ImmoTool-Servers als Dienst unter Windows wird die Open Source Software [commons-daemon](https://commons.apache.org/daemon/) der [Apache Software Foundation](https://apache.org/) verwendet. Die Programme im Unterordner **`bin\service`** des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) stammen vom "commons-daemon" Projekt.


#### Dienst unter Windows installieren {#admin_server_service_windows_install}

Der ImmoTool-Server kann auf folgenden Wegen als Dienst im Betriebssystem registriert werden:

-   Klicken Sie im Startmenü auf **"OpenEstate-ImmoServer → Dienst → ImmoServer-Dienst installieren"**.

-   Öffnen Sie den Ordner **`bin`** im [Programm-Verzeichnis]({{< relref "directories.md#admin_server_directories_application" >}}) und starten Sie das Skript **`ServiceInstall.bat`** per Doppelklick.

Da ein Dienst nur vom Windows-Administrator eingerichtet werden kann, müssen Sie die Erlaubnis zur Ausführung als Administrator erteilen.

Nach erfolgreicher Installation öffnet sich ein Dialogfenster, über welches der installierte Dienst ggf. weiter bearbeitet werden kann. 

{{< figure src="service_windows_install.png" caption="Verwaltung des Dienstes unter Windows" >}}

Bei Bedarf können z.B. im Tab **"Java"** die vom ImmoTool-Server verwendeten Verzeichnisse konfiguriert werden (siehe ["Verzeichnisse des ImmoTool-Servers"]({{< relref "directories.md#admin_server_directories" >}})):

{{< figure src="directories_setup_windows_service.png" caption="Pfade in der Dienst-Verwaltung von Windows konfigurieren" >}}

Nachdem die Einstellungen vorgenommen wurden klicken Sie auf **"Übernehmen"**. Sie können das Dialogfenster nun schließen oder den ImmoTool-Server direkt aus dem Dialogfenster starten. Klicken Sie dafür im Tab **"General"** auf den Button **"Start"**.

Beim ersten Start des ImmoTool-Servers werden Sie vom Betriebssystem eventuell gefragt, ob eingehende Verbindungen akzeptiert werden sollen. Diese Frage sollte mit **"Zugriff zulassen"** beantwortet werden.

{{< figure src="startup_windows_firewall.png" caption="Freigabe in der Firewall unter Windows erteilen" >}}


#### Dienst unter Windows deinstallieren {#admin_server_service_windows_uninstall}

Der Dienst des ImmoTool-Servers kann auf folgenden Wegen entfernt werden:

-   Klicken Sie im Startmenü auf **"OpenEstate-ImmoServer → Dienst → ImmoServer-Dienst deinstallieren"**.

-   Öffnen Sie den Ordner **`bin`** im [Programm-Verzeichnis]({{< relref "directories.md#admin_server_directories_application" >}}) und starten Sie das Skript **`ServiceUninstall.bat`** per Doppelklick.

Es öffnet sich daraufhin ein Fenster mit der Eingabeaufforderung, über welches die Deinstallation durchgeführt wird. Sie sollten in diesem Fenster eine Erfolgsmeldung oder Fehlermeldung dargestellt bekommen.

{{< info >}}
Bei einer Deinstallation des ImmoTool-Servers wird auch ein zuvor installierter Dienst aus dem Betriebssystem entfernt.
{{< /info >}}


#### Dienst unter Windows verwalten {#admin_server_service_windows_manage}

Der ImmoTool-Server stellt ein Programm zur Verwaltung / Konfiguration des Dienstes bereit. Das Programm kann auf folgenden Wegen gestartet werden:

-   Klicken Sie im Startmenü auf **"OpenEstate-ImmoServer → Dienst → ImmoServer-Dienst verwalten"**.

-   Öffnen Sie den Ordner **`bin\service`** im [Programm-Verzeichnis]({{< relref "directories.md#admin_server_directories_application" >}}) und starten Sie die Datei **`OpenEstate-ImmoServer.exe`** per Doppelklick.

Über dieses von der Apache Software Foundation bereitgestellte Programm können diverse Einstellungen zum Dienst vorgenommen werden. Ebenso kann der Dienst gestartet / gestoppt werden.

Alternativ können Sie die Dienste-Verwaltung im Windows Betriebssystem öffnen.

1.  Drücken Sie auf der Tastatur die **"Windows-Taste"** gemeinsam mit dem Buchstaben **"R"** um ein Fenster zur Ausführung von Programmen zu öffnen. Alternativ können Sie die Eingabeaufforderung öffnen.

2.  Tragen Sie den Befehl **`services.msc`** ein und bestätigen Sie die Eingabe mit **"ENTER"**.

Es öffnet sich daraufhin die Dienste-Verwaltung des Windows-Betriebssystems.

{{< figure src="service_windows_manage.png" caption="Dienste-Verwaltung des Windows-Betriebssystems" >}}

Über dieses Fenster kann der Dienst ebenfalls gestartet, gestoppt und per Doppelklick bearbeitet werden.


#### Dienst unter Windows starten {#admin_server_service_windows_start}

Nachdem der Dienst unter Windows installiert wurde (siehe ["Dienst unter Windows installieren"]({{< relref "service.md#admin_server_service_windows_install" >}})) kann dieser auf verschiedenen Wegen von Hand gestartet werden:

-   Klicken Sie im Startmenü auf **"OpenEstate-ImmoServer → Dienst → ImmoServer-Dienst starten"**.

-   Öffnen Sie den Ordner **`bin`** im [Programm-Verzeichnis]({{< relref "directories.md#admin_server_directories_application" >}}) und starten Sie das Skript **`ServiceStart.bat`** per Doppelklick.

-   Öffnen Sie das bereitgestellte Verwaltungs-Programm für den Dienst und klicken Sie darin auf **"Start"** (siehe ["Dienst unter Windows verwalten"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

-   Öffnen Sie die Dienste-Verwaltung von Windows, wählen Sie den Dienst **"OpenEstate-ImmoServer"** aus und klicken Sie oben links auf **"Den Dienst starten"** bzw. **"Den Dienst neu starten"** (siehe ["Dienst unter Windows verwalten"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

{{< info >}}
Standardmäßig wird der Dienst unter Windows **automatisch gestartet** sobald der Rechner hochgefahren wird. Daher ist es in der Regel nicht nötig den Dienst von Hand zu starten.
{{< /info >}}


#### Dienst unter Windows stoppen {#admin_server_service_windows_stop}

Nachdem der Dienst unter Windows installiert wurde (siehe ["Dienst unter Windows installieren"]({{< relref "service.md#admin_server_service_windows_install" >}})) kann dieser auf verschiedenen Wegen gestoppt werden:

-   Klicken Sie im Startmenü auf **"OpenEstate-ImmoServer → Dienst → ImmoServer-Dienst stoppen"**.

-   Öffnen Sie den Ordner **`bin`** im [Programm-Verzeichnis]({{< relref "directories.md#admin_server_directories_application" >}}) und starten Sie das Skript **`ServiceStop.bat`** per Doppelklick.

-   Öffnen Sie das bereitgestellte Verwaltungs-Programm für den Dienst und klicken Sie darin auf **"Stop"** (siehe ["Dienst unter Windows verwalten"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

-   Öffnen Sie die Dienste-Verwaltung von Windows, wählen Sie den Dienst **"OpenEstate-ImmoServer"** aus und klicken Sie oben links auf **"Den Dienst stoppen"** (siehe ["Dienst unter Windows verwalten"]({{< relref "service.md#admin_server_service_windows_manage" >}})).


### Dienst unter macOS einrichten {#admin_server_service_mac}

Unter macOS wird der Dienst mit Hilfe der vom Betriebssystem bereitgestellten Software [launchd](https://de.wikipedia.org/wiki/Launchd) betrieben. Es wird dafür im Verzeichnis **`/Library/LaunchDaemons`** eine Datei namens **`org.openestate.tool.server.service.plist`** hinterlegt.

{{< info >}}
Bei Bedarf können Sie die Service-Datei selbst bearbeiten um individuelle Anpassungen vorzunehmen (siehe [Tutorial zu launchd](http://www.launchd.info/)). In der Regel sollte dies aber nicht nötig sein.
{{< /info >}}


#### Dienst unter macOS installieren {#admin_server_service_mac_install}

Öffnen Sie das Programm-Symbol **"OpenEstate-ImmoServer"** und starten Sie im darauf dargestellten Finder das Programm **"ServiceInstall"**. Es öffnet sich daraufhin ein Terminal, welches die Installation des Dienstes durchführt.

{{< figure src="service_linux_install_settings.png" caption="Installation des Dienstes unter macOS" >}}

Das Programm benötigt administrative Rechte. Während des Vorgangs werden Sie daher ggf. nach der Eingabe Ihres Passwortes gefragt.

Folgende Optionen können Sie während des Installations-Vorgangs wählen:

-   Sie können einen Benutzer wählen, unter dessen Berechtigungen der Dienst ausgeführt wird.

-   Sie können eine Benutzergruppe, unter deren Berechtigungen der Dienst ausgeführt wird.

-   Sie können bei Bedarf eine automatische Datensicherung aktivieren (siehe ["Automatische Datensicherung unter macOS"]({{< relref "../backup.md#admin_backup_network_live_mac" >}})). Damit die automatische Datensicherung funktioniert, muss zusätzlich die Konfiguration der Manager-Programme angepasst werden (siehe ["Manager-Programme konfigurieren"]({{< relref "setup.md#admin_server_setup_manager" >}})).

Wenn alle Fragen beantwortet wurden, wird der Dienst im Verzeichnis **`/Library/LaunchDaemons`** in der Datei **`org.openestate.tool.server.service.plist`** installiert.

{{< figure src="service_mac_install_summary.png" caption="Zusammenfassung nach Installation des Dienstes unter macOS" >}}

Beim ersten Start des ImmoTool-Servers werden Sie vom Betriebssystem eventuell gefragt, ob eingehende Verbindungen akzeptiert werden sollen. Diese Frage sollte mit **"Erlauben"** beantwortet werden.

{{< figure src="startup_mac_firewall.png" caption="Freigabe in der Firewall unter macOS erteilen" >}}


#### Dienst unter macOS deinstallieren {#admin_server_service_mac_uninstall}

Öffnen Sie das Programm-Symbol **"OpenEstate-ImmoServer"** und starten Sie im darauf dargestellten Finder das Programm **"ServiceUninstall"**. Es öffnet sich daraufhin ein Terminal, welches die Deinstallation des Dienstes durchführt.

Das Programm benötigt administrative Rechte. Während des Vorgangs werden Sie daher ggf. nach der Eingabe Ihres Passwortes gefragt.


#### Dienst unter macOS starten {#admin_server_service_mac_start}

Nachdem der Dienst unter macOS installiert wurde (siehe ["Dienst unter macOS installieren"]({{< relref "service.md#admin_server_service_mac_install" >}})) kann dieser auf verschiedenen Wegen von Hand gestartet werden:

-   Öffnen Sie das Programm-Symbol **"OpenEstate-ImmoServer"** und starten Sie im darauf dargestellten Finder das Programm **"ServiceStart"**.

-   Öffnen Sie das Terminal und führen Sie den folgenden Befehl aus:

    ```bash
    sudo launchctl start org.openestate.tool.server.service
    ```

{{< info >}}
Standardmäßig wird der Dienst unter macOS **automatisch gestartet** sobald der Rechner hochgefahren wird. Daher ist es in der Regel nicht nötig den Dienst von Hand zu starten.
{{< /info >}}


#### Dienst unter macOS beenden {#admin_server_service_mac_stop}

Nachdem der Dienst unter macOS installiert wurde (siehe ["Dienst unter macOS installieren"]({{< relref "service.md#admin_server_service_mac_install" >}})) kann dieser auf verschiedenen Wegen gestoppt werden:

-   Öffnen Sie das Programm-Symbol **"OpenEstate-ImmoServer"** und starten Sie im darauf dargestellten Finder das Programm **"ServiceStop"**.

-   Öffnen Sie das Terminal und führen Sie den folgenden Befehl aus:

    ```bash
    sudo launchctl stop org.openestate.tool.server.service
    ```


### Dienst unter Linux einrichten {#admin_server_service_linux}

Unter Linux wird der Dienst mit Hilfe der vom Betriebssystem bereitgestellten Software [systemd](https://de.wikipedia.org/wiki/Systemd) betrieben. Es wird dafür im Verzeichnis **`/etc/systemd/system`** eine Datei namens **`openestate-immoserver.service`** hinterlegt.

{{< warning >}}
Die meisten aktuellen Linux-Distributionen nutzen die Software "systemd". Prüfen Sie jedoch sicherheitshalber vor der Installation des Dienstes ob Ihr Betriebssystem tatsächlich diese Software nutzt.
{{< /warning >}}

{{< info >}}
Bei Bedarf können Sie die Service-Datei selbst bearbeiten um individuelle Anpassungen vorzunehmen (siehe [Handbuch zu systemd](https://www.freedesktop.org/software/systemd/man/systemd.service.html)). In der Regel sollte dies aber nicht nötig sein.
{{< /info >}}


#### Dienst unter Linux installieren {#admin_server_service_linux_install}

Wenn der ImmoTool-Server über das [**Debian**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) installiert wurde, ist auf Ihrem Betriebssystem bereits der Dienst installiert worden. In diesem Falle sind **keine weiteren Schritte** zur Installation des Dienstes nötig.

Falls der ImmoTool-Server über das [**TAR.GZ**-Installationspaket]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}}) installiert wurde, starten Sie im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) das Skript **`ServiceInstall.sh`**.

{{< figure src="service_linux_install_settings.png" caption="Installation des Dienstes unter Linux" >}} 

Das Programm benötigt administrative Rechte. Während des Vorgangs werden Sie daher ggf. nach der Eingabe Ihres Passwortes gefragt.

Folgende Optionen können Sie während des Installations-Vorgangs wählen:

-   Sie können einen Benutzer wählen, unter dessen Berechtigungen der Dienst ausgeführt wird.

-   Sie können eine Benutzergruppe, unter deren Berechtigungen der Dienst ausgeführt wird.

-   Sie können bei Bedarf eine automatische Datensicherung aktivieren (siehe ["Automatische Datensicherung unter Linux"]({{< relref "../backup.md#admin_backup_network_live_linux" >}})). Damit die automatische Datensicherung funktioniert, muss zusätzlich die Konfiguration der Manager-Programme angepasst werden (siehe ["Manager-Programme konfigurieren"]({{< relref "setup.md#admin_server_setup_manager" >}})).

Wenn alle Fragen beantwortet wurden, wird der Dienst im Verzeichnis **`/etc/systemd/system`** in der Datei **`openestate-immoserver.service`** installiert.

{{< figure src="service_linux_install_summary.png" caption="Zusammenfassung nach Installation des Dienstes unter Linux" >}}


#### Dienst unter Linux deinstallieren {#admin_server_service_linux_uninstall}

Starten Sie im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) das Skript **`ServiceUninstall.sh`**.

Das Programm benötigt administrative Rechte. Während des Vorgangs werden Sie daher nach der Eingabe Ihres Passwortes gefragt.


#### Dienst unter Linux starten {#admin_server_service_linux_start}

Nachdem der Dienst unter Linux installiert wurde (siehe ["Dienst unter Linux installieren"]({{< relref "service.md#admin_server_service_linux_install" >}})) kann dieser auf verschiedenen Wegen von Hand gestartet werden:

-   Starten Sie im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) das Skript **`ServiceStart.sh`**.

-   Öffnen Sie eine Konsole und führen Sie den folgenden Befehl aus:

    ```bash
    sudo systemctl start openestate-immoserver
    ```

{{< info >}}
Standardmäßig wird der Dienst unter Linux **automatisch gestartet** sobald der Rechner hochgefahren wird. Daher ist es in der Regel nicht nötig den Dienst von Hand zu starten.
{{< /info >}}


#### Dienst unter Linux stoppen {#admin_server_service_linux_stop}

Nachdem der Dienst unter Linux installiert wurde (siehe ["Dienst unter Linux installieren"]({{< relref "service.md#admin_server_service_linux_install" >}})) kann dieser auf verschiedenen Wegen gestoppt werden:

-   Starten Sie im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "directories.md#admin_server_directories_application" >}}) das Skript **`ServiceStop.sh`**.

-   Öffnen Sie eine Konsole und führen Sie den folgenden Befehl aus:

    ```bash
    sudo systemctl stop openestate-immoserver
    ```
