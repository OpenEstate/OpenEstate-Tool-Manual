---

title: Projekt migrieren
linktitle: Migration
description: Migration eines Projekts von OpenEstate-ImmoTool…
weight: 50

menu:
  main:
    parent: admin
    identifier: admin-migration

---


## Einzelplatz- in Mehrplatz-Projekt umwandeln {#admin_migration_project_local}

Eine [Einzelplatz-Installation]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) kann bei Bedarf in eine [Netzwerk-Installation]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) umgewandelt werden. Die Datenbank wird dabei aus dem Einzelplatz-Projekt zum ImmoTool-Server kopiert und geringfügig angepasst.

1.  Installieren Sie den ImmoTool-Server, falls dies noch nicht geschehen ist (siehe ["ImmoTool-Server installieren"]({{< relref "../intro/install_server.md#intro_install_server" >}})).

2.  Beenden Sie den ImmoTool-Server, sollte dieser aktuell in Betrieb sein.

3.  Erzeugen Sie im [Daten-Verzeichnis]({{< relref "server/directories.md#admin_server_directories_data" >}}) des ImmoTool-Servers den Ordner `data/immotool`, wenn dieser noch nicht existieren sollte. Sollte das Verzeichnis bereits vorhanden sein, entfernen Sie die darin enthaltenen Dateien.

4.  Im Verzeichnis des Einzelplatz-Projektes sollten Sie ein Verzeichnis `data` finden. Darin befinden sich verschiedene Dateien der Datenbank: `immotool.data`, `immotool.lobs`, `immotool.properties` & `immotool.script`.

5.  Kopieren Sie die Dateien aus Schritt 4 ins Verzeichnis des ImmoTool-Servers, das in Schritt 3 erzeugt wurde. Benennen Sie die Dateien jeweils um in `db.data`, `db.lobs`, `db.properties` & `db.script`.

6.  Starten Sie den ImmoTool-Server neu und melden Sie sich mit dem [AdminTool]({{< relref "tool.md#admin_tool" >}}) auf dem Server an. Verwenden Sie den Benutzer **"SA"** mit einem **leeren Passwort**. Bei der ersten Anmeldung wird das [AdminTool]({{< relref "tool.md#admin_tool" >}}) Sie bitten ein Administrator-Passwort festzulegen.

Ab diesem Zeitpunkt kann mit dem ImmoTool & AdminTool auf die Datenbank als Mehrplatz-Projekt zugegriffen werden. Im ImmoTool muss abschließend noch ein Mehrplatz-Projekt erzeugt werden (siehe ["Verbindung zum ImmoTool-Server herstellen"]({{< relref "../intro/install_server.md#intro_install_server_immotool" >}})).

Wenn die Umstellung erfolgreich durchgeführt wurde und die Anmeldung am ImmoTool-Server über das ImmoTool funktioniert, kann das Einzelplatz-Projekt des ImmoTools bei Bedarf gelöscht werden.


## Mehrplatz- in Einzelplatz-Projekt umwandeln {#admin_migration_project_remote}

Eine [Netzwerk-Installation]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) kann bei Bedarf in eine  [Einzelplatz-Installation]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) umgewandelt werden. Die Datenbank wird dabei vom ImmoTool-Server in ein Einzelplatz-Projekt kopiert und geringfügig angepasst.

1.  Starten Sie das ImmoTool und erstellen Sie ein neues / leeres Einzelplatz-Projekt (siehe ["Einzelplatz-Projekt erzeugen"]{{< relref "../intro/install_client.md#intro_install_client_project" >}}). In dieses neu erstellte Projekt wird in den nächsten Schritten die Datenbank vom ImmoTool-Server übernommen.

2.  Beenden Sie das ImmoTool nachdem das neue / leere Einzelplatz-Projekt erstellt und erstmals geöffnet wurde.

3.  Beenden Sie den ImmoTool-Server, sollte dieser aktuell in Betrieb sein.

4.  Im Verzeichnis `data` des zuvor erstellten Einzelplatz-Projektes sollten verschiedene Dateien vorfinden: `immotool.data`, `immotool.lobs`, `immotool.properties` & `immotool.script`. Löschen Sie alle im `data`-Verzeichnis enthaltenen Dateien und Unterordner.

