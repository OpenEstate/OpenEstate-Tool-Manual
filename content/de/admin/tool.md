---

title: Verwendung von AdminTool
linktitle: AdminTool
description: Wie eine Datenbank von OpenEstate-ImmoTool mit dem AdminTool verwaltet werden kann…
weight: 30

menu:
  main:
    parent: admin
    identifier: admin-tool

---

## AdminTool {#admin_tool}

Das AdminTool ist ein **Hilfsprogramm für Administratoren** zur Verwaltung der Datenbank des ImmoTools. In der Regel wird das Programm nur bei [Netzwerk-Installationen]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) benötigt - z.B.

-   um eine neue Datenbank zur Verwendung mit dem ImmoTool vorzubereiten,
-   um ImmoTool-Benutzer in der Datenbank anzulegen,
-   um Berechtigungen für ImmoTool-Benutzer zu vergeben oder
-   um Operationen direkt auf der Datenbank durchzuführen.


### AdminTool starten {#admin_tool_startup}

Mit Installation des ImmoTools steht Ihnen auch das AdminTool zur Verfügung (siehe ["ImmoTool installieren"]({{< relref "../intro/install_client.md#intro_install_client" >}})).


#### AdminTool unter Windows starten {#admin_tool_startup_windows}

Im Startmenü finden Sie einen Ordner namens **"OpenEstate-ImmoTool"**, der eine Verknüpfung zum Start des AdminTools enthält.

Darüber hinaus können Sie das Programm auch über die Datei **`AdminTool.exe`** (bzw. **`AdminTool.bat`**) im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "client/directories.md#admin_client_directories_application" >}}) starten.


#### AdminTool unter macOS starten {#admin_tool_startup_mac}

Führen Sie einen Doppelklick auf das Programmsymbol mit der Bezeichnung **"OpenEstate-ImmoTool"** aus. Es öffnet sich daraufhin der Finder mit den vom ImmoTool bereitgestellten Programmen.

{{< figure src="client/startup_mac_folder.png" caption="Starter für AdminTool im Finder" >}}

Wenn Sie in diesem Fenster auf das Symbol **"AdminTool"** klicken, wird das Programm gestartet.

{{< tip >}}
Bei Bedarf können Sie das Programmsymbol **"AdminTool"** ins Dock integrieren, um dieses später schnell und unkompliziert starten zu können (siehe [Anleitung bei Apple](https://support.apple.com/de-de/HT201730)).
{{< /tip >}}

Um das AdminTool unter macOS via Terminal zu starten, kann das Skript **`AdminTool.sh`** im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "client/directories.md#admin_client_directories_application" >}}) verwendet werden.


#### AdminTool unter Linux starten {#admin_tool_startup_linux}

Wenn das ImmoTool mit dem [**Debian**-Paket]({{< relref "../intro/install_client.md#intro_install_client_setup_debian" >}}) installiert wurde, finden Sie im Startmenü die Einträge für den Start des Programms unter dem Namen **"OpenEstate-AdminTool"**.

Wenn das ImmoTool mit dem [**TAR.GZ**-Paket]({{< relref "../intro/install_client.md#intro_install_client_setup_linux" >}}) installiert wurde, müssen Sie ggf. vorher noch die Datei **`StartMenuAdd.sh`** im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "client/directories.md#admin_client_directories_application" >}}) ausführen um die Einträge im Startmenü zu erzeugen.

Alternativ zum Startmenü kann das Programm über die Datei **`AdminTool.sh`** im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "client/directories.md#admin_client_directories_application" >}}) gestartet werden.


### Verbindung zur Datenbank herstellen {#admin_tool_connect}

Beim Start des AdminTools wird das folgende Fenster dargestellt, über welches eine Verbindung zu einer Datenbank hergestellt werden kann:

{{< figure src="tool_connect.png" caption="Verbindung zu einer Datenbank herstellen" >}}

Es gibt zwei Möglichkeiten, eine Verbindung zu einer Datenbank mit dem AdminTool herzustellen.


#### Datenbank eines Projekts öffnen {#admin_tool_connect_project}

Die Datenbank eines bestehenden Projekts (Einzelplatz oder Mehrplatz) kann geöffnet werden. Dafür muss dem Programm lediglich das [Projekt-Verzeichnis]({{< relref "client/directories.md#admin_client_directories_project" >}}) auf der Festplatte mitgeteilt werden. Klicken Sie dafür auf den Button **"Auswählen"**.

{{< figure src="tool_connect_project.png" caption="Verbindungsaufbau durch Auswahl eines Projekts" >}}

