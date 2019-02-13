---

title: Installation am Arbeitsplatz
linktitle: Lokale Installation
description: OpenEstate-ImmoTool an einem Arbeitsplatz installieren…
weight: 50

menu:
  main:
    parent: intro
    identifier: intro-install-local

---

## ImmoTool als Einzelplatz-Version installieren {#intro_install_local}


### Was ist eine Einzelplatz-Installation? {#intro_install_local_info}

Bei einer Einzelplatz-Installation stellt das ImmoTool selbst alle nötigen Funktionen bereit. Der ImmoTool-Server muss in diesem Falle **nicht** installiert werden.

Beim Programmstart wird automatisch eine Datenbank auf dem Rechner des Anwenders erstellt, in der alle erfassten Daten (Immobilien, Kunden, etc.) gespeichert werden.

---

> **Hinweis*
>
> Wenn Sie ImmoTool mit mehreren Mitarbeitern nutzen wollen, führen Sie bitte statt dessen eine [Netzwerk-Installation]({{< relref "install_network.md#intro_install_network" >}}) durch.


#### Vorteile einer Einzelplatz-Installation {#intro_install_local_pro}

-   Dies ist die einfachst mögliche Form das ImmoTool in Betrieb zu nehmen, da nur ein einziges Programm installiert und gestartet werden muss.
-   Beim ersten Programmstart wird automatisch die Datenbank auf der Festplatte erzeugt und man kann sofort und ohne weiteren Aufwand mit der Arbeit beginnen.

---

> [**Hinweis**]{.info}
>
> Wenn Sie sich erst mal mit den Funktionen des ImmoTools vertraut machen möchten, ist eine Einzelplatz-Installation wegen der unkomplizierten Installation die beste Wahl. Im späteren Verlauf kann eine Einzelplatz-Installation jederzeit in eine Netzwerk-Installation umgewandelt werden (siehe [Einzelplatz- in Mehrplatz-Projekt umwandeln]({{< relref "../admin/migration.md#admin_migration_project_local" >}})).


#### Nachteile einer Einzelplatz-Installation {#intro_install_local_contra}

-   Die Datenbank einer Einzelplatz-Installation kann nicht von mehreren Mitarbeitern gleichzeitig geöffnet werden.
-   Es gibt keine Möglichkeiten zur Vergabe von Berechtigungen für verschiedene Mitarbeiter. Bei einer Einzelplatz-Installation hat man grundsätzlich immer alle Berechtigungen.


### Programmpaket installieren {#intro_install_local_download}

