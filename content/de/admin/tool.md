---

title: AdminTool
linktitle: AdminTool
description: Dokumentation zum von OpenEstate-AdminTool…
weight: 30

menu:
  main:
    parent: admin
    identifier: admin-tool

---

## AdminTool {#admin_tool}

Das AdminTool ist ein Hilfsprogramm zur Administration von ImmoTool-Datenbanken. Das Programm ist Bestandteil der ImmoTool-Installation und kann im `bin`-Verzeichnis durch Ausführung der Dateien `AdminTool.exe` / `AdminTool.bat` / `AdminTool.sh` gestartet werden.


### AdminTool starten {#admin_tool_startup}

Das AdminTool ist Bestandteil der ImmoTool-Installation und kann im `bin`-Verzeichnis durch Ausführung der Dateien `AdminTool.exe` / `AdminTool.bat` / `AdminTool.sh` gestartet werden.


### Verbindung zur Datenbank herstellen {#admin_tool_connect}

Um eine Verbindung mit einer ImmoTool-Datenbank herzustellen, wird zum Start des AdminTools das folgende Fenster dargestellt.

{{< figure src="tool_login.jpg" caption="Verbindung zu einer Datenbank mit dem AdminTool herstellen." >}}

Es gibt zwei Möglichkeiten, eine Verbindung zur Datenbank mit dem AdminTool herzustellen:

1.  Die Datenbank eines bestehenden Projektes (Einzelplatz oder Mehrplatz) kann geöffnet werden. Dafür muss dem Programm lediglich das Projektverzeichnis auf der Festplatte mitgeteilt werden. Klicken Sie dafür auf den Button `Auswahl`.

    {{< figure src="tool_login_local.jpg" caption="Verbindungsaufbau via AdminTool durch Auswahl eines Projektes" >}}

    Sollte es sich um ein Mehrplatz-Projekt handeln, muss zusätzlich `Benutzer` und `Passwort` des Administrators (in der Regel Benutzer `SA`) eingegeben werden.

2.  Es kann eine direkte Verbindung zu einem ImmoTool-Server hergestellt werden, indem dessen Verbindungsdaten sowie die Zugangsdaten des Administrators eingegeben werden.

    {{< figure src="tool_login_remote.jpg" caption="Verbindungsaufbau via AdminTool durch direkte Eingabe der Verbindungsdaten" >}}


### Werkzeugleiste {#admin_tool_toolbar}

Das AdminTool stellt verschiedene Funktionen in der Werkzeugleiste zur Verfügung.

{{< figure src="tool_toolbar.jpg" caption="Werkzeugleiste im AdminTool" >}}

-   **DB öffnen**
    Öffnet eine Verbindung zu einer Datenbank. Eine eventuell bereits geöffnete Datenbank-Verbindung wird geschlossen.

-   **DB schließen**
    Wenn eine Datenbank-Verbindung geöffnet ist, wird diese geschlossen.

-   **Aktualisieren**
    Alle dargestellten Reiter werden aktualisiert.


### Firmendaten bearbeiten {#admin_tool_company}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab `Anbieter` die Firmendaten und das Firmenlogo des Projekts eingesehen und bearbeitet werden.

{{< figure src="tool_company-01.jpg" caption="Firmendaten im AdminTool bearbeiten" >}}

-   Klicken Sie im Tab auf `Aktualisieren` um die Firmendaten aus der Datenbank erneut zu ermitteln.
-   Klicken Sie im Tab auf `Übernehmen` um geänderte Firmendaten dauerhaft in der Datenbank zu speichern.


### Add-Ons bearbeiten {#admin_tool_addons}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab `Add-Ons` die verfügbaren und im Projekt installierten Add-Ons eingesehen und bearbeitet werden.

-   Klicken Sie im Tab auf `Aktualisieren` um die Add-Ons aus der Datenbank erneut zu ermitteln.

#### Installierte Add-Ons verwalten {#admin_tool_addons_installed}

Im Tab `Add-Ons` wird unter `Installierte Add-Ons` eine tabellarische Übersicht der aktuell installierten Add-Ons dargestellt.

{{< figure src="tool_addons-01.jpg" caption="Übersicht der installierten Add-Ons" >}}

