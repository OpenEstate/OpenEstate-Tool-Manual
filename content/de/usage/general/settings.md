---

title: Einstellungen des Programms bearbeiten
linktitle: Einstellungen
description: Einstellungen von OpenEstate-ImmoTool bearbeiten…
weight: 40

menu:
  main:
    parent: usage-general
    identifier: usage-general-settings

---

## Einstellungen am Programm anpassen {#usage_general_settings}

Um Einstellungen am Programm / Add-Ons vorzunehmen, klicken Sie im Kopfmenü auf `Extras` → `Einstellungen`.

{{< figure src="menu_extras.jpg" caption="Einstellungen im Extras-Menü aufrufen" >}}

> **Hinweis**
>
> Bitte beachten Sie, dass im folgenden Fenster vorgenommene Einstellungen erst durch betätigen des Buttons `Speichern` übernommen werden.


### Allgemeine Programmeinstellungen {#usage_general_settings}

{{< figure src="settings_general.jpg" caption="Allgemeine Einstellungen" >}}

#### Browser {#usage_general_settings_webbrowser}

Der bevorzugte Web-Browser kann hier eingetragen werden. Im ImmoTool angezeigte URL's werden im hinterlegten Web-Browser geöffnet. Wenn kein Web-Browser eingetragen wurde, versucht das Programm den Standard-Browser des Betriebssystems zu starten.

Um den bevorzugten Webbrowser auszuwählen klicken Sie auf das Ordnersysmbol rechts neben der entsprechenden Zeile und navigieren im fogenden Dialogfenster zur Programmdatei. Markieren dieses und übernehmen die Einstellung mit dem Button `Programmdatei wählen`.

#### PDF-Reader {#usage_general_settings_pdfreader}

Der bevorzugte PDF-Reader kann hier eingetragen werden. Erzeugte PDF-Dokumente können aus dem ImmoTool heraus mit der hinterlegten Anwendung geöffnet werden.

Um den bevorzugten PDF-Reader auszuwählen klicken Sie auf das Ordnersysmbol rechts neben der entsprechenden Zeile und navigieren im fogenden Dialogfenster zur Programmdatei. Markieren dieses und übernehmen die Einstellung mit dem Button `Programmdatei wählen`.

#### Sonstiges

Hier können Sie einstellen, ob das zu letzt verwendete Projekt beim Start des Programmes geöffnet werden soll. Wenn Sie nur ein Projekt verwalten empfiehlt sich die Aktivierung.


#### Netzwerk-Einstellungen {#usage_general_settings_network}

{{< figure src="settings_general_network.jpg" caption="Einstellungen zum Netzwerk" >}}

Wenn Sie für HTTP- und / oder FTP-Verbindungen ins Internet einen Proxyserver verwenden, können Sie dies hier der Software mitteilen.

Sollte dies der Fall sein, entfernen Sie den Haken bei `Keinen HTTP/FTP-Proxy verwenden` und tragen Sie `Hostname / IP-Adresse` sowie die `Port-Nr` des Proxy-Servers ein.

> **Hinweis**
>
> Auf der Webseite der Entwickler können Sie ggf. weitere Informationen zur Konfiguration der aktiven FTP-Übertragung erhalten.


#### Datenbank-Einstellungen {#usage_general_settings_database}

{{< figure src="settings_general_database.jpg" caption="Einstellungen zur Datenbank" >}}

Hier können Sie festlegen, wo und wann die automatische Datensicherung vollzogen wird. Standardmäßig ist bereits ein Verzeichnis eingetragen, welches Sie bei Bedarf ändern können. Dies sollten Sie aber nur machen, wenn es zwingend notwwendig ist, weil Sie z.B. die Sicherung auf einem externen Datenträger speichern möchten.

Für den Zeitpunkt der Datensicherung werden Ihnen mehrere Optionen angeboten. Wählen Sie eine Einstellung, die Ihren Anforderungen entspricht. Die Standardeinstellung ist `an jedem Tag`.

Die Ziffer unter Limit gibt an, wieviele Datenbanksicherungen angelegt werden. Der voreingestellte Standardwert ist 5. Dies bedeutet z.B., dass - unabhängig von den Einstellungen unter `Automatische Sicherung` - fünf Sicherungen angelegt werden. Wenn die sechste Sicherung angelgt wird wird die erste gelöscht, so dass immer die fünf letzten Sicherungen verfügbar sind.
Wenn Sie diesen Wert erhöhen, beachten Sie, dass jede Sicherung die gesammte Datenbank enthält. Diese können je nach Datenbestand recht groß werden.


