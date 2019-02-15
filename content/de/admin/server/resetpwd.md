---

title: Passwort zurücksetzen
linktitle: Passwort zurücksetzen
description: Administration von OpenEstate-ImmoTool…
weight: 60

menu:
  main:
    parent: admin-server
    identifier: admin-server-resetpwd

---

## Passwort des Datenbank-Administrators zurücksetzen {#admin_server_resetpwd}

Im Falle, dass der Administrator sein Passwort vergessen hat und sich nicht mehr auf die vom ImmoTool-Server bereitgestellte Datenbank zugreifen kann, kann auf folgendem Wege ein neues Passwort zugewiesen werden.

1.  Beenden Sie den ImmoTool-Server, wenn dieser aktuell in Betrieb sein sollte.

2.  Öffnen Sie die Datei `db.script` aus dem Verzeichnis `var/data/immotool` des ImmoTool-Servers mit einem Texteditor.

    {{< warning >}}Sichern Sie sich die `db.script`-Datei, bevor Sie daran Änderungen vornehmen. Eventuelle Fehler können zu einer kaputten Datenbank führen.{{< /warning >}}

3.  Suchen Sie in der `db.script`-Datei die Zeile, die wie folgt beginnt:
    ```
    CREATE USER SA PASSWORD DIGEST
    ```

    Tauschen Sie die gefundene Zeile durch folgende Zeile aus:
    ```
    CREATE USER SA PASSWORD DIGEST '16d7a4fca7442dda3ad93c9a726597e4'
    ```

4.  Speichern Sie die geänderte `db.script`-Datei ab und starten Sie den ImmoTool-Server neu.

5.  Das Passwort des Administrator-Benutzers `SA` sollte damit geändert worden sein auf `test1234`. Dieses Passwort kann ab sofort verwendet werden, um sich als Datenbank-Administrator anzumelden.

    {{< warning >}}Das geänderte Administrator-Passwort sollte mit Hilfe der AdminTools wieder auf ein geheimes Passwort geändert werden.{{< /warning >}}
