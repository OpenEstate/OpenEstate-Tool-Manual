---

title: Projekt migrieren
linktitle: Migration
description: Migration eines Projekts von OpenEstate-ImmoTool…
weight: 40

menu:
  main:
    parent: admin
    identifier: admin-migration

---


## Einzelplatz- in Mehrplatz-Projekt umwandeln {#admin_migration_project_local}

Im Folgenden wird die Vorgehensweise beschrieben, um ein bestehendes Einzelplatz-Projekt nachträglich auf einen ImmoTool-Server zu migrieren. Die im Einzelplatz-Projekt erfassten Daten können auf diesem Wege für mehrere Benutzer im Netzwerk verfügbar gemacht werden.

1.  Beenden Sie den ImmoTool-Server, sollte dieser aktuell in Betrieb sein.

2.  Erzeugen Sie im Verzeichnis des ImmoTool-Servers den Ordner `var/data/immotool`, wenn dieser noch nicht existieren sollte. Sollte das Verzeichnis bereits vorhanden sein, entfernen Sie die darin enthaltenen Dateien.

3.  Im Verzeichnis des Einzelplatz-Projektes sollten Sie ein Verzeichnis `data` finden. Darin befinden sich verschiedene Dateien der Einzelplatz-Datenbank: `immotool.data`, `immotool.lobs`, `immotool.properties` & `immotool.script`.

4.  Kopieren Sie die Dateien aus Schritt 3 ins Verzeichnis `var/data/immotool` des ImmoTool-Servers. Benennen Sie die Dateien jeweils um in `db.data`, `db.lobs`, `db.properties` & `db.script`.

5.  Starten Sie den ImmoTool-Server neu und melden Sie sich mit dem AdminTool auf dem Server an (Benutzer "SA" mit leerem Passwort). Bei der ersten Anmeldung wird das AdminTool Sie bitten ein Administrator-Passwort festzulegen.

Ab diesem Zeitpunkt kann mit dem ImmoTool & AdminTool auf die Datenbank als Mehrplatz-Projekt zugegriffen werden. Der Verbindungsaufbau auf das Mehrplatz-Projekt via ImmoTool wird im Handbuch-Kapitel zur [Installation im Netzwerk]({{< relref "../intro/install_server.md#intro_install_server_immotool_project" >}}) beschrieben.


## Mehrplatz- in Einzelplatz-Projekt umwandeln {#admin_migration_project_remote}

Im Folgenden wird die Vorgehensweise beschrieben, um ein bestehendes Mehrplatz-Projekt aus einem ImmoTool-Server in ein Einzelplatz-Projekt umzuwandeln.

1.  Starten Sie das ImmoTool und erstellen Sie ein neues / leeres Einzelplatz-Projekt. In dieses neu erstellte Projekt wird in den nächsten Schritten die Datenbank vom ImmoTool-Server übernommen.

    > **Hinweis**
    >
    > Merken Sie sich den Speicherort des Projektes auf Ihrer Festplatte.

2.  Beenden Sie das ImmoTool nachdem das neue Projekt erstellt und erstmals geöffnet wurde.

3.  Beenden Sie den ImmoTool-Server, sollte dieser aktuell in Betrieb sein.

4.  Im Verzeichnis `data` des zuvor erstellten Einzelplatz-Projektes sollten verschiedene Dateien vorfinden: `immotool.data`, `immotool.lobs`, `immotool.properties` & `immotool.script`. Löschen Sie alle im `data`-Verzeichnis enthaltenen Dateien und Unterordner.

5.  Im Verzeichnis `var/data/immotool` des ImmoTool-Servers sollten Sie folgende Dateien vorfinden: `db.data`, `db.lobs`, `db.properties` & `db.script`. Kopieren Sie diese Dateien ins `data`-Verzeichnis des zuvor erstellten Einzelplatz-Projektes. Benennen Sie die Dateien jeweils um in `immotool.data`, `immotool.lobs`, `immotool.properties` & `immotool.script`.

6.  Bearbeiten Sie die Datei `immotool.script` aus dem `data`-Verzeichnis des Einzelplatz-Projektes mit einem Texteditor.

    > **Achtung**
    >
    > Sichern Sie sich die `immotool.script`-Datei, bevor Sie daran Änderungen vornehmen. Eventuelle Fehler können zu einer kaputten Datenbank führen.

7.  Suchen Sie in der `immotool.script`-Datei die Zeile, die wie folgt beginnt:
    ```
    CREATE USER SA PASSWORD DIGEST
    ```

    Tauschen Sie die gefundene Zeile durch folgende Zeile aus:
    ```
    CREATE USER SA PASSWORD DIGEST 'd41d8cd98f00b204e9800998ecf8427e'
    ```

8.  Speichern Sie die geänderte `immotool.script`-Datei ab.

Ab diesem Zeitpunkt kann das Einzelplatz-Projekt mit ImmoTool geöffnet werden und alle Daten aus dem Mehrplatz-Projekt stehen zur Verfügung.


## Altes Projekt aus ImmoTool 0.9.x übernehmen {#admin_migration_project_0_9}

Die folgende Anleitung beschreibt die Vorgehensweise, um ein Projekt aus ImmoTool 0.9.x in ImmoTool 1.0 zu übernehmen.

> **Hinweis**
>
> Die alte ImmoTool-Installation bei der Migration komplett unangetastet. Sollte die Umstellung auf Version 1.0 Probleme bereiten oder fehlschlagen, kann mit der alten Version normal weiter gearbeitet werden.


