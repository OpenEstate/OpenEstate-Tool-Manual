---

title: Datenbank sichern & wiederherstellen
linktitle: Datensicherung
description: Wie eine Datenbank von OpenEstate-ImmoTool gesichert und wiederhergestellt werden kann…
weight: 40

menu:
  main:
    parent: admin
    identifier: admin-backup

---

## Datenbank sichern & wiederherstellen {#admin_backup}

Für den alltäglichen Betrieb ist es **unbedingt empfohlen** eine Strategie zur regelmäßigen Datensicherung zu finden und umzusetzen. Dieses Kapitel beschreibt mögliche Vorgehensweisen, wie eine Datensicherung in ImmoTool und ImmoTool-Server erfolgen kann.  

Es ist zu beachten, dass hier unterschiedliche Vorgehensweisen bei [Einzelplatz-Installationen]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) und [Netzwerk-Installationen]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) nötig sind (siehe ["Wie ImmoTool betrieben werden kann…"]({{< relref "../intro/install_types.md#intro_install_types" >}})).

{{< warning >}}
Verlassen Sie sich nicht allein auf die Sicherungsfunktionen des Betriebssystems. Die Praxis hat gezeigt, dass z.B. die Verwendung von Sicherungspunkten unter Windows zu einer fehlerhaft wiederhergestellten Datenbank führen kann.
{{< /warning >}}

{{< info >}}
Um eventuelle Datenverluste oder Probleme zu vermeiden, sollten Sie eine Strategie zur Datensicherung implementieren sobald das ImmoTool produktiv genutzt wird.
{{< /info >}}

{{< tip >}}
Wir empfehlen Ihnen die Vorgehensweise zur Sicherung und Wiederherstellung zu testen und sich die nötigen Schritte zu notieren. Somit können Sie im Fehlerfall auf Ihre interne Dokumentation zurückgreifen und schnell handeln.
{{< /tip >}}

{{< tip >}}
Um eine maximale Ausfallsicherheit zu gewährleisten bietet es sich an, die Sicherungsdateien der Datenbank auf einer externen / separaten Hardware zu sichern. Verwenden Sie z.B. eine externe Festplatte oder übertragen Sie die Sicherungsdateien zu einem separaten Server (z.B. auf Ihrem Webspace oder bei einem Cloud-Anbieter).
{{< /tip >}}


### Sicherung einer Einzelplatz-Installation {#admin_backup_local}

Bei einer **Einzelplatz-Installation** wird die zu sichernde Datenbank direkt vom ImmoTool verwaltet (siehe ["Betrieb an einem einzelnen Arbeitsplatz"]({{< relref "../intro/install_types.md#intro_install_types_local" >}})). Die Sicherung sollte daher in der Regel über den Rechner durchgeführt werden, auf dem auch das ImmoTool installiert ist.


#### Projekt-Verzeichnis kopieren {#admin_backup_local_copy}

Die einfachste Form der Datensicherung einer **Einzelplatz-Installation** ist die Kopie des [Projekt-Verzeichnisses]({{< relref "client/directories.md#admin_client_directories_project" >}}). Bringen Sie in Erfahrung unter welchem Ordner das Projekt gespeichert wurde und sichern Sie diesen Ordner entsprechend.

{{< info >}}
Standardmäßig erstellt das ImmoTool für jedes verwaltete Projekt im Benutzerverzeichnis unter **`OpenEstate-Files/projects`** ein separates Verzeichnis. 
{{< /info >}}

{{< warning >}}
Erstellen Sie die Kopie des [Projekt-Verzeichnisses]({{< relref "client/directories.md#admin_client_directories_project" >}}) möglichst nur, wenn das Projekt aktuell nicht bereits vom ImmoTool geöffnet ist - bzw. wenn aktuell kein ImmoTool gestartet ist.
{{< /warning >}}


#### Manuelle Sicherung via ImmoTool {#admin_backup_local_manual}

Nachdem ein Einzelplatz-Projekt im Programm geöffnet wurde, können Sie im Hauptmenü auf **"Extras → Datenbank → Sicherung"** klicken um eine manuelle Sicherung der Datenbank durchzuführen. Es erscheint daraufhin ein Dialogfenster, in dem der Speicherort der zu erzeugenden Datensicherung gewählt werden kann.


#### Automatische Sicherung via ImmoTool {#admin_backup_local_automatic}

Alternativ zur manuellen Sicherung kann eine automatische Datensicherung eines Einzelplatz-Projekts im Programm eingerichtet werden. In diesem Falle erzeugt das Programm automatisch eine Sicherung der Datenbank in bestimmten Situationen.