5.  Öffnen Sie das Datenbank-Verzeichnis des ImmoTool-Servers. Standardmäßig finden Sie dieses im Unterordner `data/immotool` des [Daten-Verzeichnisses]({{< relref "server/directories.md#admin_server_directories_data" >}}). Hier sollten Sie folgende Dateien vorfinden: `db.data`, `db.lobs`, `db.properties` & `db.script`. Kopieren Sie diese Dateien ins `data`-Verzeichnis des zuvor erstellten Einzelplatz-Projektes (siehe Schritt 4). Benennen Sie die Dateien jeweils um in `immotool.data`, `immotool.lobs`, `immotool.properties` & `immotool.script`.

6.  Bearbeiten Sie die Datei `immotool.script` aus dem `data`-Verzeichnis des Einzelplatz-Projektes mit einem Texteditor.

    {{< warning >}}Sichern Sie sich die `immotool.script`-Datei, bevor Sie daran Änderungen vornehmen. Eventuelle Fehler können zu einer kaputten Datenbank führen.{{< /warning >}}

7.  Suchen Sie in der `immotool.script`-Datei die Zeile, die wie folgt beginnt:

    ```
    CREATE USER SA PASSWORD DIGEST
    ```

    Tauschen Sie die gefundene Zeile durch folgende Zeile aus:

    ```
    CREATE USER SA PASSWORD DIGEST 'd41d8cd98f00b204e9800998ecf8427e'
    ```

8.  Speichern Sie die geänderte `immotool.script`-Datei ab.

Ab diesem Zeitpunkt kann das Einzelplatz-Projekt im ImmoTool geöffnet werden. Alle Daten aus dem Mehrplatz-Projekt stehen nun als Einzelplatz-Projekt zur Verfügung.


## Altes Projekt aus ImmoTool 0.9.x übernehmen {#admin_migration_legacy}

ImmoTool 0.9.x ist mittlerweile sehr alt, wird seit Längerem nicht weiter entwickelt und kann von OpenEstate nicht mehr betreut werden. Wir raten daher **dringend** auf die aktuellste Version 1.x zu migrieren. Im Folgenden werden die dafür nötigen Schritte dokumentiert.

{{< info >}}
Die alte ImmoTool-Installation bleibt bei der Migration komplett unangetastet. Sollte die Umstellung auf Version 1.x Probleme bereiten oder fehlschlagen, kann mit der alten Version bis zur Klärung des Problems normal weiter gearbeitet werden.
{{< /info >}}


### Projekt aus ImmoTool 0.9.x sichern {#admin_migration_legacy_backup}

Im ersten Schritt muss das Projekt in ImmoTool 0.9.x auf dem folgenden Wege gesichert werden.

1.  Aktualisieren Sie Ihre bestehende ImmoTool-Installation auf die aktuellste verfügbare Version (mindestens **0.9.15** bzw. **1.0-beta10f**). Klicken Sie dafür im Hauptmenü auf **"Extras → Aktualisierung"**.

    {{< figure src="migration_update.png" caption="Aktualisierung in ImmoTool 0.9.x starten" >}}
    
    Alternativ können Sie Version 0.9.33 (die letzte 0.9.x Version) von der [Webseite des OpenEstate-Projekts](https://openestate.org/downloads/openestate-immotool/0.9.33) herunterladen.

2.  Öffnen Sie das zu übernehmende Projekt im alten ImmoTool und erzeugen Sie eine Datensicherung, durch Klick im Hauptmenü auf **"Extras → Datenbank → Sicherung für Version 1.x"**.

    {{< figure src="migration_export.png" caption="Datensicherung für ImmoTool 1.x erzeugen" >}}

    Bei diesem Vorgang wird ein ZIP-Archiv mit den Inhalten der Projekt-Datenbank auf der Festplatte gespeichert, welches Sie in den folgenden Schritten benötigen werden.

Die Vorgehensweise zur Übernahme der exportierten Daten hängt davon ab, ob das Projekt in ImmoTool 1.x als [Einzelplatz-Installation]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) oder [Netzwerk-Installation]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) fortgeführt werden soll.