Laden Sie die zu Ihrem Betriebssystem passende Installationsdatei für das ImmoTool aus dem [Download-Bereich](https://openestate.org/downloads/openestate-immotool) herunter (siehe [Programme herunterladen]({{< relref "download.md#intro_download" >}})).


#### Installation unter Windows {#intro_install_local_windows}

Laden Sie die zu Ihrem Windows passende **EXE**-Installationsdatei herunter. Unter einem 64bit-Windows sollte möglichst auch die 64bit-Installationsdatei verwendet werden.

Öffnen Sie die heruntergeladene EXE-Datei mit einem Doppelklick. Es startet daraufhin ein Installationsprogramm, welches Sie durch die weiteren Schritte der Installation leitet.

{{< figure src="install_local_windows.jpg" caption="Installationsprogramm unter Windows" >}}


#### Installation unter macOS {#intro_install_local_mac}

Laden Sie die **DMG**-Installationsdatei herunter und öffnen Sie die Datei durch einen Doppelklick. Es öffnet sich daraufhin ein Fenster, über welches das Programm installiert werden kann.

Ziehen Sie mit der Maus das ImmoTool-Programmsymbol in den Programmordner. Alternativ können Sie das Programmsymbol auch auf die Arbeitsfläche oder an eine andere beliebige Stelle auf Ihrer Festplatte ziehen.  


#### Installation unter Debian, Ubuntu & Co. {#intro_install_local_debian}

Wenn Sie eine Debian-basierte Linux-Distribution nutzen (z.B. **Debian**, **Ubuntu** oder **Linux Mint**), empfehlen wir die Nutzung des Repositories (siehe [Pakete aus Debian-Repository beziehen]({{< relref "download.md#intro_download_debian" >}})). Nachdem das Repository erfolgreich eingerichtet wurde, kann das Programm über folgende Befehle installiert werden:

1.  Abruf der Paketliste:
    
    ```bash
    sudo apt update
    ```
    
2.  Installation des ImmoTools:

    ```bash
    sudo apt install openestate-immotool
    ```

---

Sollten Sie das Repository nicht nutzen wollen, können Sie alternativ die **DEB**-Installationsdatei herunterladen und per Doppelklick oder durch folgenden Befehl installieren:

```bash
sudo dpkg -i openestate-immotool_x.y.z_amd64.deb
```

Wobei `x.y.z` durch die jeweilige Versions-Nummer zu ersetzen ist.

---

> [**Hinweis**]{.info}
>
> Bei der Installation des Debian-Pakets werden automatisch die nötigen Einträge im Startmenü für alle Benutzer des Betriebssystems erzeugt.


#### Installation unter Linux {#intro_install_local_linux} 

Wenn Sie keine Debian-basierte Linux-Distribution nutzen oder das Repository nicht einbinden wollen, können Sie alternativ die **TAR.GZ**-Installationsdatei herunterladen. 

Nachdem Sie diese Datei auf Ihrem Rechner entpackt haben, finden Sie einen Ordner namens `OpenEstate-ImmoTool`. Verschieben Sie diesen Ordner an eine Stelle Ihrer Wahl (z.B. ins Benutzerverzeichnis oder nach `/opt/OpenEstate-ImmoTool`).

---

> [**Hinweis**]{.info}
>
> Bei Bedarf können Sie im Verzeichnis `bin` das Skript `StartMenuAdd.sh` ausführen. Es werden dadurch die Startmenü-Einträge des Programms für den aktuell angemeldeten Benutzer erzeugt. 


### ImmoTool starten


#### ImmoTool unter Windows starten

Bei der Installation unter Windows wird automatisch eine Verknüpfung auf dem Desktop erzeugt, über die das Programm gestartet werden kann. Alternativ finden Sie im Startmenü einen Ordner namens `OpenEstate-ImmoTool` mit verschiedenen Verknüpfungen.

Darüber hinaus können Sie das Programm auch über die Datei `ImmoTool.exe` / `ImmoTool.bat` im Verzeichnis `bin` des Programm-Verzeichnisses starten.


#### ImmoTool unter macOS starten

Führen Sie einen Doppelklick auf das Programmsymbol mit der Bezeichnung OpenEstate-ImmoTool aus. Es öffnet sich daraufhin der Finder mit den vom ImmoTool bereitgestellten Programmen. Wenn Sie hier auf das ImmoTool-Symbol klicken, wird das Programm gestartet.

{{< figure src="../admin/client/startup_mac.jpg" caption="Programmverzeichnis mit dem ImmoTool-Starter" >}}

> [**Hinweis**]{.info}
>
> Bei Bedarf können Sie das ImmoTool-Symbol ins Dock integrieren, um das Programm später schnell und unkompliziert starten zu können (siehe [Anleitung bei Apple](https://support.apple.com/de-de/HT201730)).


#### ImmoTool unter Linux starten

Wenn das ImmoTool mit dem [Debian-Paket]({{< relref "install_local.md#intro_install_local_debian" >}}) installiert wurde, finden Sie im Startmenü die Einträge für den Start des Programms.

Wenn das ImmoTool mit dem [TAR.GZ-Paket]({{< relref "install_local.md#intro_install_local_linux" >}}) installiert wurde, müssen Sie ggf. vorher noch die Datei `StartMenuAdd.sh` im `bin`-Verzeichnis des Programms ausführen um die Einträge im Startmenü zu erzeugen.

Alternativ zum Startmenü kann das Programm über die Datei `ImmoTool.sh` im `bin`-Verzeichnis des Programms gestartet werden.


### Sprache wählen

Beim ersten Programmstart prüft das `ImmoTool` ob eine Übersetzung zu der im Betriebssystem eingestellten Sprache vorliegt. Sollte dies nicht der Fall sein, erscheint das folgende Fenster, in dem Sie die im ImmoTool verwendete Sprache auswählen können:

> **TODO**
>
> Bild einfügen

Beachten Sie bitte, dass hier nur Sprachen zur Auswahl gestellt werden, für die aktuell eine Übersetzung vorliegt und für die ein Sprachpaket im Programm enthalten ist.


### Einzelplatz-Projekt erzeugen

Der Projektassistent wird geöffnet und Sie können eine Datenbank für Ihre Arbeit mit dem ImmoTool erzeugen. Im Folgenden und innerhalb des Programms werden solche Datenbanken als **Projekt** bezeichnet.

> **TODO**
>
> Bild einfügen. Weitere Anmerkungen zum Projektassistenten einfügen
