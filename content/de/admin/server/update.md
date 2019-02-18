---

title: ImmoTool-Server aktualisieren
linktitle: Server aktualisieren
description: Administration von OpenEstate-ImmoTool…
weight: 40

menu:
  main:
    parent: admin-server
    identifier: admin-server-update

---

## ImmoTool-Server aktualisieren {#admin_server_update}

Gelegentlich werden Aktualisierungen für den ImmoTool-Server veröffentlicht. Im Unterschied zum ImmoTool können diese Aktualisierungen jedoch nicht automatisch heruntergeladen und installiert werden. Im folgenden Abschnitt wird die Vorgehensweise beschrieben, um eine Aktualisierung des ImmoTool-Servers in Betrieb zu nehmen.

{{< tip >}}
Um einen Datenverlust im Falle eines Fehlers zu vermeiden, empfehlen wir das Programmverzeichnis des ImmoTool-Servers vor der Aktualisierung zu sichern.
{{< /tip >}}

1.  Laden Sie sich die aktuelle Version des ImmoTool-Servers aus dem [Download-Bereich von OpenEstate.org](http://de.openestate.org/downloads/) herunter.

2.  Entpacken Sie das heruntergeladene ZIP-Archiv (oder TAR.GZ-Archiv) in ein neues Verzeichnis auf Ihrem Computer.

3.  Beenden Sie den ImmoTool-Server auf Ihrem Rechner, sollte dieser aktuell noch gestartet sein. Sollte der ImmoTool-Server als Dienst auf Ihrem Rechner installiert worden sein, deinstallieren Sie den Dienst bevor Sie mit der Aktualisierung fortfahren.

4.  Kopieren Sie alle Dateien aus dem in Schritt 2 erzeugten `bin`-Verzeichnis in das gleichnamige Verzeichnis des aktuell installierten ImmoTool-Servers. Bereits vorhandene Dateien im `bin`-Verzeichnis können dabei überschrieben werden.

5.  Kopieren Sie alle Dateien aus dem in Schritt 2 erzeugten `etc`-Verzeichnis in das gleichnamige Verzeichnis des aktuell installierten ImmoTool-Servers. Bereits vorhandene Dateien im `etc`-Verzeichnis sollten dabei **nicht** überschrieben werden.

6.  Entfernen Sie alle Dateien und Ordner im `lib`-Verzeichnis des aktuell installierten ImmoTool-Servers. Kopieren Sie dorthin alle Dateien aus dem in Schritt 2 erzeugten gleichnamigen Verzeichnis.

7.  Entfernen Sie alle Dateien und Ordner im `doc`-Verzeichnis des aktuell installierten ImmoTool-Servers. Kopieren Sie dorthin alle Dateien aus dem in Schritt 2 erzeugten gleichnamigen Verzeichnis.

8.  Der ImmoTool-Server kann nun wieder neu gestartet werden. Bei Bedarf kann nun wieder der ImmoTool-Server als Dienst im Betriebssystem installiert werden.