### Projekt als Einzelplatz-Installation übernehmen {#admin_migration_legacy_local}

Wenn des Projekt in ImmoTool 1.x als [**Einzelplatz-Installation**]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) betrieben werden soll, installieren Sie ImmoTool 1.x zusätzlich zur bereits vorhandenen alten ImmoTool-Version (siehe ["ImmoTool installieren"]({{< relref "../intro/install_client.md#intro_install_client" >}})).

{{< warning >}}
Überschreiben oder entfernen Sie die alte ImmoTool-Installation unter keinen Umständen! Die neue und alte Version sollten **nebeneinander** installiert werden.
{{< /warning >}}

Beim ersten Start von ImmoTool 1.x kann die zuvor gesicherte Datenbank mit Hilfe des [Projektassistenten]({{< relref "../usage/general/projects.md#usage_general_projects_wizard" >}}) importiert werden.

{{< figure src="migration_import_local.png" caption="Datensicherung via Projektassistent importieren" >}}

Wählen Sie als **"Art des Projektes"** die Option **"Einzelplatz-Projekt von ImmoTool 0.9.x migrieren"**. Im daraufhin dargestellten Formular, können Sie die [zuvor erstellte Sicherungsdatei]({{< relref "migration.md#admin_migration_legacy_backup" >}}) auswählen, indem Sie auf den Button **"Auswahl"** klicken. Das ZIP-Archiv wird daraufhin vom Programm geprüft und die Firmendaten automatisch übernommen.

Prüfen Sie sicherheitshalber die Firmendaten & Add-Ons und klicken Sie abschließend auf **"Projekt erzeugen"**. Während der Erzeugung des neuen Projekts wird die Sicherungsdatei automatisch in die Datenbank importiert.


### Projekt als Netzwerk-Installation übernehmen {#admin_migration_legacy_remote}

Wenn des Projekt in ImmoTool 1.x als [**Netzwerk-Installation**]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) betrieben werden soll, installieren Sie ImmoTool 1.x zusätzlich zur bereits vorhandenen alten ImmoTool-Version (siehe ["ImmoTool installieren"]({{< relref "../intro/install_client.md#intro_install_client" >}})) sowie den ImmoTool-Server (siehe ["ImmoTool-Server installieren"]({{< relref "../intro/install_server.md#intro_install_server" >}})).

{{< warning >}}
Überschreiben oder entfernen Sie die alte ImmoTool-Installation unter keinen Umständen! Die neue und alte Version sollten **nebeneinander** installiert werden.
{{< /warning >}}

Nachdem der ImmoTool-Server erfolgreich in Betrieb genommen wurde kann die gesicherte Datenbank mit Hilfe des [AdminTools]({{< relref "tool.md#admin_tool" >}}) auf den ImmoTool-Server übertragen werden. Die [zuvor erstellte Sicherungsdatei]({{< relref "migration.md#admin_migration_legacy_backup" >}}) kann im [AdminTool]({{< relref "tool.md#admin_tool" >}}) auf folgenden Wegen importiert werden:

-   Bei der **erstmaligen Anmeldung** am ImmoTool-Server wird ein Fenster dargestellt, über welches die Datenbank installiert werden kann. Dabei kann zusätzlich die zuvor erzeugte Sicherungsdatei angegeben werden.

    {{< figure src="migration_import_remote_new.png" caption="Datensicherung beim Erzeugen eines Projekts importieren" >}}

-   Wenn die Datenbank vorher bereits mit dem [AdminTool]({{< relref "tool.md#admin_tool" >}}) erzeugt wurden, kann die Datensicherung **nachträglich** durch Klick ins Hauptmenü auf **"Extras → Migration aus ImmoTool 0.9.x"** importiert werden.

    {{< figure src="migration_import_remote_existing.png" caption="Datensicherung nachträglich importieren" >}}

Nachdem die Datenübernahme ins Mehrplatz-Projekt abgeschlossen wurde kann die Verbindung zur Datenbank über das ImmoTool hergestellt werden (siehe ["Verbindung zum ImmoTool-Server herstellen"]({{< relref "../intro/install_server.md#intro_install_server_immotool" >}})).
