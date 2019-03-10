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

Nachdem ein Projekt erstellt und im ImmoTool geöffnet wurde wird ein Programm-Fenster dargestellt, das wie folgt aufgebaut ist:

{{< figure src="gui.png" caption="Programm-Fenster des ImmoTools" >}}

Im obigen Bildschirmfoto wurden die folgenden Bereiche des Programm-Fensters farblich markiert:

1.  **Hauptmenü:** \
    Über das Hauptmenü können die Funktionen des Programms direkt aufgerufen werden. Aktivierten Add-Ons können bei Bedarf Einträge in das Hauptmenü einfügen (z.B. **"Adressbuch"** oder **"Immobilien"**). 
    
    Wenn kein Projekt geöffnet ist, erscheinen im Hauptmenü nur die Menüs **"Programm"** und **"Extras"**.

2.  **Seitenleiste (Auswahl):** \
    Über die Seitenleiste können die verschiedenen Funktionen des Programms einfach angesteuert werden. Die aktivierten Add-Ons können Einträge in der Seitenleiste hinterlegen. Bei Klick auf eines der Symbole in der Seitenleiste wird rechts daneben eine Ansicht zur weiteren Verfeinerung der Auswahl dargestellt (z.B. für den Zugriff auf Immobiliendaten).
    
    Wenn kein Projekt geöffnet ist, wird die Seitenleiste mit der Auswahl **nicht** dargestellt.

3.  **Seitenleiste (Ansicht):** \
    Für die unter (2) getätigte Auswahl wird rechts neben der Symbolleiste eine Ansicht zum Zugriff auf die bereitgestellten Funktionen dargestellt. Abhängig von der Auswahl unter (2) kann in der Ansicht z.B. auf die Immobiliendaten, Kalendereinträge oder Kontaktdaten zugegriffen werden.

4.  **Hauptbereich:** \
    In diesem Bereich werden die im Programm werden die Formulare und Tabellen zur Verwaltung der vom Programm bereitgestellten Funktionen dargestellt. Wird über das Hauptmenü (1) oder die Seitenleiste (3) zum Beispiel die Immobilienübersicht gewählt, wird die Tablle mit den Immobiliendaten im Hauptbereich dargestellt.
    
    Es können mehrere Ansichten gleichzeitig im Hauptbereich dargestellt werden. Über sogenannte Tabs oberhalb des Hauptbereichs kann zwischen den Ansichten gewechselt werden.
    
    Ein Tab kann durch Klick auf das rote **"X"** (oder via **"Hauptmenü → Programm → Tab schließen"**) geschlossen werden.

5.  **Fußzeile:** \
    In der Fußzeile können weitere Informationen zur Nutzung des Programms eingeblendet werden. Standardmäßig finden Sie hier zwei Symbole:
    
    -   **Informationen und Mitteilungen des Programms:** \
        Während der Nutzung des Programms können Mitteilungen eintreffen, die vom Programm unten rechts in der Fußzeile dargestellt werden - z.B.:
        
        {{< figure src="../../admin/client/update_notification.png" caption="Benachrichtigung über eine Aktualisierung" >}}
        
        Wenn eine Mitteilung vorliegt, färbt sich das Informations-Symbol blau ein. Durch Klick auf das rote **"X"** kann die Mitteilung ausgeblendet werden. Nach einer gewissen Wartezeit verschwinden die Mitteilungen automatisch.
    
    -   **Indikator für im Hintergrund durchgeführte Prozesse:** \
        Verschiedene Operationen führt das Programm während des Betriebs im Hintergrund durch - z.B. Export von Immobilien an Immobilienportale oder Abruf von E-Mails. Immer wenn ein solcher Prozess im Hintergrund ausgeführt wird, färbt sich der Kreis ein und beginnt sich zu drehen.
        
        {{< figure src="gui_progress_notification.png" caption="Export wird im Hintergrund durchgeführt" >}}
        
        Wenn auf den sich drehenden Kreis geklickt wird, werden weitere Informationen zu den aktuell durchgeführten Prozessen dargestellt. Durch Klick auf das rote **"X"** kann die Information wieder ausgeblendet werden.


### Verwendung von Tabellen {#usage_general_gui_tables}

An verschiedenen Stellen werden Tabellen innerhalb des Programmes dargestellt.

{{< figure src="table.png" caption="Tabellenansicht einrichten" >}}

Verschiedene Standardfunktionen sind in den Tabellen enthalten.

-   **Zeilen umsortieren:** \
    Durch einen Klick mit der linken Maustaste auf einen Spalten-Titel in der Tabelle, kann nach dieser Spalte auf- oder absteigend sortiert werden. Ein kleiner Pfeil neben dem Spalten-Titel zeigt die aktuelle Richtung der Sortierung an.

-   **Spalten umsortieren:** \
    Wenn mit der linken Maustaste auf einen Spalten-Titel in der Tabelle geklickt und die Taste gehalten wird, kann die Spalte innerhalb der Tabelle verschoben werden (Drag & Drop).

-   **Spalten ein- & ausblenden:** \
    Zum Ein- oder Ausblenden einer Spalte klicken Sie rechts von den Spalten-Titeln auf das Tabellen-Symbol um das Menü der Tabelle zu öffnen. Aktivieren oder deaktivieren Sie die entsprechende Spalte durch Klick auf den gewünschten Spalten-Titel.

-   **Einstellungen speichern:** \
    Um Änderungen dauerhaft zu speichern klicken Sie rechts von den Spalten-Titeln auf das Tabellen-Symbol und klicken auf **"Einstellungen zur Tabelle merken"**.

-   **Tabelle exportieren:** \
    Um die aktuelle Tabelle als CSV-, Excel oder PDF-Tabelle zu speichern klicken Sie rechts von den Spalten-Titeln auf das Tabellen-Symbol und wählen unter **"Tabelle exportieren"** das gewünschte Format, wählen im sich öffnenden Fenster den Speicherort und speichern die Datei.
    
{{< info >}}
Die beschriebenen Tabellen-Funktionen werden in den meisten - aber nicht in allen Tabellen - unterstützt.
{{< /info >}}


### Verwendung von Formularen {#usage_general_gui_forms}

Um Eingaben zu tätigen, werden an verschiedenen Stellen im Programm Formulare dargestellt.

{{< figure src="form.png" caption="Farbliche Markierung der Eingabefelder" >}}

{{< todo >}}
Bild einfügen
{{< /todo >}}

Die folgenden Standardfunktionen werden dabei verwendet.

-   **Pflichtfelder:** \
    Eingaben, die für eine weitere Verarbeitung zwingend notwendig sind, werden gelb hervorgehoben.

-   **Ungültige Eingaben:** \
    Ungültige Eingaben in einem Pflichtfeld werden rot hervorgehoben.

-   **Gültige Eingaben:** \
    Gültige Eingaben in einem Pflichtfeld werden grün hervorgehoben.
