---

title: Passwort Datenbank-Benutzers zurücksetzen
linktitle: Passwort zurücksetzen
description: Wie das Passwort eines Benutzers in OpenEstate-ImmoServer zurückgesetzt werden kann…
weight: 60

menu:
  main:
    parent: admin-server
    identifier: admin-server-resetpwd

---

## Passwort eines Datenbank-Benutzers zurücksetzen {#admin_server_resetpwd}


### Passwort eines regulären Benutzers zurücksetzen {#admin_server_resetpwd_user}

Falls das Passwort eines regulären Benutzers verloren gegangen ist, kann sich der Administrator über das [AdminTool]({{< relref "../tool.md#admin_tool" >}}) anmelden und in der Benutzer-Verwaltung ein neues Passwort für den betreffenden Benutzer zuweisen (siehe ["Benutzer bearbeiten"]({{< relref "../tool.md#admin_tool_users" >}})).

{{< info >}}
So lange das Passwort von mindestens einem Datenbank-Benutzer mit Administrator-Berechtigung bekannt ist, können auf diesem Wege die Passwörter aller Benutzer (auch anderer Administratoren) geändert werden. 
{{< /info >}}


### Passwort des Administrators zurücksetzen {#admin_server_resetpwd_admin}

Falls das Passwort keines Datenbank-Administrators mehr bekannt ist, kann das Passwort über folgenden Umweg zurückgesetzt werden.

1.  Beenden Sie den ImmoTool-Server, wenn dieser aktuell in Betrieb sein sollte.

2.  Öffnen Sie die Datei `db.script` aus dem Verzeichnis der Datenbank des ImmoTool-Servers mit einem Texteditor. Standardmäßig finden Sie das Datenbank-Verzeichnis im Unterordner `data/immotool` des [Daten-Verzeichnisses]({{< relref "directories.md#admin_server_directories_data" >}}).

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

5.  Das Passwort des Administrator-Benutzers `SA` sollte damit geändert worden sein auf `test1234`. Dieses Passwort kann ab sofort verwendet werden um sich als Datenbank-Administrator anzumelden.

{{< warning >}}
Das geänderte Administrator-Passwort sollte mit Hilfe der [AdminTools]({{< relref "../tool.md#admin_tool" >}}) wieder auf ein geheimes Passwort geändert werden (siehe ["Benutzer bearbeiten"]({{< relref "../tool.md#admin_tool_users" >}})).
{{< /warning >}}
