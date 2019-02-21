---

title: ImmoTool-Server aktualisieren
linktitle: Server aktualisieren
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

Verschieben Sie den Programm-Starter **"OpenEstate-ImmoServer"** an die gleiche Stelle, wo sich die alte ImmoTool-Installation befindet. Bestätigen Sie die Rückfrage, ob die alte Version des Programms überschrieben werden soll.

{{< todo >}}
Testen, ob eine vorherige Löschung des Programm-Ordners nötig ist.
{{< /todo >}}


### Aktualisierung unter Debian, Ubuntu & Co. {#admin_server_update_debian}

Wenn Sie das Debian-Repository in Ihrem Betriebssystem eingerichtet haben (siehe ["Installation unter Debian, Ubuntu & Co."]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}})), müssen Sie das Programm **nicht** von der OpenEstate-Webseite herunterladen. Statt dessen genügt es folgende Befehle im Terminal auszuführen:

```bash
sudo apt update
sudo apt install openestate-immoserver
```

Wenn Sie das Debian-Repository **nicht** nutzen aber das **DEB**-Installationspaket bei der Installation verwendet haben, können Sie die **DEB**-Installationsdatei herunterladen und per Doppelklick starten. Alternativ kann die Datei über folgenden Befehl im Terminal installiert werden:

```bash
sudo dpkg -i openestate-immoserver_x.y.z_amd64.deb
```

Wobei `x.y.z` durch die jeweilige Versions-Nummer zu ersetzen ist.

{{< warning >}}
Sollten Sie Anpassungen im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) vorgenommen, sichern Sie die betreffende Dateien vor der Aktualisierung. Nach der Aktualisierung können Sie die betreffenden Dateien wieder zurück kopieren.
{{< /warning >}}


### Aktualisierung unter Linux {#admin_server_update_linux}

1.  Bringen Sie in Erfahrung in welchem Verzeichnis der ImmoTool-Server installiert wurde.
2.  Laden Sie die **TAR.GZ**-Installationsdatei für Linux herunter und entpacken Sie die Datei auf Ihrem Rechner. 
3.  Benennen Sie das in Schritt 1 ermittelte Programmverzeichnis des ImmoTool-Servers um - z.B. in `OpenEstate-ImmoServer-ALT`.
4.  Erzeugen Sie ein neues / leeres Verzeichnis unter dem in Schritt 1 festgestellten Namen - z.B. `OpenEstate-ImmoServer`.
5.  Kopieren Sie die in Schritt 2 entpackten Dateien in das neue / leere Programmverzeichnis.

Nachdem das Programm in der neuen Version erfolgreich gestartet werden konnte, kann das in Schritt 3 erzeugte alte Programmverzeichnis bei Bedarf gelöscht werden.

{{< warning >}}
Sollten Sie Anpassungen im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) vorgenommen, sichern Sie die betreffende Dateien vor der Aktualisierung. Nach der Aktualisierung können Sie die betreffenden Dateien wieder zurück kopieren.
{{< /warning >}}
