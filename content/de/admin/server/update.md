---

title: ImmoTool-Server aktualisieren
linktitle: Aktualisierung
description: Wie OpenEstate-ImmoServer aktualisiert werden kann…
weight: 50

menu:
  main:
    parent: admin-server
    identifier: admin-server-update

---

## ImmoTool-Server aktualisieren {#admin_server_update}

Weitaus seltener als beim ImmoTool werden Aktualisierungen für den ImmoTool-Server veröffentlicht. Im Unterschied zum ImmoTool findet **keine automatische Prüfung auf Aktualisierungen** statt. Sie sollten daher gelegentlich die [Webseite des OpenEstate-Projekts](https://openestate.org/) besuchen oder den [RSS-Feed](https://openestate.org/news/feed/de/rss/) abonnieren um über Aktualisierungen informiert zu werden.

Laden Sie das Installationspaket für Ihr Betriebssystem herunter und starten Sie den Installationsvorgang (siehe ["ImmoTool-Server installieren"]({{< relref "../../intro/install_server.md#intro_install_server" >}})). Beachten Sie dabei die folgenden Anmerkungen für Ihr Betriebssystem.

{{< warning >}}
Sollte der ImmoTool-Server aktuell gestartet sein, sollten Sie diesen vor der Aktualisierung beenden / stoppen.
{{< /warning >}}

{{< tip >}}
Um einen Datenverlust im Falle eines Fehlers zu vermeiden, empfehlen wir das [Daten-Verzeichnis]({{< relref "directories.md#admin_server_directories_data" >}}) des ImmoTool-Servers vor der Aktualisierung zu sichern.
{{< /tip >}}


### Aktualisierung unter Windows {#admin_server_update_windows}

Das **EXE**-Installationsprogramm erkennt automatisch den Speicherort der ImmoTool-Server-Installation und führt die Aktualisierung für Sie durch.

{{< warning >}}
Sollten Sie Anpassungen im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) vorgenommen, sichern Sie die betreffende Dateien vor der Aktualisierung. Nach der Aktualisierung können Sie die betreffenden Dateien wieder zurück kopieren.
{{< /warning >}}


### Aktualisierung unter macOS {#admin_server_update_mac}

Verschieben Sie den Programm-Starter **"OpenEstate-ImmoServer"** an die gleiche Stelle, wo sich die alte Installation des ImmoTool-Servers befindet. Es erscheint eine Rückfrage, ob die bestehende Installation überschrieben werden soll:

{{< figure src="update_mac.png" caption="Rückfrage zur Aktualisierung unter macOS" >}}

Bestätigen Sie die Rückfrage in diesem Dialogfenster durch Klick auf **"Ersetzen"**.


### Aktualisierung unter Debian, Ubuntu & Co. {#admin_server_update_debian}

Wenn Sie das Debian-Repository in Ihrem Betriebssystem eingerichtet haben (siehe ["Pakete aus Debian-Repository beziehen"]({{< relref "../../intro/download.md#intro_download_debian" >}})), müssen Sie das Programm **nicht** von der OpenEstate-Webseite herunterladen. Statt dessen genügt es folgende Befehle im Terminal auszuführen:

```bash
sudo apt update
sudo apt install openestate-immoserver
```

Wenn Sie das Debian-Repository **nicht** nutzen aber das [**Debian**-Paket]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) bei der Installation verwendet haben, können Sie die **DEB**-Installationsdatei herunterladen und per Doppelklick starten. Alternativ kann die Datei über folgenden Befehl im Terminal installiert werden:

```bash
sudo dpkg -i openestate-immoserver_x.y.z_amd64.deb
```

Wobei **`x.y.z`** durch die jeweilige Versions-Nummer zu ersetzen ist.

{{< warning >}}
Sollten Sie Anpassungen im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) vorgenommen, sichern Sie die betreffende Dateien vor der Aktualisierung. Nach der Aktualisierung können Sie die betreffenden Dateien wieder zurück kopieren.
{{< /warning >}}


### Aktualisierung unter Linux {#admin_server_update_linux}

1.  Bringen Sie in Erfahrung in welchem Verzeichnis der ImmoTool-Server installiert wurde.
2.  Laden Sie die **TAR.GZ**-Installationsdatei für Linux herunter und entpacken Sie die Datei auf Ihrem Rechner. 
3.  Benennen Sie das in Schritt 1 ermittelte Programmverzeichnis des ImmoTool-Servers um - z.B. in **`OpenEstate-ImmoServer-ALT`**.
4.  Erzeugen Sie ein neues / leeres Verzeichnis unter dem in Schritt 1 festgestellten Namen - z.B. **`OpenEstate-ImmoServer`**.
5.  Kopieren Sie die in Schritt 2 entpackten Dateien in das neue / leere Programmverzeichnis.

Nachdem das Programm in der neuen Version erfolgreich gestartet werden konnte, kann das in Schritt 3 erzeugte alte Programmverzeichnis bei Bedarf gelöscht werden.

{{< warning >}}
Sollten Sie Anpassungen im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) vorgenommen, sichern Sie die betreffende Dateien vor der Aktualisierung. Nach der Aktualisierung können Sie die betreffenden Dateien wieder zurück kopieren.
{{< /warning >}}


### Wichtige Hinweise für bestimmte Versionen {#admin_server_update_advices}

Für den Umstieg auf verschiedene Versionen kann es eventuell besondere Hinweise geben. Diese werden im Folgenden dokumentiert.


#### Umstieg von Version 1.0-beta auf 1.x {#admin_server_update_advices_beta}

Mit der Umstellung von ImmoTool-Server 1.0-beta auf Version 1.0.0 gab es einige grundlegende Änderungen, die bei einer Aktualisierung zu beachten sind.


