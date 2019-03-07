---

title: Einstellungen des Programms bearbeiten
linktitle: Einstellungen
description: Einstellungen von OpenEstate-ImmoTool bearbeiten…
weight: 50

menu:
  main:
    parent: usage-general
    identifier: usage-general-settings

---

## Einstellungen am Programm anpassen {#usage_general_settings}

Um Einstellungen am Programm / Add-Ons vorzunehmen, klicken Sie im Hauptmenü auf **"Extras → Einstellungen"**.

{{< figure src="menu_extras.png" caption="Einstellungen im Extras-Menü aufrufen" >}}

{{< info >}}
Bitte beachten Sie, dass im folgenden Fenster vorgenommene Einstellungen erst durch betätigen des Buttons **"Speichern"** übernommen werden.
{{< /info >}}


### Allgemeine Einstellungen {#usage_general_settings_general}

{{< figure src="settings_general.png" caption="Allgemeine Einstellungen" >}}


#### Browser {#usage_general_settings_webbrowser}

Der bevorzugte Web-Browser kann hier eingetragen werden. Im ImmoTool angezeigte URL's werden im hinterlegten Web-Browser geöffnet. Wenn kein Web-Browser eingetragen wurde, versucht das Programm den Standard-Browser des Betriebssystems zu starten.

Um den bevorzugten Webbrowser auszuwählen klicken Sie auf das Ordner-Symbol rechts neben der entsprechenden Zeile und navigieren im folgenden Dialogfenster zur Programmdatei. Markieren dieses und übernehmen die Einstellung mit dem Button **"Programmdatei wählen"**.


#### PDF-Reader {#usage_general_settings_pdfreader}

Der bevorzugte PDF-Reader kann hier eingetragen werden. Erzeugte PDF-Dokumente können aus dem ImmoTool heraus mit der hinterlegten Anwendung geöffnet werden.

Um den bevorzugten PDF-Reader auszuwählen klicken Sie auf das Ordner-Symbol rechts neben der entsprechenden Zeile und navigieren im folgenden Dialogfenster zur Programmdatei. Markieren dieses und übernehmen die Einstellung mit dem Button **"Programmdatei wählen"**.


#### Darstellung {#usage_general_settings_rendering}

Hier können Sie die Schriftgröße im Programm einstellen. Vorgenommene Änderungen werden erst nach einem Neustart des Programms wirksam.


#### Sonstiges {#usage_general_settings_other}

Hier können Sie einstellen, ob das zu letzt verwendete Projekt beim Start des Programmes geöffnet werden soll. Wenn Sie nur ein Projekt verwalten empfiehlt sich die Aktivierung.


#### Netzwerk-Einstellungen {#usage_general_settings_network}

{{< figure src="settings_general_network.png" caption="Einstellungen zum Netzwerk" >}}

Wenn Sie für HTTP- und / oder FTP-Verbindungen ins Internet einen Proxy-Server verwenden, können Sie dies hier der Software mitteilen.

Sollte dies der Fall sein, entfernen Sie den Haken bei **"Keinen HTTP/FTP-Proxy verwenden"** und tragen Sie **"Hostname / IP-Adresse"** sowie die **"Port-Nr"** des Proxy-Servers ein.

{{< info >}}
Auf der Webseite der Entwickler können Sie ggf. weitere Informationen zur Konfiguration der aktiven FTP-Übertragung erhalten.
{{< /info >}}


#### Datenbank-Einstellungen {#usage_general_settings_database}

{{< figure src="settings_general_database.png" caption="Einstellungen zur Datenbank" >}}

Hier können Sie festlegen, wo und wann die automatische Datensicherung vollzogen wird. Standardmäßig ist bereits ein Verzeichnis eingetragen, welches Sie bei Bedarf ändern können. Dies sollten Sie aber nur machen, wenn es zwingend notwendig ist, weil Sie z.B. die Sicherung auf einem externen Datenträger speichern möchten.

Für den Zeitpunkt der Datensicherung werden Ihnen unter **"Automatische Sicherung"** mehrere Optionen angeboten. Wählen Sie eine Einstellung, die Ihren Anforderungen entspricht. Die Standardeinstellung ist **"an jedem Tag"**.