Nachdem ein Einzelplatz-Projekt im Programm geöffnet wurde, können Sie im Hauptmenü auf **"Extras → Einstellungen"** klicken um die Programm-Einstellungen zu öffnen. Wählen Sie im dargestellten Dialogfenster das Formular **"Datenbank"** aus um die automatische Datensicherung zu konfigurieren.

{{< figure src="backup_local_automatic.png" caption="Konfiguration der automatischen Datensicherung" >}}

In dem Formular kann ein Ordner gewählt werden, unter dem die automatischen Datensicherungen gespeichert werden sollen. Des Weiteren kann gewählt werden, zu welchem Zeitpunkt die automatische Datensicherung erfolgen soll (z.B. beim Öffnen des Projekts).

Der als **"Limit"** eingetragene Zahlenwert legt fest, wie viele Sicherungen im angegebenen Ordner maximal gespeichert werden sollen. Wenn z.B. mehr als fünf Sicherungen im Ordner vorliegen werden die ältesten Sicherungen entfernt sodass das eingetragene Limit nicht überschritten wird.

{{< tip >}}
Wenn für die automatische Datensicherung eine externe USB-Festplatte oder ein Ordner auf einem anderen Rechner gewählt wird (z.B. ein Netzlaufwerk unter Windows), kann sichergestellt werden, dass die Datensicherung auch beim Hardware-Defekt des Arbeitsplatz-Rechners erhalten bleibt.
{{< /tip >}}


#### Wiederherstellung einer Sicherung {#admin_backup_local_restore}

Wenn das [Projekt-Verzeichnis]({{< relref "client/directories.md#admin_client_directories_project" >}}) kopiert wurde (siehe ["Projekt-Verzeichnis kopieren"]({{< relref "backup.md#admin_backup_local_copy" >}})), kann das gesicherte Verzeichnis einfach an den ursprünglichen Speicherort zurück kopiert und mit dem ImmoTool geöffnet werden.

Sicherungen, die aus dem ImmoTool heraus erzeugt wurden, werden als **TAR.GZ**-Archiv gespeichert (siehe ["Manuelle Sicherung via ImmoTool"]({{< relref "backup.md#admin_backup_local_manual" >}}) und ["Automatische Sicherung via ImmoTool"]({{< relref "backup.md#admin_backup_local_automatic" >}})). Zur Wiederherstellung dieser Sicherungen können Sie wie folgt vorgehen:

1.  Beenden Sie das ImmoTool, sollte es aktuell gestartet sein.
2.  Entpacken Sie das TAR.GZ-Archiv mit der Datensicherung.
3.  Öffnen Sie das [Projekt-Verzeichnis]({{< relref "client/directories.md#admin_client_directories_project" >}}) im Datei-Browser (Explorer / Finder).
4.  Benennen Sie den Unterordner **`data`** um - z.B. in **`data-alt`**.
5.  Erzeugen Sie einen neuen Unterordner namens **`data`**.
6.  Kopieren Sie die in Schritt 2 entpackten Dateien in den neu erstellten **`data`**-Ordner.
7.  Starten Sie das ImmoTool und öffnen Sie das betreffende Projekt.

Wenn das wiederhergestellte Projekt erfolgreich geöffnet werden kann, kann der in Schritt 4 erstellte Ordner **`data-alt`** bei Bedarf gelöscht werden.


### Sicherung einer Netzwerk-Installation {#admin_backup_network}

Bei einer **Netzwerk-Installation** wird die zu sichernde Datenbank vom ImmoTool-Server verwaltet (siehe ["Betrieb an mehreren Arbeitsplätzen"]({{< relref "../intro/install_types.md#intro_install_types_network" >}})). Die Sicherung sollte daher in der Regel über den Rechner durchgeführt werden, auf dem auch der ImmoTool-Server installiert ist.


#### Datensicherung eines inaktiven ImmoTool-Servers {#admin_backup_network_copy}

Wenn der ImmoTool-Server nicht gestartet ist (oder kurzzeitig beendet wurde), kann das [Daten-Verzeichnis]({{< relref "server/directories.md#admin_server_directories_data" >}}) des ImmoTool-Servers kopiert werden. Dort werden standardmäßig die Dateien aller im Server verwalteten Datenbanken abgelegt.

{{< warning >}}
Es ist nicht empfehlenswert, das [Daten-Verzeichnis]({{< relref "server/directories.md#admin_server_directories_data" >}}) im laufenden Betrieb des ImmoTool-Servers zu sichern. Dies kann zu einer fehlerhaften Datensicherung führen, die nicht wiederhergestellt werden kann.
{{< /warning >}}


#### Datensicherung eines laufenden ImmoTool-Servers {#admin_backup_network_live}

Der ImmoTool-Server kann im laufenden Betrieb gesichert werden, ohne dass dieser beendet werden muss. Für diesen Fall wird mit dem ImmoTool-Server ein Hilfsprogramm namens **"ManagerBackup"** bereitgestellt.

