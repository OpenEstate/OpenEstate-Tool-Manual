---

title: ImmoTool installieren 
linktitle: ImmoTool installieren
description: OpenEstate-ImmoTool an einem Arbeitsplatz installieren…
weight: 50

menu:
  main:
    parent: intro
    identifier: intro-install-client

---

## ImmoTool installieren {#intro_install_client}


### Programmpaket installieren {#intro_install_client_setup}

Laden Sie die zu Ihrem Betriebssystem passende Installationsdatei für das ImmoTool aus dem [Download-Bereich](https://openestate.org/downloads/openestate-immotool) herunter (siehe ["Programme herunterladen"]({{< relref "download.md#intro_download" >}})).


#### Installation unter Windows {#intro_install_client_setup_windows}

Laden Sie die zu Ihrem Windows passende **EXE**-Installationsdatei herunter. Unter einem 64bit-Windows sollte möglichst auch die 64bit-Installationsdatei verwendet werden.

Öffnen Sie die heruntergeladene EXE-Datei mit einem Doppelklick. Es startet daraufhin ein Installationsprogramm, welches Sie durch die weiteren Schritte der Installation leitet.

{{< figure src="install_client_windows.png" caption="Installation des ImmoTools unter Windows" >}}


#### Installation unter macOS {#intro_install_client_setup_mac}

Laden Sie die **DMG**-Installationsdatei herunter und öffnen Sie die Datei durch einen Doppelklick. Es öffnet sich daraufhin ein Fenster, über welches das Programm installiert werden kann.

Ziehen Sie mit der Maus das ImmoTool Programmsymbol in den Programmordner. Alternativ können Sie das Programmsymbol auch auf die Arbeitsfläche oder an eine andere beliebige Stelle auf Ihrer Festplatte ziehen.  

{{< figure src="install_client_mac.jpg" caption="Installation des ImmoTools unter macOS" >}}


#### Installation unter Debian, Ubuntu & Co. {#intro_install_client_setup_debian}

Wenn Sie eine Debian-basierte Linux-Distribution nutzen (z.B. **Debian**, **Ubuntu** oder **Linux Mint**), empfehlen wir die Nutzung des Repositories (siehe ["Pakete aus Debian-Repository beziehen"]({{< relref "download.md#intro_download_debian" >}})). Nachdem das Repository erfolgreich eingerichtet wurde, kann das Programm über folgende Befehle installiert werden:

1.  Abruf der Paketliste:
    
    ```bash
    sudo apt update
    ```
    
2.  Installation des ImmoTools:

    ```bash
    sudo apt install openestate-immotool
    ```

Sollten Sie das Repository nicht nutzen wollen, können Sie *alternativ* die **DEB**-Installationsdatei herunterladen und per Doppelklick oder durch folgenden Befehl installieren:

```bash
sudo dpkg -i openestate-immotool_x.y.z_amd64.deb
```

Wobei `x.y.z` durch die jeweilige Versions-Nummer zu ersetzen ist.

{{< info >}}
Bei der Installation des Debian-Pakets wird das Programm im Verzeichnis `/opt/OpenEstate-ImmoTool` installiert.
{{< /info >}}

{{< info >}}
Bei der Installation des Debian-Pakets werden automatisch die nötigen Einträge im Startmenü für alle Benutzer des Betriebssystems erzeugt.
{{< /info >}}


#### Installation unter Linux {#intro_install_client_setup_linux} 

Wenn Sie keine Debian-basierte Linux-Distribution nutzen oder das Repository nicht einbinden wollen, können Sie alternativ die **TAR.GZ**-Installationsdatei herunterladen. 

Nachdem Sie diese Datei auf Ihrem Rechner entpackt haben, finden Sie einen Ordner namens `OpenEstate-ImmoTool`. Verschieben Sie diesen Ordner an eine Stelle Ihrer Wahl (z.B. ins Benutzerverzeichnis oder nach `/opt/OpenEstate-ImmoTool`).

{{< tip >}}
Bei Bedarf können Sie im Verzeichnis `bin` das Skript `StartMenuAdd.sh` ausführen. Es werden dadurch die Startmenü-Einträge des Programms für den aktuell angemeldeten Benutzer erzeugt.
{{< /tip >}} 


### ImmoTool starten {#intro_install_client_startup}


#### ImmoTool unter Windows starten {#intro_install_client_startup_windows}

Bei der Installation unter Windows wird automatisch eine Verknüpfung auf dem Desktop erzeugt, über die das Programm gestartet werden kann. Alternativ finden Sie im Startmenü einen Ordner namens **"OpenEstate-ImmoTool"** mit verschiedenen Verknüpfungen.

Darüber hinaus können Sie das Programm auch über die Datei `ImmoTool.exe` / `ImmoTool.bat` im Verzeichnis `bin` des Programm-Verzeichnisses starten.


#### ImmoTool unter macOS starten {#intro_install_client_startup_mac}

Führen Sie einen Doppelklick auf das Programmsymbol mit der Bezeichnung **"OpenEstate-ImmoTool"** aus. Es öffnet sich daraufhin der Finder mit den vom ImmoTool bereitgestellten Programmen.

{{< figure src="../admin/client/startup_mac.png" caption="Starter für ImmoTool im Finder" >}}

Wenn Sie in diesem Fenster auf das **ImmoTool**-Symbol klicken, wird das Programm gestartet.

{{< tip >}}
Bei Bedarf können Sie das ImmoTool-Symbol ins Dock integrieren, um das Programm später schnell und unkompliziert starten zu können (siehe ["Anleitung bei Apple"](https://support.apple.com/de-de/HT201730)).
{{< /tip >}}


#### ImmoTool unter Linux starten {#intro_install_client_startup_linux}

Wenn das ImmoTool mit dem [**Debian**-Paket]({{< relref "install_client.md#intro_install_client_setup_debian" >}}) installiert wurde, finden Sie im Startmenü die Einträge für den Start des Programms.

Wenn das ImmoTool mit dem [**TAR.GZ**-Paket]({{< relref "install_client.md#intro_install_client_setup_linux" >}}) installiert wurde, müssen Sie ggf. vorher noch die Datei `StartMenuAdd.sh` im `bin`-Verzeichnis des Programms ausführen um die Einträge im Startmenü zu erzeugen.

Alternativ zum Startmenü kann das Programm über die Datei `ImmoTool.sh` im `bin`-Verzeichnis des Programms gestartet werden.


### Sprache wählen

Beim ersten Programmstart prüft das ImmoTool ob eine Übersetzung zu der im Betriebssystem eingestellten Sprache vorliegt. Sollte dies nicht der Fall sein, erscheint das folgende Fenster, in dem Sie die im ImmoTool verwendete Sprache auswählen können:

{{< figure src="install_client_language.png" caption="Auswahl der Sprache beim ersten Programmstart" >}}

Es werden hier nur Sprachen zur Auswahl gestellt, für die aktuell eine Übersetzung vorliegt und für die ein Sprachpaket im Programm enthalten ist.

{{< info >}}
Das ImmoTool kann in beliebige Sprachen übersetzt werden. Wenn Sie sich an der Übersetzungsarbeit beteiligen möchten (z.B. weitere Sprachen ergänzen oder bestehende Übersetzungen korrigieren), finden Sie dazu weitere Informationen auf der [Webseite des OpenEstate-Projekts](https://openestate.org/immotool/translations).
{{< /info >}}


### Einzelplatz-Projekt erzeugen

Der Projektassistent wird geöffnet und Sie können eine Datenbank für Ihre Arbeit mit dem ImmoTool erzeugen.

{{< warning >}}
Wenn Sie eine **Netzwerk-Installation** durchführen möchten (siehe ["Betrieb an mehreren Arbeitsplätzen"]({{< relref "install_types.md#intro_install_types_network" >}})), folgen Sie bitte den Hinweisen im Kapitel ["ImmoTool-Server installieren"]({{< relref "install_server.md#intro_install_server" >}}). Ein Einzelplatz-Projekt muss in diesem Falle **nicht** erzeugt werden.
{{< /warning >}}

{{< figure src="install_client_project.png" caption="Einzelplatz-Projekt beim ersten Programmstart erzeugen" >}}

Folgende Einstellungen sind im Projektassistenten zur Erstellung eines Einzelplatz-Projekts vorzunehmen:

-   **Projekt-Name:** \
    Tragen Sie einen beliebigen Namen für das Projekt ein.

-   **Projekt-Art:** \
    Wählen Sie **"Neues Einzelplatz-Projekt erzeugen."** aus.

-   Bei Bedarf können Sie im Tab **"Firma"** noch weitere Angaben zu Ihrem Unternehmen hinterlegen.

-   Bei Bedarf können im Tab **"Add-Ons"** einzelne Erweiterungen von der Installation ausgeschlossen werden.

Nachdem die Lizenzbedingungen bestätigt wurden kann das Projekt durch Klick auf **"Projekt erzeugen"** erzeugt werden. Das erstellte Projekt wird danach automatisch geöffnet.

Ab sofort können Sie mit dem Programm arbeiten. Wir wünschen viel Spaß und Erfolg!
