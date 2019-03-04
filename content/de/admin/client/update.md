---

title: ImmoTool aktualisieren
linktitle: Aktualisierung
description: Wie OpenEstate-ImmoTool aktualisiert werden kann…
weight: 30

menu:
  main:
    parent: admin-client
    identifier: admin-client-update

---

## ImmoTool aktualisieren {#admin_client_update}

Einmal am Tag prüft das ImmoTool beim ersten Programmstart automatisch ob Aktualisierungen vorliegen. Im Falle, dass Aktualisierungen vorhanden sind, wird eine Information dargestellt.

{{< figure src="update_notification.png" caption="Information über eine verfügbare Aktualisierung" >}}

Bei Klick auf **"Installationspaket herunterladen."** wird im Web-Browser der Link zum Download des Installationspakets für das verwendete Betriebssystem geöffnet.

Bei Klick auf **"Webseite mit Downloads."** wird im Web-Browser der [Download-Bereich](https://openestate.org/downloads/openestate-immotool) auf der Webseite von OpenEstate.org mit der aktuellen Programm-Version geöffnet.

Laden Sie das Installationspaket für Ihr Betriebssystem herunter und starten Sie den Installationsvorgang (siehe ["ImmoTool installieren"]({{< relref "../../intro/install_client.md#intro_install_client" >}})). Beachten Sie dabei die folgenden Anmerkungen für Ihr Betriebssystem.

{{< warning >}}
Beenden Sie das ImmoTool bevor die Aktualisierung durchgeführt wird.
{{< /warning >}}

{{< info >}}
Wenn ImmoTool in einer Netzwerk-Installation betrieben wird (siehe ["Betrieb an mehreren Arbeitsplätzen"]({{< relref "../../intro/install_types.md#intro_install_types_network" >}})), sollten die ImmoTool-Installationen **bei allen Arbeitsplätzen** aktualisiert werden. Es kann Situationen geben, in denen unterschiedliche ImmoTool-Versionen nicht gemeinsam im Netzwerk genutzt werden können. 
{{< /info >}}


### Aktualisierung unter Windows {#admin_client_update_windows}

Das **EXE**-Installationsprogramm erkennt automatisch den Speicherort der ImmoTool-Installation und führt die Aktualisierung für Sie durch.


### Aktualisierung unter macOS {#admin_client_update_mac}

Verschieben Sie den Programm-Starter **"OpenEstate-ImmoTool"** an die gleiche Stelle, wo sich die alte ImmoTool-Installation befindet. Es erscheint eine Rückfrage, ob die bestehende Installation überschrieben werden soll:

{{< figure src="update_mac.png" caption="Rückfrage zur Aktualisierung unter macOS" >}}

Bestätigen Sie die Rückfrage in diesem Dialogfenster durch Klick auf **"Ersetzen"**.


### Aktualisierung unter Debian, Ubuntu & Co. {#admin_client_update_debian}

Wenn Sie das Debian-Repository in Ihrem Betriebssystem eingerichtet haben (siehe ["Pakete aus Debian-Repository beziehen"]({{< relref "../../intro/download.md#intro_download_debian" >}})), müssen Sie das Programm **nicht** von der OpenEstate-Webseite herunterladen. Statt dessen genügt es folgende Befehle in der Konsole auszuführen:

```bash
sudo apt update
sudo apt install openestate-immotool
```

Wenn Sie das Debian-Repository **nicht** nutzen aber das [**Debian**-Paket]({{< relref "../../intro/install_client.md#intro_install_client_setup_debian" >}}) bei der Installation verwendet haben, können Sie die **DEB**-Installationsdatei herunterladen und per Doppelklick starten. Alternativ kann die Datei über folgenden Befehl in der Konsole installiert werden:

```bash
sudo dpkg -i openestate-immotool_x.y.z_amd64.deb
```

Wobei **`x.y.z`** durch die jeweilige Versions-Nummer zu ersetzen ist.


### Aktualisierung unter Linux {#admin_client_update_linux}

1.  Bringen Sie in Erfahrung in welchem Verzeichnis ImmoTool installiert wurde.
2.  Laden Sie die **TAR.GZ**-Installationsdatei für Linux herunter und entpacken Sie die Datei auf Ihrem Rechner. 
3.  Benennen Sie das in Schritt 1 ermittelte Programmverzeichnis des ImmoTools um - z.B. in **`OpenEstate-ImmoTool-ALT`**.
4.  Erzeugen Sie ein neues / leeres Verzeichnis unter dem in Schritt 1 festgestellten Namen - z.B. **`OpenEstate-ImmoTool`**.
5.  Kopieren Sie die in Schritt 2 entpackten Dateien in das neue / leere Programmverzeichnis.

Nachdem das Programm in der neuen Version erfolgreich gestartet werden konnte, kann das in Schritt 3 erzeugte alte Programmverzeichnis bei Bedarf gelöscht werden.


### Wichtige Hinweise für bestimmte Versionen {#admin_client_update_advices}

Für den Umstieg auf verschiedene Versionen kann es eventuell besondere Hinweise geben. Diese werden im Folgenden dokumentiert.


#### Umstieg von Version 1.0-beta auf 1.x {#admin_client_update_advices_from_beta}

Mit der Umstellung von ImmoTool 1.0-beta auf Version 1.0.0 gab es einige grundlegende Änderungen, die bei einer Aktualisierung zu beachten sind.


##### Neue Installationsroutine für Windows & macOS {#admin_client_update_advices_from_beta_installer}

Für **Windows** und **macOS** gibt es eine **neue Installationsroutine** (EXE und DMG Installationspakete). Die neuen Installationspakete sind nicht kompatibel mit der alten Vorgehensweise. Beachten Sie daher, dass Sie die alte ImmoTool-Version (1.0-beta) bei der Installation **nicht überschreiben**. Wir empfehlen die folgende Vorgehensweise:

-   Prüfen Sie, wo das ImmoTool auf der Festplatte installiert wurde. 

    -   Sollte sich das Programm unter Windows im Ordner **`C:\Programme\OpenEstate-ImmoTool`** befinden, benennen Sie diesen Ordner um - z.B. in **`C:\Programme\OpenEstate-ImmoTool-ALT`**.
    
    -   Unter macOS sollte es keine Probleme mit der Benennung geben. Ermitteln Sie hier dennoch den Installationsordner des Programms.
    
-   Entfernen Sie unter Windows eventuell erstellte Verknüpfungen (auf dem Desktop oder im Startmenü). Unter macOS können Sie eventuell vorhandene Verknüpfungen aus dem Dock entfernen.

-   Führen Sie eine Neuinstallation durch (siehe ["ImmoTool installieren"]({{< relref "../../intro/install_client.md#intro_install_client" >}})).

-   Wenn das Programm erfolgreich installiert wurde und gestartet werden kann, kann der Installationsordner von ImmoTool 1.0-beta entfernt werden.

Bei zukünftigen Aktualisierungen unter Windows und macOS sind diese Schritte nicht mehr nötig. 


##### Java kann entfernt werden {#admin_client_update_advices_from_beta_java}

Im Installationspaket des ImmoTools ist nun Java enthalten. Wenn Sie auf Ihrem Betriebssystem Java nicht anderweitig benötigen, können Sie nach der erfolgreichen Umstellung auf ImmoTool 1.x **Java im Betriebssystem deinstallieren**.

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


#### Umstieg von Version 0.9.x auf 1.x {#admin_client_update_advices_from_0_9}

Für den Umstieg von ImmoTool 0.9.x auf 1.x gelten die gleichen Hinweise, wie beim [Umstieg von 1.0-beta auf 1.x]({{< relref "update.md#admin_client_update_advices_from_beta" >}}). Hier kann jedoch die Datenbank nicht automatisch übernommen werden. Beachten Sie daher ebenfalls die [Anleitung zur Migration des Projekts in ImmoTool 1.x]({{< relref "../migration.md#admin_migration_legacy" >}}).  
