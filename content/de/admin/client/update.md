---

title: Aktualisierung durchführen
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
