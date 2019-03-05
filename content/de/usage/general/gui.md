---

title: Die grafische Oberfläche des Programms
linktitle: Grafische Oberfläche
description: Die grafische Oberfläche von OpenEstate-ImmoTool…
weight: 10

menu:
  main:
    parent: usage-general
    identifier: usage-general-gui

---


## Die grafische Oberfläche des Programms {#usage_general_gui}
  

### Das Programm-Fenster {#usage_general_gui_window}

Nachdem ein Projekt erstellt und im ImmoTool geöffnet wurde wird ein Programm-Fenster dargestellt, das ungefähr wie folgt aussieht:

{{< figure src="gui.png" caption="Programm-Fenster des ImmoTools" >}}

Das Programm-Fenster besteht aus den folgenden Elementen:

1.  **Hauptmenü**

    Über das Hauptmenü können die Funktionen des Programmes direkt aufgerufen werden.

    Die installierten / aktivierten Add-Ons können bei Bedarf Einträge in das Hauptmenü einfügen.

2.  **Ansichtsauswahl**

    Die verschiedenen Ansichten können in dieser Auswahlbox gewählt werden.

    Beim Wechsel der Ansicht werden im Ansichtsbereich (4) weitere Einträge in einer *Baumansicht* dargestellt.

3.  **Ansichtsmenü**

    Für die in (2) gewählte Ansicht wird ein Menü mit weiteren Aktionen dargestellt, wenn Sie auf diesen Button klicken.

    Die Einträge im erzeugten Menü hängen davon ab, welche Auswahl im Ansichtsbereich (4) getätigt wurde. Alternativ kann das Ansichtsmenü durch Klick mit rechter Maustaste in den Ansichtsbereich (4) geöffnet werden.

4.  **Ansichtsbereich**

    Für die in (2) gewählte Ansicht werden in diesem Bereich verschiedene Informationen zur weiteren Bearbeitung dargestellt.

5.  **Hauptbereich**

    In diesem Bereich werden die Informationen aus der Datenbank dargestellt und bearbeitet.

    Es können beliebig viele Reiter / Tabs im Hauptbereich dargestellt werden. Durch Klick auf das *rote X* (oder via Hauptmenü F8 Programm Tab schließen) kann ein geöffneter Reiter / Tab im Hauptbereich geschlossen werden.

6.  **Kalenderbereich**

    Der aktuelle Kalender wird dargestellt.

    Aktuelle Termine werden farblich im Kalender hervorgehoben und können durch Doppelklick geöffnet werden.

7.  **Statusmeldung**

    Wenn eine Aufgabe im Hintergrund ausgeführt wird, werden an dieser Stelle Status-Meldungen dargestellt.

    Wenn keine Prozesse im Hintergrund arbeiten (oder keine Status-Meldungen gesendet werden) wird der Firmen-Name des aktuellen Projektes dargestellt.

8.  **Fortschrittsbalken**

    Während eine Aufgabe im Hintergrund ausgeführt wird, findet an dieser eine optische Rückmeldung statt.

9.  **Benachrichtigung / Balloon-Message**

    Eine ausgeführte Aufgabe kann Rückmeldungen liefern, die im Programm als Information dargestellt werden.

    Nach einer Zeitspanne von 30 Sekunden wird die Benachrichtigung automatisch ausgeblendet. Es werden die letzten fünf Benachrichtigungen angezeigt. Wenn man die Benachrichtigung explizit schließt (durch Klick auf das *rote X*), werden die fünf zuletzt dargestellten Benachrichtigungen geleert.

{{< todo >}}
Bereiche beschreiben
{{< /todo >}}


### Verwendung von Tabellen {#usage_general_gui_tables}

An verschiedenen Stellen werden Tabellen innerhalb des Programmes dargestellt.

{{< figure src="table.png" caption="Tabellenansicht einrichten" >}}

Verschiedene Standardfunktionen sind in den Tabellen enthalten.

-   **Zeilen umsortieren**
    Durch einen Klick mit der linken Maustaste auf einen Spalten-Titel in der Tabelle, kann nach dieser Spalte auf- oder absteigend sortiert werden. Ein kleiner Pfeil neben dem Spalten-Titel zeigt die aktuelle Richtung der Sortierung an.

-   **Spalten umsortieren**
    Wenn mit der linken Maustaste auf einen Spalten-Titel in der Tabelle geklickt und die Taste gehalten wird, kann die Spalte innerhalb der Tabelle verschoben werden (Drag & Drop).

-   **Spalten ein- & ausblenden**
    Zum Ein- oder Ausblenden einer Spalte klicken Sie rechts von den Spalten-Titeln auf das Tabellen-Symbol um das Menü der Tabelle zu öffnen. Aktivieren oder deaktivieren Sie die entsprechende Spalte durch Klick auf den gewünschten Spalten-Titel.

-   **Einstellungen speichern**
    Um Änderungen dauerhaft zu speichern klicken Sie rechts von den Spalten-Titeln auf das Tabellen-Symbol und klicken auf `Einstellungen zur Tabelle merken`.

-   **Tabelle exportieren**
    Um die aktuelle Tabelle als CSV-, Excel oder PDF-Tabelle zu speichern klicken Sie rechts von den Spalten-Titeln auf das Tabellen-Symbol und wählen unter `Tabelle exportieren` das gewünschte Format, wählen iḿ sich öffnenden Fenster den Speicherort und speichern die Datei.
    
{{< info >}}
Die beschriebenen Tabellen-Funktionen werden in den meisten - aber nicht in allen Tabellen - unterstützt.
{{< /info >}}


### Verwendung von Formularen {#usage_general_gui_forms}

Um Eingaben zu tätigen, werden an verschiedenen Stellen im Programm Formulare dargestellt.

{{< figure src="form.png" caption="Farbliche Markierung der Formularfelder" >}}

{{< todo >}}
Bild einfügen
{{< /todo >}}

Die folgenden Standardfunktionen werden dabei verwendet.

-   **Pflichtfelder**
    Eingaben, die für eine weitere Verarbeitung zwingend notwendig sind, werden gelb hervorgehoben.

-   **Ungültige Eingaben**
    Ungültige Eingaben in einem Pflichtfeld werden rot hervorgehoben.

-   **Gültige Eingaben**
    Gültige Eingaben in einem Pflichtfeld werden grün hervorgehoben.