-   In der Spalte `Add-On` wird der interne Name des jeweiligen Add-Ons dargestellt.
-   In der Spalte `Version` wird die aktuell in der Datenbank installierte Version des Add-Ons dargestellt.
-   In der Spalte `Aktiv` wird dargestellt, ob das jeweilige Add-On in der Datenbank installiert wurde.


##### Add-Ons (de)aktivieren {#admin_tool_addons_installed_enable}

Um ein Add-On im Projekt verwenden zu können, muss dieses durch die Administration aktiviert worden sein.

Klicken Sie dafür in der Tabellenspalte `Aktiv` auf die jeweilige Zeile um ein Add-On zu aktivieren. Eine Änderung muss durch Klick auf `Speichern` bestätigt werden.


##### Add-Ons deinstallieren {#admin_tool_addons_installed_uninstall}

Markieren Sie ein Add-On in der Tabelle und klicken Sie auf `Deinstallieren` um das gewählte Add-On komplett aus der Datenbank zu entfernen.

{{< warning >}}
Bei der Deinstallation gehen sämtliche Daten verloren, die eventuell bereits mit dem Add-On erfasst worden sind.
{{< /warning >}}


#### Aktualisierbare Add-Ons verwalten {#admin_tool_addons_updates}

Im Tab `Add-Ons` wird unter `Aktualisierungen` eine tabellarische Übersicht der Add-Ons dargestellt,

-   die vom AdminTool beim Programmstart gefunden wurden aber noch nicht in der Datenbank installiert sind.
-   die vom AdminTool beim Programmstart gefunden wurden und in der Datenbank in einer älteren Version installiert sind.

{{< figure src="tool_addons-02.jpg" caption="Übersicht der aktualisierbaren Add-Ons" >}}

-   In der Spalte `Add-On` wird der interne Name des jeweiligen Add-Ons dargestellt.
-   In der Spalte `installierte Version` wird die aktuell installierte Version des Add-Ons in der Datenbank dargestellt, wenn es bereits installiert wurde.
-   In der Spalte `neue Version` wird die lokal verfügbare Version des Add-Ons dargestellt.
-   In der Spalte `Installation` kann markiert werden, dass die Installation / Aktualisierung des jeweiligen Add-Ons durchgeführt werden soll.

Klicken Sie in der Tabellenspalte `Installation` auf die jeweilige Zeile um ein Add-On zu installieren / aktualisieren. Der Vorgang wird durch Klick auf `Installation` gestartet.

{{< info >}}
Ein Add-On kann im ImmoTool nur verwendet werden, wenn die in der Datenbank installierte Version mit der lokal verfügbaren Version übereinstimmt.
{{< /info >}}


### Benutzer bearbeiten {#admin_tool_users}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab `Benutzer` die Benutzerkonten der Datenbank eingesehen / bearbeitet werden. Allgemein können beliebig viele Benutzer können auf die Datenbank zugreifen und gemeinsam an einem Projekt arbeiten.

{{< figure src="tool_users-01.jpg" caption="Benutzerkonten bearbeiten" >}}

Auf der linken Seite eine Liste der aktuell vorhandenen Benutzerkonten dargestellt. Klicken Sie auf einen der Benutzer um diesen zur Bearbeitung auszuwählen.

Auf der rechten Seite der Ansicht werden Informationen zu dem aktuell ausgewählten Benutzer dargestellt.

Folgende Aktionen können über die Buttons oberhalb der Benutzer-Ansicht ausgeführt werden:

-   Klicken Sie im Tab auf `Aktualisieren` um die aktuelle Ansicht aktualisieren.
-   Klicken Sie im Tab auf `Neuer Benutzer` um einen neuen Benutzer zu erfassen.
-   Klicken Sie im Tab auf `Entfernen` um den aktuell gewählten Benutzer zu entfernen.
-   Klicken Sie im Tab auf `Übernehmen` um die vorgenommenen Änderungen in der Benutzer-Ansicht dauerhaft speichern.

{{< info >}}
Bitte beachten Sie, dass Sie nach jeder Änderung abschließend auf `Übernehmen` klicken sollten. Andernfalls wird die zwischenzeitliche Änderung nicht gespeichert und geht verloren.
{{< /info >}}