### Projekt aus "ImmoTool 0.9.x" sichern {#admin_migration_project_0_9_backup}

Im ersten Schritt muss das Projekt in ImmoTool 0.9.x auf dem folgenden Wege gesichert werden.

1.  Aktualisieren Sie Ihre bestehende ImmoTool-Installation auf die aktuellste Version (mindestens 0.9.15 bzw. 1.0-beta10f). Klicken Sie dafür im Hauptmenü auf `Extras` → `Aktualisierung`.

    {{< figure src="migration_upgrade_0_9-01.jpg" caption="ImmoTool 0.9.x aktualisieren" >}}

2.  Öffnen Sie das zu übernehmende Projekt im alten ImmoTool und erzeugen Sie eine Datensicherung, durch Klick im Hauptmenü auf `Extras` → `Datenbank` → `Sicherung für Version 1.x`.

    {{< figure src="migration_upgrade_0_9-02.jpg" caption="Datensicherung für ImmoTool 1.x erzeugen" >}}

    Bei diesem Vorgang wird ein ZIP-Archiv mit den Inhalten der Projekt-Datenbank auf der Festplatte gespeichert, welches Sie unter Schritt (4) noch benötigen werden.

Die Vorgehensweise zur Übernahme der unter (2) exportierten Daten hängt davon ab, ob das Projekt in ImmoTool 1.0 als Einzelplatz- oder Mehrplatz-Projekt fortgeführt werden soll.


### Projekt als Einzelplatz-Installation übernehmen {#admin_migration_project_0_9_local}

Wenn des Projekt in ImmoTool 1.0 als **Einzelplatz-Installation** betrieben werden soll, installieren Sie ImmoTool 1.0 zusätzlich zur bereits vorhandenen alten ImmoTool-Version. Die Installationsschritte sind im Kapitel ["ImmoTool als Einzelplatz-Version installieren"]({{< relref "../intro/install_client.md#intro_install_client" >}}) dokumentiert.

> **Wichtig**
>
> Überschreiben oder entfernen Sie die alte ImmoTool-Installation unter keinen Umständen! Die neue und alte Version sollten *nebeneinander* installiert werden.

Beim ersten Start von ImmoTool 1.0 kann die zuvor gesicherte Datenbank mit Hilfe des [Projektassistenten]({{< relref "../usage/general/projects.md#usage_general_projects_wizard" >}}) importiert werden.

{{< figure src="migration_upgrade_0_9_local-01.jpg" caption="Datensicherung via Projektassistent importieren" >}}

Wählen Sie als `Art des Projektes` die Option `Neues Einzelplatz-Projekt aus ImmoTool 0.9.x übernehmen`. Im daraufhin dargestellten Formular, können Sie die [zuvor erstellte Sicherungsdatei](#admin_migration_project_0_9_backup) auswählen, indem Sie auf den Button `Auswahl` klicken. Das ZIP-Archiv wird daraufhin vom Programm geprüft und die Firmendaten automatisch übernommen.

{{< figure src="migration_upgrade_0_9_local-02.jpg" caption="Sicherungsdatei zum Import ausgewählt" >}}

Prüfen Sie sicherheitshalber die Firmendaten & Add-Ons und klicken Sie abschließend auf `Projekt erzeugen`. Während der Erzeugung des neuen Projekts wird die Sicherungsdatei automatisch in die Datenbank importiert.


### Projekt als Mehrplatz-Installation übernehmen {#admin_migration_project_0_9_remote}

Wenn des Projekt in ImmoTool 1.0 als **Mehrplatz-Installation** betrieben werden soll, installieren Sie ImmoTool 1.0 zusätzlich zur bereits vorhandenen alten ImmoTool-Version sowie den ImmoTool-Server. Die Installationsschritte sind im Kapitel ["ImmoTool als Netzwerk-Version installieren"]({{< relref "../intro/install_server.md#intro_install_server" >}}) dokumentiert.

> **Wichtig**
>
> Überschreiben oder entfernen Sie die alte ImmoTool-Installation unter keinen Umständen! Die neue und alte Version sollten *nebeneinander* installiert werden.

Nachdem der ImmoTool-Server erfolgreich in Betrieb genommen wurde, kann die gesicherte Datenbank mit Hilfe des AdminTools auf den ImmoTool-Server übertragen werden. Die [zuvor erstellte Datensicherung](#admin_migration_project_0_9_backup) kann im AdminTool auf folgenden Wegen importiert werden:

-   Bei der erstmaligen Anmeldung am ImmoTool-Server wird ein Fenster dargestellt, über welches die Datenbank installiert werden kann. Dabei kann zusätzlich die zuvor erzeugte Sicherungsdatei angegeben werden.

    {{< figure src="migration_upgrade_0_9_remote-01.jpg" caption="Datensicherung beim Erzeugen eines Projekts importieren" >}}

-   Wenn die Datenstrukturen bereits mit dem AdminTool erzeugt wurden, kann die Datensicherung nachträglich durch Klick ins Hauptmenü auf `Werkzeuge` → `Migration aus früherer Version` importiert werden.

    {{< figure src="migration_upgrade_0_9_remote-02.jpg" caption="Datensicherung nachträglich importieren" >}}

Nachdem die Datenübernahme ins Mehrplatz-Projekt abgeschlossen wurde, kann die Verbindung zur Datenbank über das ImmoTool hergestellt werden, wie im Kapitel ["ImmoTool mit dem ImmoTool-Server verbinden"]({{< relref "../intro/install_server.md#intro_install_server_immotool_project" >}}) beschrieben.
