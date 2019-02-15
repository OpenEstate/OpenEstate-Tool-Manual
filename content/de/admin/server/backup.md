---

title: Datensicherung
linktitle: Datensicherung
description: Administration von OpenEstate-ImmoTool…
weight: 40

menu:
  main:
    parent: admin-server
    identifier: admin-server-backup

---

## Datensicherung des ImmoTool-Servers {#admin_server_backup}

Im alltäglichen Betrieb ist es zwingend empfohlen, regelmäßige Sicherungen von der Datenbank des ImmoTool-Servers zu erzeugen. In diesem Abschnitt werden verschiedene Strategien zur Datensicherung vorgestellt und die Vorgehensweise zur Wiederherstellung beschrieben.


### Datensicherung eines inaktiven ImmoTool-Servers {#admin_server_backup_copy}

Wenn der ImmoTool-Server nicht gestartet ist (oder kurzzeitig beendet wurde), genügt eine Sicherung des Unterordners `var/data` im Programmverzeichnis des ImmoTool-Servers. Dort werden standardmäßig alle Dateien der Datenbank abgelegt.

{{< warning >}}
Es ist nicht empfehlenswert, das `var/data`-Verzeichnis im laufenden Betrieb des ImmoTool-Servers zu sichern. Dies kann zu einer fehlerhaften Datensicherung führen, die nicht wiederhergestellt werden kann.
{{< /warning >}}


### Datensicherung eines laufenden ImmoTool-Servers {#admin_server_backup_live}

Wenn man den ImmoTool-Server nicht beenden kann oder will um eine Datensicherung zu erzeugen, kann das Hilfsprogramm `manager-backup.bat` (unter Windows), `manager-backup.sh` (unter Unix/Linux) oder `manager-backup` (unter Mac OS X) aus dem `bin`-Verzeichnis des ImmoTool-Servers verwendet werden.

Damit das Hilfsprogramm sich mit der Datenbank verbinden kann, sind folgende Konfigurationen einmalig vorzunehmen.

1.  Öffnen Sie die Datei `manager.conf` im `etc`-Verzeichnis des ImmoTool-Servers mit einem Texteditor. Die Datei sieht ungefähr wie folgt aus:
    ```
    urlid immotool
    url jdbc:hsqldb:hsql://localhost/immotool
    username SA
    password
    ```

2.  Tragen Sie hinter dem Text `password` das Passwort des Datenbank-Administrators (Benutzer `SA`) ein. Nach der Änderung sieht die Datei ungefähr wie folgt aus:
    ```
    urlid immotool
    url jdbc:hsqldb:hsql://localhost/immotool
    username SA
    password test1234
    ```

3.  Starten Sie den ImmoTool-Server, wenn dies noch nicht gestartet ist.

4.  Starten Sie das Hilfsprogramm `manager-backup.bat` (unter Windows), `manager-backup.sh` (unter Unix/Linux) oder `manager-backup` (unter Mac OS X) aus dem `bin`-Verzeichnis des ImmoTool-Servers.

Nach erfolgreicher Ausführung des Hilfsprogramms finden Sie im Verzeichnis `var/backup/immotool` des ImmoTool-Servers ein TAR.GZ-Archiv mit der Sicherung der aktuellen Datenbank.

{{< tip >}}
Mit Hilfe des Taskplaners (unter Windows) oder eines Cron-Jobs (unter Unix) kann das Hilfsprogramm automatisch zu einem beliebigen Zeitpunkt geplant und ausgeführt werden.
{{< /tip >}}

{{< info >}}
Wenn mehr als eine Datenbank auf dem ImmoTool-Server hinterlegt wurden, müssen die Skripte `manager-backup.bat` / `manager-backup.sh` von Hand entsprechend angepasst und weitere Zugangsdaten müssen in `manager.conf` hinterlegt werden.
{{< /info >}}


### Wiederherstellung der gesicherten Datenbank {#admin_server_backup_restore}

Eine Datensicherung ist grundsätzlich eine Kopie der Datenbank-Dateien. Die Wiederherstellung dieser Daten ist relativ einfach.

1.  Beenden Sie den ImmoTool-Server, wenn dieser aktuell in Betrieb sein sollte.

2.  Sollte die Sicherung als ZIP-Archiv oder TAR.GZ-Archiv vorliegen, entpacken Sie diese Dateien auf Ihrem Rechner.

3.  Kopieren Sie die gesicherten Datenbank-Dateien `db.data`, `db.lobs`, `db.properties` & `db.script` in das Verzeichnis der jeweiligen Datenbank - z.B. in das Unterverzeichnis `var/data/immotool` des ImmoTool-Servers.

    {{< info >}}Stellen Sie sicher, dass das Datenbank-Verzeichnis vor dem Kopieren der Datenbank-Dateien komplett leer ist.{{< /info >}}

4.  Starten Sie den ImmoTool-Server neu, um mit der wiederhergestellten Datenbank weiterarbeiten zu können.