-   Das Programm kann unter Windows über das Startmenü mit der Verknüpfung **"Datenbank sichern""** ausgeführt werden.
-   Das Programm kann unter macOS über den Starter **"ManagerBackup""** ausgeführt werden.
-   Alternativ kann das Programm über die Datei **`ManagerBackup.exe`** / **`ManagerBackup.bat`** / **`ManagerBackup.sh`** im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "server/directories.md#admin_server_directories_application" >}}) ausgeführt werden.

Das Hilfsprogramm muss eine Verbindung zu allen zu sichernden Datenbanken herstellen. Dafür muss sich das Programm als Administrator auf allen zu sichernden Datenbanken anmelden können.

Öffnen Sie dafür die Datei **`manager.conf`** im [Konfigurations-Verzeichnis]({{< relref "server/directories.md#admin_server_directories_etc" >}}) des ImmoTool-Servers mit einem Texteditor. Für jede zu sichernde Datenbank sind folgende Zeilen in die Datei einzufügen:

```
urlid immotool
url jdbc:hsqldb:hsql://localhost/immotool
username SA
password
```

Hinter dem Wort **`password`** muss getrennt durch ein Leerzeichen das Passwort des Datenbank-Administrators (**`SA`**) eingetragen werden - z.B. **`password test1234`** (siehe auch ["Manager-Programme konfigurieren"]({{< relref "server/setup.md#admin_server_setup_manager" >}})).

Wenn **ManagerBackup** gestartet wird, wird für alle in **`manager.conf`** konfigurierten Datenbanken eine Sicherung erzeugt. Das Programm speichert die Sicherungen standardmäßig im [Daten-Verzeichnis]({{< relref "server/directories.md#admin_server_directories_data" >}}) des ImmoTool-Servers in einem Unterordner namens **`backups`**. 


##### Automatische Datensicherung unter Windows {#admin_backup_network_live_windows}

Mit Hilfe der Aufgabenplanung des Windows-Betriebssystems kann **ManagerBackup** automatisch zu einem beliebigen Zeitpunkt ausgeführt werden.

Öffnen Sie die Aufgabenplanung von Windows:

1.  Drücken Sie auf der Tastatur die **"Windows-Taste"** gemeinsam mit dem Buchstaben **"R"** um ein Fenster zur Ausführung von Programmen zu öffnen. Alternativ können Sie die Eingabeaufforderung öffnen.

2.  Tragen Sie den Befehl **`taskschd.msc`** ein und bestätigen Sie die Eingabe mit **"ENTER"**.

Klicken Sie im dargestellten Dialogfenster auf der rechten Seite im Bereich **"Aktionen"** auf **"Aufgabe erstellen"**.

{{< figure src="backup_network_live_windows_task_add.png" caption="Aufgabe zur automatischen Datensicherung erstellen" >}}

Es öffnet sich daraufhin ein weiteres Dialogfenster, über welches die Aufgabe eingerichtet werden kann. 

{{< figure src="backup_network_live_windows_task_general.png" caption="Allgemeine Einstellungen zur Aufgabe" >}}

Tragen Sie im Reiter **"Allgemein"** einen passenden Namen und eine passende Beschreibung für die Aufgabe ein. Darüber hinaus sollten Sie durch Klick auf **"Benutzer oder Gruppe ändern"** den Benutzer **"Lokaler Dienst"** auswählen. 

{{< figure src="backup_network_live_windows_task_trigger.png" caption="Allgemeine Einstellungen zur Aufgabe" >}}

Im Reiter **"Trigger"** können Sie nach Bedarf konfigurieren, wann die automatische Datensicherung ausgeführt werden soll.

{{< figure src="backup_network_live_windows_task_action.png" caption="Allgemeine Einstellungen zur Aufgabe" >}} 

Wählen Sie im Reiter **"Aktionen"** die Datei **`ManagerBackup.exe`** aus dem Unterordner **`bin`** im [Programm-Verzeichnisses]({{< relref "server/directories.md#admin_server_directories_application" >}}) des ImmoTool-Servers aus.

Bei Bedarf können Sie weitere Einstellungen über diese Dialogfenster vornehmen. Klicken Sie abschließend auf **"OK"** um die Aufgabe im Betriebssystem zu registrieren.


##### Automatische Datensicherung unter macOS {#admin_backup_network_live_mac}

Wenn der ImmoTool-Server unter macOS über die bereitgestellten Skripte als Dienst eingerichtet wurde, kann dabei auch eine tägliche automatische Datensicherung konfiguriert werden (siehe ["Dienst unter macOS einrichten"]({{< relref "server/service.md#admin_server_service_mac" >}})).