##### Neue Verzeichnisse {#admin_server_update_advices_beta_directories}

Im Unterschied zur 1.0-beta Version speichert der ImmoTool-Server die Datenbanken nicht mehr im Programmverzeichnis. Bevor das Programmverzeichnis des alten ImmoTool-Servers gelöscht wird, sollten Sie **unbedingt den Inhalt des Ordners `var/data` sichern**.

Nachdem die neue Version des ImmoTool-Servers installiert wurde, starten Sie das Programm testweise und beenden Sie das Programm sofort wieder. Es wird dadurch das neue [Daten-Verzeichnis]({{< relref "directories.md#admin_server_directories_data" >}}) erstellt. Öffnen Sie dieses Verzeichnis und kopieren Sie den Inhalt des zuvor gesicherten **`var/data`** Ordners in den neu erstellten Unterordner **`data`** des [Daten-Verzeichnisses]({{< relref "directories.md#admin_server_directories_data" >}}).

Der bereits vorhandene Ordner **`data`** sollte dabei nicht überschrieben sondern vorher gelöscht (oder umbenannt) werden.

Bei zukünftigen Aktualisierungen von ImmoTool-Server 1.x sind diese Schritte nicht mehr nötig.


##### Neuer Mechanismus für Dienste {#admin_server_update_advices_beta_services}

Die Einrichtung der Dienste wurde mit ImmoTool-Server 1.0.0 grundlegend überarbeitet. Sollten Sie einen Dienst für den ImmoTool-Server eingerichtet haben, sollten Sie **vor der Aktualisierung den Dienst aus dem Betriebssystem entfernen**. Führen Sie dafür im **`bin`** Verzeichnis des alten ImmoTool-Servers die Datei **`ServiceUninstall.bat`** bzw. **`ServiceUninstall.sh`** aus.

Nachdem die neue Version des ImmoTool-Servers installiert wurde kann der Dienst neu eingerichtet werden (siehe ["ImmoTool-Server als Dienst einrichten"]({{< relref "service.md#admin_server_service" >}})).

Bei zukünftigen Aktualisierungen von ImmoTool-Server 1.x sind diese Schritte nicht mehr nötig.


##### Neue Installationsroutine für Windows & macOS {#admin_server_update_advices_beta_installer}

Für **Windows** und **macOS** gibt es eine **neue Installationsroutine** (EXE und DMG Installationspakete). Die neuen Installationspakete sind nicht kompatibel mit der alten Vorgehensweise. Beachten Sie daher, dass Sie die alte Version des ImmoTool-Servers (1.0-beta) bei der Installation **nicht überschreiben**. Wir empfehlen die folgende Vorgehensweise:

-   Prüfen Sie, wo ImmoTool-Server 1.0-beta auf der Festplatte installiert wurde. 

    -   Sollte sich das Programm unter Windows im Ordner **`C:\Programme\OpenEstate-ImmoServer`** befinden, benennen Sie diesen Ordner um - z.B. in **`C:\Programme\OpenEstate-ImmoServer-ALT`**.
    
    -   Unter macOS sollte es keine Probleme mit der Benennung geben. Ermitteln Sie hier dennoch den Installationsordner des Programms.
    
-   Entfernen Sie unter Windows eventuell erstellte Verknüpfungen (auf dem Desktop oder im Startmenü). Unter macOS können Sie eventuell vorhandene Verknüpfungen aus dem Dock entfernen.

-   Führen Sie eine Neuinstallation durch (siehe ["ImmoTool-Server installieren"]({{< relref "../../intro/install_server.md#intro_install_server" >}})).

-   Wenn das Programm in der neuen Version erfolgreich in Betrieb genommen und die Datenbank übernommen wurde (siehe ["Neue Verzeichnisse"]({{< relref "update.md#admin_server_update_advices_beta_directories" >}})), kann der Installationsordner von ImmoTool-Server 1.0-beta entfernt werden.

Bei zukünftigen Aktualisierungen unter Windows und macOS sind diese Schritte nicht mehr nötig.


##### Java kann entfernt werden {#admin_server_update_advices_beta_java}

Im Installationspaket des ImmoTool-Servers ist nun Java enthalten. Wenn Sie auf Ihrem Betriebssystem Java nicht anderweitig benötigen, können Sie nach der erfolgreichen Umstellung auf ImmoTool-Server 1.x **Java im Betriebssystem deinstallieren**.

-   Unter Windows können Sie dafür die Systemsteuerung öffnen und im Bereich zur Deinstallation von Software **"Oracle Java"** entsprechend entfernen.

-   Unter macOS können Sie **"Oracle Java"** wie folgt entfernen:

    1.  Klicken Sie im Dock auf das **"Finder"**-Symbol.
    2.  Klicken Sie im Suchmenü auf **"Los"**.
    3.  Klicken Sie auf **"Dienstprogramme"**.
    4.  Doppelklicken Sie auf das **"Terminal"**-Symbol.
    5.  Kopieren und fügen Sie die folgenden Befehle im Terminalfenster ein:
    
        ```bash
        sudo rm -fr /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin
        sudo rm -fr /Library/PreferencePanes/JavaControlPanel.prefPane
        sudo rm -fr ~/Library/Application\ Support/Oracle/Java
        ```

    (zitiert aus der [offiziellen Anleitung von Oracle](https://www.java.com/de/download/help/mac_uninstall_java.xml))

-   Unter Linux können Sie entweder **"OpenJDK"** über das Paketsystem des Betriebssystems entfernen. Oder falls Sie **"Oracle Java"** installiert haben kann der verwendete Installationsordner entfernt werden. 