Die Ziffer unter Limit gibt an, wie viele Sicherungen der Datenbank angelegt werden. Der voreingestellte Standardwert ist 5. Dies bedeutet z.B., dass - unabhängig von den Einstellungen unter **"Automatische Sicherung"** - fünf Sicherungen angelegt werden. Wenn die sechste Sicherung angelegt wird wird die erste gelöscht, so dass immer die fünf letzten Sicherungen verfügbar sind.
Wenn Sie diesen Wert erhöhen, beachten Sie, dass jede Sicherung die gesamte Datenbank enthält. Diese können je nach Datenbestand recht groß werden.

{{< info >}}
Unabhängig von diesen Einstellungen können Sie im Hauptmenü unter **"Extras → Datenbank → Sicherung"** jederzeit eine Manuelle Datensicherung nach Bedarf durchführen.
{{< /info >}}


### Kalender Add-On {#usage_general_settings_calendar_addon}

{{< figure src="settings_calendar.png" caption="Einstellungen zum Kalender Add-On" >}}

Hier können Sie Ihre Arbeitszeit eingrenzen. In der Tagesansicht des Kalenders wird diese Einstellung in der Anzeige berücksichtigt und Zeiten davor und danach nicht angezeigt.

{{< todo >}}
Aktivitäten und Geburtstage erklären.
{{< /todo >}}


### Immobilien Add-On {#usage_general_settings_realestate_addon}


#### Allgemein {#usage_general_settings_realestate_addon_general}

{{< figure src="settings_realestate.png" caption="Einstellungen zum Immobilien Add-On" >}}

Hier können Sie die maximale Größe (Höhe und Breite in Pixel) einstellen, mit welcher die Bilder von Immobilien in das ImmoTool importiert werden. Voreingestellt ist eine Größe von 1000 x 1000 Pixeln. Sollte ein kleineres Bild importiert werden, bleibt dieses unangetastet und wird nicht auf die eingestellte Größe vergrößert.

Um die Datenbank nicht unnötig groß werden zu lassen, sollten Sie die Bilder der Immobilien auf die maximal benötigte Größe verkleinern. Zur Orientierung könnte hierbei die maximale Bild-Größe auf den Portalen dienen, auf welchen Sie inserieren.


#### Weitere Optionen {#usage_general_settings_realestate_addon_other}

Hier können Sie angeben, ob beim Export der Immobilie nummerischen Attributen der Text 'ca.' vorangestellt wird.


#### Geodaten {#usage_general_settings_realestate_geodata}

Manche Portale benötigen eigene Geodaten um Immobilien regional präzise zuordnen zu können. Diese Geodaten können bei Bedarf in das ImmoTool importiert werden.

{{< figure src="settings_realestate_geo.png" caption="Geodaten verwalten" >}}

Für IS24 können Sie die benötigte Datei unter (Link wird nachgeführt) herunterladen. Speichern Sie diese Datei auf Ihrem Rechner und betätigen in den ImmoTool-Einstellungen Immobilien » Geodaten den Button Importieren. Wählen Sie im folgenden Dialogfenster die entsprechende Datei auf Ihrem Rechner und starten den Import durch den button 'Geo-Datei wählen'.

{{< todo >}}
Link zu Download der Geo-Daten von IS24 einfügen.
{{< /todo >}}


#### Sprachen {#usage_general_settings_realestate_languages}

{{< figure src="settings_realestate_languages.png" caption="Sprachen der Immobiliendaten verwalten" >}}

Hier können Sie die Sprachen wählen, in welchen Texte zu den Immobilien erfasst werden sollen. Aktivieren Sie die gewünschten Sprachen durch Anklicken der Checkboxen.

{{< info >}}
Hierbei handelt es sich nicht um die Übersetzungen des ImmoTools. Diese werden im Kapitel Add_Ons behandelt.
{{< /info >}}


#### Suchvorlagen {#usage_general_settings_realestate_addon_search}

Häufig verwendete Suchanfragen können als Suchvorlage abgelegt und bei Bedarf 

{{< figure src="settings_realestate_search.png" caption="Sprachen der Immobiliendaten verwalten" >}}


{{< todo >}}
Funktion Suchvorlagen erklären.
{{< /todo >}}