Beim Verbindungsaufbau zur Datenbank werden in diesem Falle automatisch die Projekt-Einstellungen übernommen.

Sollte es sich um ein Mehrplatz-Projekt ([Netzwerk-Installation]({{< relref "../intro/install_types.md#intro_install_types_network" >}})) handeln, müssen zusätzlich in den Eingabefeldern **"Benutzer"** und **"Passwort"** die Zugangsdaten des Administrators eingetragen werden. Der Benutzername des Datenbank-Administrators lautet in der Regel **"SA"**.


#### Direkte Verbindung zum ImmoTool-Server herstellen {#admin_tool_connect_server}

Es kann eine direkte Verbindung zu einem ImmoTool-Server hergestellt werden. In diesem Falle müssen Verbindungsdaten sowie die Zugangsdaten des Administrators vollständig eingetragen werden.

{{< figure src="tool_connect_remote.png" caption="Verbindungsaufbau durch direkte Eingabe der Verbindungsdaten" >}}

Folgende Einstellungen können vorgenommen werden:

-   **Datenbank:** \
     Hier sollte die Option **"HSQL.remote"** gewählt werden.

-   **Protokoll:** \
     Im Normalfall muss hier **"hsql"** gewählt werden. Wenn eine Verschlüsselung auf dem Server eingerichtet wurde, muss hier **"hsqls"** gewählt werden (siehe ["SSL-Verschlüsselung einrichten"]({{< relref "server/setup.md#admin_server_setup_ssl" >}})).

-   **Hostname:** \
     Hier muss die IP-Adresse oder der Hostname des Rechners eingetragen werden, auf dem der ImmoTool-Server betrieben wird. Wenn das AdminTool vom gleichen Rechner gestartet wurde auf dem sich auch der ImmoTool-Server befindet, kann der Hostname **"localhost"** unverändert bleiben.

-   **Port-Nr:** \
     Die Port-Nummer lautet standardmäßig **"9001"**. Nur wenn im ImmoTool-Server ein anderer Wert konfiguriert wurde, muss der Standard-Wert geändert werden.

-   **DB-Name:** \
     Der Name der Datenbank lautet standardmäßig **"immotool"**. Nur wenn im ImmoTool-Server eine Datenbank unter einem anderen Namen konfiguriert wurde, muss der Standard-Wert geändert werden.

-   **Benutzer:** \
    Der Name des Administrator-Benutzers lautet **"SA"** und muss in der Regel nicht geändert werden.

-   **Passwort:** \
    Beim ersten Verbindungsaufbau mit dem ImmoTool-Server ist das Passwort leer. Nachdem ein Passwort in der Datenbank hinterlegt wurde, muss dieses hier eingetragen werden.


### Werkzeugleiste {#admin_tool_toolbar}

Das AdminTool stellt verschiedene Funktionen in der Werkzeugleiste zur Verfügung.

{{< figure src="tool_icons.png" caption="Werkzeugleiste im AdminTool" >}}

-   **DB öffnen:** \
    Öffnet eine Verbindung zu einer Datenbank. Eine eventuell bereits geöffnete Datenbank-Verbindung wird geschlossen.

-   **DB schließen:** \
    Wenn eine Datenbank-Verbindung geöffnet ist, wird diese geschlossen.

-   **Aktualisieren:** \
    Alle dargestellten Tabs werden aktualisiert.


### Firmendaten bearbeiten {#admin_tool_company}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab **"Agentur"** die Firmendaten und das Firmenlogo des Projekts eingesehen und bearbeitet werden.

{{< figure src="tool_agency.png" caption="Firmendaten im AdminTool bearbeiten" >}}

-   Klicken Sie im Tab auf **"Aktualisieren"** um die Firmendaten aus der Datenbank erneut zu ermitteln.
-   Klicken Sie im Tab auf **"Übernehmen"** um geänderte Firmendaten dauerhaft in der Datenbank zu speichern.


### Add-Ons bearbeiten {#admin_tool_addons}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab **"Add-Ons"** die verfügbaren und im Projekt installierten Add-Ons bearbeitet werden.

-   Klicken Sie im Tab auf **"Aktualisieren"** um die Übersicht der Add-Ons neu zu laden.

#### Installierte Add-Ons verwalten {#admin_tool_addons_installed}

Im Tab **"Installierte Add-Ons"** wird eine tabellarische Übersicht der aktuell im Projekt installierten Add-Ons dargestellt.

{{< figure src="tool_addons_installed.png" caption="Übersicht der installierten Add-Ons" >}}