#### Eckdaten des Benutzers {#admin_tool_users_general}

Wenn ein Benutzerkonto zur Bearbeitung ausgewählt wurde, werden dessen Eckdaten auf der rechten Seite im Tab `Benutzer` dargestellt.

{{< figure src="tool_users-02.jpg" caption="Eckdaten eines Benutzers" >}}

-   **Login des Benutzers**
    Mit diesem Namen meldet sich der Benutzer an der Datenbank an. Der gewählte Name darf nicht doppelt vergeben werden.

-   **Passwort des Benutzers**
    Mit diesem Passwort meldet sich der Benutzer beim Start des ImmoTools auf der Datenbank an. Markieren Sie das Feld ändern, um nachträglich ein neues Passwort zuzuordnen.

-   **Benutzer ist freigeschaltet**
    Mit dieser Option kann dem Benutzer die Berechtigung zur Anmeldung auf der Datenbank erteilt oder entzogen werden.

-   **Benutzer ist Administrator**
    Mit dieser Option werden dem Benutzer sämtliche Zugriffsrechte in dem Projekt erteilt. Der Benutzer darf damit auf alle Daten zugreifen, weitere Benutzer anlegen, Add-Ons installieren etc.

-   **Notizen zum Benutzer**
    An dieser Stelle können bei Bedarf Anmerkungen und Notizen zu einem Benutzerkonto hinterlegt werden.

-   **Effektive Berechtigungen**
    In der Tabelle werden die Berechtigungen des Benutzers dargestellt, die ihm direkt zugewiesen wurden oder die er durch Zuweisung von Gruppen geerbt hat.


#### Personendaten des Benutzers {#admin_tool_users_person}

Wenn ein Benutzerkonto zur Bearbeitung ausgewählt wurde, werden dessen Personendaten auf der rechten Seite im Tab `Person` dargestellt.

{{< figure src="tool_users-03.jpg" caption="Personendaten eines Benutzers" >}}

{{< info >}}
Die hier hinterlegten Personendaten kann der Benutzer nachträglich via ImmoTool bearbeiten (wenn die nötigen Rechte vorhanden sind).
{{< /info >}}


#### Gruppen des Benutzers {#admin_tool_users_groups}

Wenn ein Benutzerkonto zur Bearbeitung ausgewählt wurde, werden dessen Gruppen-Mitgliedschaften auf der rechten Seite im Tab `Gruppen` dargestellt.

{{< figure src="tool_users-04.jpg" caption="Gruppen eines Benutzers" >}}

In der Tabelle werden die aktuell in der Datenbank registrierten Gruppen dargestellt. Durch Klick in die Spalte `Zuweisung` können dem Benutzer eine oder mehrere Gruppen zugewiesen werden.

{{< info >}}
Ein Benutzer erbt die Berechtigungen aus den ihm zugewiesenen Gruppen.
{{< /info >}}


#### Berechtigungen des Benutzers {#admin_tool_users_permissions}

Wenn ein Benutzerkonto zur Bearbeitung ausgewählt wurde, werden dessen Berechtigungen auf der rechten Seite im Tab `Berechtigungen` dargestellt.

{{< figure src="tool_users-05.jpg" caption="Berechtigungen eines Benutzers" >}}

In der Tabelle werden die von den Add-Ons bereitgestellten Berechtigungen dargestellt. Durch Klick in die Spalte `Aktiv` können dem Benutzer eine oder mehrere Berechtigungen zugewiesen werden.


### Gruppen bearbeiten {#admin_tool_groups}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab `Gruppen` die Benutzergruppen der Datenbank eingesehen / bearbeitet werden.

Allgemein können die Benutzer können in mehrere Gruppen zusammengefasst werden. Durch die Mitgliedschaft eines Benutzers in einer Gruppe erbt dieser die in der Gruppe hinterlegten Berechtigungen.

{{< figure src="tool_groups-01.jpg" caption="Benutzergruppen bearbeiten" >}}

In der Ansicht wird auf der linken Seite eine Liste der aktuell vorhandenen Gruppen dargestellt. Klicken Sie auf eine der Gruppen um diese zur Bearbeitung auszuwählen.