### Immobilien Add-On {#usage_general_settings_realestate_addon}

#### Allgemein

{{< figure src="settings_realestate.jpg" caption="Einstellungen zum Immobilien-Addon" >}}

Hier können Sie die maximale Bildgröße (Höhe und Breite in Pixel) einstellen, mit welcher die Immobilienbilder in das ImmoTool importiert werden. Voreigestellt ist eine Größ von 1000 Pixel x 1000 Pixel. Sollte ein kleineres Bild importiert werden bleibt dieses unagetastet und wird nicht auf die eingestellte Größe vergrößert.

Um die Datenbank nicht unnötig groß werden zu lassen, sollten Sie die Bilder der Immobilien auf die maximal benötigte Größe verkleinern. Zur Oientierung könnte hierbei die maximale Bildgröße auf den Portalen diehnen, auf welchen Sie inserieren.

Weitere Optionen

Hier können Sie angeben, ob beim Export der Immobilie nummerischen Attributen der Text 'ca.' vorangestellt wird.


#### Geodaten {#usage_general_settings_realestate_geodata}

Manche Portale benötigen eigene Geodaten um Immobilien regional präzise zuordnen zu können. Diese Geodaten können bei Bedarf in das ImmoTool importiert werden.

{{< figure src="settings_realestate_geo.jpg" caption="Geodaten verwalten" >}}

Für IS24 können Sie die benötigte Datei unter http://wiki.openestate.org/mediawiki/images/0/0d/Geo_is24.xml herunterladen. Speichern SIe diese Datei auf Ihrem Rechner und betätigen in den ImmoTool-Einsstellungen Immobilien » Geodaten den Button Importieren. Wählen Sie im folgenden Dialogfenster die entsprechende Datei auf Ihrem Rechenr und starten den Import durch den button 'Geo-Datei wählen'.


#### Sprachen {#usage_general_settings_realestate_languages}

{{< figure src="settings_realestate_languages.jpg" caption="Sprachen der Immobiliendaten verwalten" >}}

Hier können Sie die Sprachen wählen, in welchen Sie Freitexte zu den Immobilien ablegen möchten. Aktivieren Sie die gewünschten Sprachen durch anklicken der Checkboxen. Weitere Infonrmationen erhalten Sie im Kapitel 'Immobilie anlegen / verwalten'.

> **Hinweis**
>
> Hierbei handelt es sich nicht um die Übersetzungen des ImmoTools. Diese werden im Kapitel Add_Ons behandelt.


#### Suchvorlagen

Häufig verwendete Suchanfragen können als Suchvorlage abgelegt und bei Bedarf 

> **TODO**
>
> Inhalte einfügen Funktion unklar


### Kalender Add-On {#usage_general_settings_calendar_addon}

{{< figure src="settings_calendar.jpg" caption="Einstellungen zum Kalender-Addon" >}}

Hier können Sie Ihre Arbeitszeit eingrenzen. In der Tagesansicht des Kalenders wird diese Einstellung in der Anzeige berücksichtigt und Zeiten davor und danch nicht angezeigt.


### Programm- / Addons-Aktualiserung {#usage_general_settings_updates}

Deaktivieren Sie bei Bedarf die automatische Aktualisierung des Programms und der Add-Ons bei Programmstart. Sind diese Otionen aktiviert wird beim Start des Programms in einem Hintergrundprozess nach Aktualisierungen gesucht. Werden Aktualisierungen gefunden, so werden Sie darauf hingewiesen und können selbst entscheiden, ob diese installiert werden sollen.

> **Hinweis**
>
> Standardmäßig ist das Programm so eingestellt, dass beim Start vorhandene Aktualisierungen gesucht und zum herunterladen angeboten werden!
>
> Diese Funktion sucht ausschließlich nach aktuelleren Versionen des ImmoTools und der bereits installierten Add-Ons. Weitere zur Installation verfügbare Add-Ons werden hier nicht angezeigt. Diese finden Sie ggf. im [Anwenderbereich](http://dev.openestate.org) oder bei einem externen Anbieter.

> **TODO**
>
> Funktion nicht gegeben