##### Add-Ons (de)aktivieren {#admin_tool_addons_installed_enable}

Um ein installiertes Add-On im Projekt verwenden zu können, muss dieses durch die Administration aktiviert worden sein.

Aktivieren oder deaktivieren Sie dafür in der Tabellenspalte **"aktiv"** die Check-Box für das betreffende Add-On und klicken Sie danach auf den Button **"Änderungen speichern"**.


##### Add-Ons deinstallieren {#admin_tool_addons_installed_uninstall}

Markieren Sie das zu deinstallierende Add-On in der Tabelle durch Klick auf die jeweilige Zeile. Klicken Sie danach auf **"Deinstallation durchführen"** um das gewählte Add-On komplett aus der Datenbank zu entfernen.

{{< warning >}}
Bei der Deinstallation gehen sämtliche Daten verloren, die eventuell bereits mit dem Add-On erfasst worden sind.
{{< /warning >}}


#### Weitere Add-Ons installieren {#admin_tool_addons_other}

Einzelne Add-Ons können eventuell im [Plugin-Verzeichnis des ImmoTools]({{< relref "client/directories.md#admin_client_directories_plugins" >}}) vorhanden, aber noch nicht im Projekt installiert sein. Diese Add-Ons werden in der Tabelle im Reiter **"Weitere Add-Ons"** aufgelistet.

{{< figure src="tool_addons_other.png" caption="Übersicht der weiteren Add-Ons" >}}

Um ein Add-On aus dieser Tabelle zu installieren, aktivieren Sie in der Tabellenspalte **"Installieren"** die Check-Box für das betreffende Add-On und klicken Sie danach auf den Button **"Installation durchführen"**.


#### Add-Ons aktualisieren {#admin_tool_addons_updates}

Im Tab **"Aktualisierbare Add-Ons"** finden Sie tabellarische Übersicht von Add-Ons und Erweiterungen, die im Projekt installiert sind aber noch nicht auf die neueste vorliegende Version aktualisiert wurden. 

{{< figure src="tool_addons_updates.png" caption="Übersicht der aktualisierbaren Add-Ons" >}}

Um eine Aktualisierung aus dieser Tabelle durchzuführen, markieren Sie die betreffende Zeile in der Tabelle und klicken Sie danach auf den Button **"Aktualisierung durchführen"**.

{{< info >}}
Ein Add-On kann im ImmoTool nur verwendet werden, wenn die in der Datenbank installierte API-Version mit der auf der Festplatte verfügbaren API-Version übereinstimmt.
{{< /info >}}


### Benutzer bearbeiten {#admin_tool_users}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab **"Benutzer"** die Benutzerkonten der Datenbank eingesehen / bearbeitet werden. Bei [Netzwerk-Installationen]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) können beliebig viele Benutzer auf die Datenbank zugreifen und gemeinsam an einem Projekt arbeiten.

{{< figure src="tool_users.png" caption="Benutzerkonten bearbeiten" >}}

Auf der linken Seite wird eine Liste der aktuell vorhandenen Benutzerkonten dargestellt. Klicken Sie auf einen der Benutzer um diesen zur Bearbeitung auszuwählen.

Auf der rechten Seite der Ansicht werden Informationen zum aktuell ausgewählten Benutzer dargestellt.

Folgende Aktionen können über die Buttons oberhalb der Benutzer-Ansicht ausgeführt werden:

-   Klicken Sie auf **"Aktualisieren"** um die aktuelle Ansicht aktualisieren.
-   Klicken Sie auf **"Neuer Benutzer"** um einen neuen Benutzer zu erfassen.
-   Klicken Sie auf **"Benutzer entfernen"** um den aktuell gewählten Benutzer zu entfernen.
-   Klicken Sie auf **"Übernehmen"** um die vorgenommenen Änderungen an einem Benutzerkonto dauerhaft speichern.

{{< info >}}
Bitte beachten Sie, dass Sie nach jeder Änderung abschließend auf **"Übernehmen"** klicken sollten. Andernfalls wird die zwischenzeitliche Änderung nicht gespeichert und geht verloren.
{{< /info >}}


#### Eckdaten des Benutzers {#admin_tool_users_general}

Wenn ein Benutzerkonto zur Bearbeitung ausgewählt wurde, werden dessen Eckdaten auf der rechten Seite im Tab **"Benutzer"** dargestellt.

{{< figure src="tool_users_general.png" caption="Eckdaten eines Benutzers" >}}