Falls bei der Installation des Dienstes die Option zur automatischen Datensicherung aktiviert wurde, wird eine Datei namens **`org.openestate.tool.server.backup.plist`** im Verzeichnis **`/Library/LaunchDaemons`** abgelegt. Über diese Datei wird im Betriebssystem die tägliche automatische Ausführung von **ManagerBackup** konfiguriert.

{{< info >}}
Sie sind nicht gezwungen die bereitgestellten Funktionen zur automatischen Datensicherung zu nutzen. Statt dessen können Sie auch einen eigenen Cronjob (oder Agent für launchd) konfigurieren um **ManagerBackup** auszuführen.
{{< /info >}}


##### Automatische Datensicherung unter Linux {#admin_backup_network_live_linux}

Wenn der ImmoTool-Server unter Linux über das bereitgestellte [**Debian**-Paket]({{< relref "../intro/install_server.md#intro_install_server_setup_debian" >}}) installiert wurde, wird automatisch die tägliche Datensicherung eingerichtet.

Alternativ kann bei der Installation des Dienstes über die bereitgestellten Skripte die automatische Datensicherung aktiviert werden (siehe ["Dienst unter Linux einrichten"]({{< relref "server/service.md#admin_server_service_linux" >}})).

Über die Dateien **`openestate-immoserver-backup.timer`** und **`openestate-immoserver-backup.service`** im Verzeichnis **`/etc/systemd`** wird im Betriebssystem die tägliche automatische Ausführung von **ManagerBackup** konfiguriert.

{{< info >}}
Sie sind nicht gezwungen die bereitgestellten Funktionen zur automatischen Datensicherung zu nutzen. Statt dessen können Sie auch einen eigenen Cronjob (oder Timer für systemd) konfigurieren um **ManagerBackup** auszuführen.
{{< /info >}}


##### Parameter zur Ausführung von ManagerBackup {#admin_backup_network_live_options}

Das Hilfsprogramm **ManagerBackup** kann über Kommandozeilen-Parameter bei Bedarf präziser gesteuert werden.

-   **-help** \
    Stellt eine Zusammenfassung aller Parameter auf der Konsole dar und beendet das Programm.

-   **-conf `<file>`** \
    Der Pfad zur **`manager.conf`** Konfigurationsdatei kann bei Bedarf angegeben werden.
    
-   **-id `<urlid>`** \
    Nur die in **`manager.conf`** registrierte Datenbank mit der Kennung **`<urlid>`** sichern. Andernfalls werden alle in **`manager.conf`** registrierten Datenbanken gesichert.

-   **-dir `<path>`** \
    Die erzeugten Datensicherungen werden im unter **`<path>`** angegebenen Pfad gespeichert.

-   **-limit `<number>`** \
    Maximal werden die als **`<number>`** angegebenen Datenbank im Sicherungsverzeichnis vorgehalten. Ältere überschüssige Sicherungsdateien werden automatisch aus dem Verzeichnis gelöscht.
    
-   **-delay `<seconds>`** \
    Die Datensicherung kann um die in **`<seconds>`** angegebenen Sekunden verzögert werden.
    
-   **-wait** \
    Nach erfolgter Ausführung wird das Programm nicht sofort beendet. Der Benutzer muss erst mit ENTER bestätigen, dass das Programm beendet werden soll.
    
-   **-dump** \
    Statt einer Kopie der Datenbank-Dateien wird ein Dump erzeugt.


#### Wiederherstellung der gesicherten Datenbank {#admin_backup_network_restore}

Eine Datensicherung ist eine Kopie der Datenbank-Dateien. Die Wiederherstellung dieser Daten ist relativ einfach.

1.  Beenden Sie den ImmoTool-Server, wenn dieser aktuell in Betrieb sein sollte.

2.  Sollte die Sicherung als ZIP-Archiv oder TAR.GZ-Archiv vorliegen, entpacken Sie diese Dateien auf Ihrem Rechner.

3.  Benennen Sie das betreffende Datenbank-Verzeichnis um und erstellen Sie ein neues / leeres Datenbank-Verzeichnis.

4.  Kopieren Sie die gesicherten Datenbank-Dateien **`db.data`**, **`db.lobs`**, **`db.properties`** & **`db.script`** in das Verzeichnis der jeweiligen Datenbank (siehe ["Daten-Verzeichnis des ImmoTool-Servers"]({{< relref "server/directories.md#admin_server_directories_data" >}})).

5.  Starten Sie den ImmoTool-Server neu, um mit der wiederhergestellten Datenbank weiterarbeiten zu können.

Das in Schritt 3 umbenannte alte Datenbank-Verzeichnis kann nach erfolgreicher Wiederherstellung bei Bedarf gelöscht werden.