Auf der rechten Seite der Gruppen-Ansicht werden Informationen zu der aktuell ausgewählten Gruppe dargestellt.

Folgende Aktionen können über die Buttons oberhalb der Gruppen-Ansicht ausgeführt werden:

-   Klicken Sie im Tab auf `Aktualisieren` um die aktuelle Ansicht aktualisieren.
-   Klicken Sie im Tab auf `Neuer Gruppe` um einen neue Gruppe zu erfassen.
-   Klicken Sie im Tab auf `Entfernen` um die aktuell gewählte Gruppe zu entfernen.
-   Klicken Sie im Tab auf `Übernehmen` um die vorgenommenen Änderungen in der Gruppen-Ansicht dauerhaft speichern.

{{< info >}}
Bitte beachten Sie, dass Sie nach jeder Änderung abschließend auf `Übernehmen` klicken sollten. Andernfalls wird die zwischenzeitliche Änderung nicht gespeichert und geht verloren.
{{< /info >}}


#### Eckdaten der Gruppe {#admin_tool_groups_general}

Wenn eine Benutzergruppe zur Bearbeitung ausgewählt wurde, werden dessen Eckdaten auf der rechten Seite im Tab `Gruppe` dargestellt.

{{< figure src="tool_groups-02.jpg" caption="Eckdaten einer Benutzergruppe" >}}

-   **Name der Gruppe**
    Tragen Sie eine Bezeichnung für die Gruppe ein, sodass Sie diese später besser wiedererkennen.

-   **Notizen zur Gruppe**
    An dieser Stelle können bei Bedarf Anmerkungen und Notizen zu einer Gruppe hinterlegt werden.


#### Benutzer zuweisen {#admin_tool_groups_users}

Wenn eine Benutzergruppe zur Bearbeitung ausgewählt wurde, werden die zugewiesenen Benutzerkonten auf der rechten Seite im Tab `Mitglieder` dargestellt.

{{< figure src="tool_groups-03.jpg" caption="Mitglieder einer Benutzergruppe" >}}

In der Tabelle werden die aktuell in der Datenbank registrierten Benutzer dargestellt. Durch Klick in die Spalte `Zuweisung` können der Gruppe eine oder mehrere Benutzer als Mitglied zugewiesen werden.

{{< info >}}
Jeder Benutzer, der einer Gruppe als Mitglied zugewiesen wurde, erhält automatisch alle Berechtigungen der Gruppe.
{{< /info >}}


#### Berechtigungen erteilen {#admin_tool_groups_permissions}

Wenn eine Benutzergruppe zur Bearbeitung ausgewählt wurde, werden die Berechtigungen auf der rechten Seite im Tab `Berechtigungen` dargestellt.

{{< figure src="tool_groups-04.jpg" caption="Berechtigungen einer Benutzergruppe" >}}

In der Tabelle werden die von den Add-Ons bereitgestellten Berechtigungen dargestellt. Durch Klick in die Spalte `Aktiv` können der Gruppe eine oder mehrere Berechtigungen zugewiesen werden.

{{< info >}}
Jeder Benutzer, der einer Gruppe als Mitglied zugewiesen wurde, erhält automatisch alle Berechtigungen dieser Gruppe.
{{< /info >}}


### Inhalte der Datenbank anzeigen {#admin_tool_browser}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab `SQL-Browser` die rohen Inhalte der Datenbank eingesehen werden ("Tabellen", "Views" & "Stored Procedures").

{{< figure src="tool_browser-01.jpg" caption="Inhalte der Datenbank anzeigen" >}}


### SQL-Befehle auf der Datenbank ausführen {#admin_tool_console}

Nachdem eine Verbindung zur Datenbank hergestellt wurde können im Tab `SQL-Konsole` beliebige SQL-Anfragen auf der Datenbank ausgeführt werden.

{{< figure src="tool_console-01.jpg" caption="SQL-Befehle im AdminTool ausführen" >}}

{{< warning >}}
Verwenden Sie diese Funktion mit Bedacht. Ein falscher Eingriff kann die Datenbank beschädigen.
{{< /warning >}}