-   **Login des Benutzers:** \
    Mit diesem Namen meldet sich der Benutzer an der Datenbank an. Der gewählte Name darf innerhalb eines Projekts nicht doppelt vergeben werden.

-   **Passwort des Benutzers:** \
    Mit diesem Passwort meldet sich der Benutzer beim Start des ImmoTools auf der Datenbank an. Aktivieren Sie die Check-Box **"Passwort ändern."** um nachträglich ein neues Passwort einzutragen.

-   **Benutzer ist freigeschaltet:** \
    Mit dieser Option kann dem Benutzer die Berechtigung zur Anmeldung auf der Datenbank erteilt oder entzogen werden. Freigeschaltete Benutzer werden automatisch zum Mitglied der Gruppe **"IMMOTOOL"**.

-   **Benutzer ist Administrator:** \
    Mit dieser Option werden dem Benutzer alle Zugriffsrechte in dem Projekt erteilt. Der Benutzer darf damit auf alle Daten zugreifen, weitere Benutzer anlegen, Add-Ons installieren etc. Einem Administrator müssen keine Berechtigungen zugewiesen werden, da dieser immer alle Berechtigungen besitzt.

-   **Notizen zum Benutzer:** \
    An dieser Stelle können bei Bedarf Anmerkungen und Notizen zu einem Benutzerkonto hinterlegt werden.

-   **Effektive Berechtigungen:** \
    In der Tabelle werden die Berechtigungen des Benutzers dargestellt, die ihm direkt zugewiesen wurden oder die er durch Zuweisung von Gruppen erhalten hat.

{{< warning >}}
Sollten Sie die Datenbank einer [Einzelplatz-Installation]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) im AdminTool verwalten, ändern Sie nicht das Passwort des Benutzers **"SA"**. Das Passwort sollte in diesem Falle grundsätzlich immer leer sein.
{{< /warning >}}


#### Personendaten des Benutzers {#admin_tool_users_person}

Wenn ein Benutzerkonto zur Bearbeitung ausgewählt wurde, werden dessen Personendaten auf der rechten Seite im Tab **"Person"** dargestellt.

{{< figure src="tool_users_person.png" caption="Personendaten eines Benutzers" >}}

{{< info >}}
Die hier hinterlegten Personendaten kann der Benutzer nachträglich via ImmoTool bearbeiten (wenn die nötigen Rechte vorhanden sind).
{{< /info >}}


#### Gruppen des Benutzers {#admin_tool_users_groups}

Wenn ein Benutzerkonto zur Bearbeitung ausgewählt wurde, werden dessen Gruppen-Mitgliedschaften auf der rechten Seite im Tab **"Gruppen"** dargestellt.

{{< figure src="tool_users_groups.png" caption="Gruppen eines Benutzers" >}}

In der Tabelle werden die aktuell in der Datenbank registrierten Gruppen dargestellt. Durch Klick in die Spalte **"zugewiesen"** können dem Benutzer eine oder mehrere Gruppen zugeteilt werden.

{{< info >}}
Ein Benutzer erhält die Berechtigungen aus den ihm zugewiesenen Gruppen.
{{< /info >}}

{{< info >}}
Ein Benutzer ist automatisch ein Mitglied der Gruppe **"IMMOTOOL"**, wenn dieser im Tab **"Benutzer"** aktiviert wurde.
{{< /info >}}


#### Berechtigungen des Benutzers {#admin_tool_users_permissions}

Wenn ein Benutzerkonto zur Bearbeitung ausgewählt wurde, werden die ihm direkt zugewiesenen Berechtigungen auf der rechten Seite im Tab **"Berechtigungen"** dargestellt.

{{< figure src="tool_users_permissions.png" caption="Berechtigungen eines Benutzers" >}}

In der Tabelle werden die von den Add-Ons bereitgestellten Berechtigungen dargestellt. Durch Klick in die Spalte **"zugewiesen"** können dem Benutzer die gewünschten Berechtigungen erteilt werden.

{{< tip >}}
Statt einem Benutzer bestimmte Berechtigungen direkt zuzuweisen, können Sie auch Gruppen anlegen. Die Berechtigungen müssen dann nur einmal der Gruppe zugewiesen werden und alle Mitglieder dieser Gruppe erhalten diese Berechtigungen automatisch.
{{< /tip >}}


### Gruppen bearbeiten {#admin_tool_groups}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab **"Gruppen"** die Benutzergruppen der Datenbank eingesehen / bearbeitet werden.

Allgemein können die Benutzer in mehrere Gruppen zusammengefasst werden. Durch die Mitgliedschaft eines Benutzers in einer Gruppe erhält dieser automatisch alle in der Gruppe hinterlegten Berechtigungen.

{{< figure src="tool_groups.png" caption="Benutzergruppen bearbeiten" >}}

In der Ansicht wird auf der linken Seite eine Liste der aktuell vorhandenen Gruppen dargestellt. Klicken Sie auf eine der Gruppen um diese zur Bearbeitung auszuwählen.

Auf der rechten Seite der Gruppen-Ansicht werden Informationen zu der aktuell ausgewählten Gruppe dargestellt.

Folgende Aktionen können über die Buttons oberhalb der Gruppen-Ansicht ausgeführt werden:

-   Klicken Sie im Tab auf **"Aktualisieren"** um die aktuelle Ansicht aktualisieren.
-   Klicken Sie im Tab auf **"Neue Gruppe"** um einen neue Gruppe zu erfassen.
-   Klicken Sie im Tab auf **"Gruppe entfernen"** um die aktuell gewählte Gruppe zu entfernen.
-   Klicken Sie im Tab auf **"Übernehmen"** um die vorgenommenen Änderungen an einer Gruppe dauerhaft zu speichern.

{{< info >}}
Bitte beachten Sie, dass Sie nach jeder Änderung abschließend auf **"Übernehmen"** klicken sollten. Andernfalls wird die zwischenzeitliche Änderung nicht gespeichert und geht verloren.
{{< /info >}}


#### Eckdaten der Gruppe {#admin_tool_groups_general}

Wenn eine Benutzergruppe zur Bearbeitung ausgewählt wurde, werden deren Eckdaten auf der rechten Seite im Tab **"Gruppe"** dargestellt.

{{< figure src="tool_groups_general.png" caption="Eckdaten einer Benutzergruppe" >}}

-   **Name der Gruppe:** \
    Tragen Sie eine Bezeichnung für die Gruppe ein, sodass Sie diese später besser wiedererkennen. Der gewählte Name darf innerhalb eines Projekts nicht doppelt vergeben werden.

-   **Notizen zur Gruppe:** \
    An dieser Stelle können bei Bedarf Anmerkungen und Notizen zu einer Gruppe hinterlegt werden.


#### Benutzer zuweisen {#admin_tool_groups_users}

Wenn eine Benutzergruppe zur Bearbeitung ausgewählt wurde, werden deren zugewiesene Benutzerkonten auf der rechten Seite im Tab **"Mitglieder"** dargestellt.

{{< figure src="tool_groups_users.png" caption="Mitglieder einer Benutzergruppe" >}}

In der Tabelle werden die aktuell in der Datenbank registrierten Benutzer dargestellt. Durch Klick in die Spalte **"zugewiesen"** können der Gruppe eine oder mehrere Benutzer als Mitglied zugewiesen werden.


#### Berechtigungen erteilen {#admin_tool_groups_permissions}

Wenn eine Benutzergruppe zur Bearbeitung ausgewählt wurde, werden deren Berechtigungen auf der rechten Seite im Tab **"Berechtigungen"** dargestellt.

{{< figure src="tool_groups_permissions.png" caption="Berechtigungen einer Benutzergruppe" >}}

In der Tabelle werden die von den Add-Ons bereitgestellten Berechtigungen dargestellt. Durch Klick in die Spalte **"zugewiesen"** können der Gruppe eine oder mehrere Berechtigungen zugewiesen werden.


### Inhalte der Datenbank anzeigen {#admin_tool_browser}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab **"SQL-Browser"** die rohen Inhalte der Datenbank eingesehen werden (Tabellen, Views und Stored Procedures).

{{< figure src="tool_browser.png" caption="Inhalte der Datenbank anzeigen" >}}

Diese Ansicht stellt keine weiteren besonderen Funktionen bereit und dient einzig der Überprüfung der Datenbank.


### SQL-Befehle auf der Datenbank ausführen {#admin_tool_console}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab **"SQL-Konsole"** beliebige SQL-Befehle auf der Datenbank ausgeführt werden.

{{< figure src="tool_console.png" caption="SQL-Befehle im AdminTool ausführen" >}}

{{< warning >}}
Verwenden Sie diese Funktion mit Bedacht. Ein falscher Eingriff kann die Datenbank beschädigen.
{{< /warning >}}

{{< info >}}
Eine Übersicht der unterstützten Befehle kann der [Dokumentation der HSQL-Datenbank](http://www.hsqldb.org/doc/2.0/guide/sql-ind.html) entnommen werden.
{{< /info >}}
