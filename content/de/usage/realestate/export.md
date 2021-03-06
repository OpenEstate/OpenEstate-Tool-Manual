---

title: Immobilien exportieren
linktitle: Exporte
description: Hinweise zum Export von Immobilien in OpenEstate-ImmoTool…
weight: 50

menu:
  main:
    parent: usage-realestate
    identifier: usage-realestate-export

---

## Immobilien exportieren {#usage_realestate_export}

Die im ImmoTool erfassten Immobiliendaten können als Export zusammengestellt und an externe Partner versendet werden (z.B. Immmobilienportale). Für jeden zu beliefernden Empfänger muss eine **Export-Schnittstelle** im Programm eingerichtet werden.

{{< info >}}
Zu den uns bekannten funktionierenden Immobilienportalen finden Sie [Hilfestellungen und Anleitungen auf der OpenEstate-Webseite](https://openestate.org/immotool/portals). Berücksichtigt sind hier Portale, welche von uns getestet wurden oder zu welchen ImmoTool-Benutzer erfolgreich senden konnten.
{{< /info >}}


### Übersicht der Export-Schnittstellen {#usage_realestate_export_summary}

Zur Verwaltung der Export-Schnittstelle gelangen Sie auf zweierlei Wegen:

1.  Klicken Sie im Hauptmenü auf **"Immobilien → Schnittstellen anzeigen"**.

    {{< figure src="menu.png" caption="Schnittstellen über das Hauptmenü auflisten" >}}

2.  Klicken Sie in der Sidebar auf den Eintrag **"Export-Schnittstellen"**. Alternativ können Sie auch den Eintrag **"Export-Schnittstellen"** markieren und mit der rechten Maustaste **"Schnittstellen anzeigen"** betätigen.

    {{< figure src="sidebar.png" caption="Schnittstellen über die Sidebar auflisten" >}}


Es öffnet sich daraufhin ein Fenster mit den von Ihnen angelegten Export-Schnittstellen.

{{< figure src="export_table.png" caption="Übersicht der Export-Schnittstellen" >}}


### Exportvorgang starten {#usage_realestate_export_start}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary) und [aktivieren](#usage_realestate_export_enable) bzw. [deaktivieren](#usage_realestate_export_enable) Sie die Schnittstellen, welche für den Export verwendet / nicht verwendet werden sollen.  Bei den aktivierten Schnittstellen ist die Schrift schwarz und bei den deaktivierten ist sie grau.

Klicken Sie, um die Exportvorbereitung zu starten, auf **"Export starten"**. Es öffnet sich folgendes Fenster.

{{< figure src="export_summary.png" caption="Vorbereitung des Exportvorgangs" >}}

Hier erhalten Sie zur den jeweiligen Schnittstellen verschiedene Informationen. Sie können die Einstellung der Schnittstelle zum Modus (Teil- oder Vollabgleich) temporär für diesen Export ändern. Wenn sie auf die blauen Pfeile klicken wird Ihnen aufgezeigt, welche Aktionen mit welcher Immobilie ausgeführt werden. Wenn Sie auf ein rotes Minus klicke, wird die entsprechende Schnittstelle temporär für diesen Export deaktiviert. Sollten Sie eine Schnittstelle versehentlich deaktiviert haben, können Sie diese wieder hinzufügen, indem Sie auf den Button **"Hinzufügen"** klicken und die gewünschten Schnittstellen wieder hinzufügen.


### Export-Schnittstelle erstellen {#usage_realestate_export_add}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary) und klicken oben rechts auf den Button **"Neu"**. Es öffnet sich danach ein [Formular zur Erfassung einer neuen Export-Schnittstelle](#usage_realestate_export_form).


### Export-Schnittstelle bearbeiten {#usage_realestate_export_edit}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary). Per Doppelklick auf eine der zuvor erfassten Export-Schnittstellen öffnet sich ein [Formular zur Bearbeitung der gewählten Export-Schnittstelle](#usage_realestate_export_form).


### Export-Schnittstelle löschen {#usage_realestate_export_remove}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary).

Mit einem Rechtsklick auf die betreffende Export-Schnittstelle in der Tabelle öffnet sich ein Menü, in dem Sie die Aktion **"Schnittstelle entfernen"** auswählen können um die Export-Schnittstelle zu löschen.

Alternativ kann die betreffende Export-Schnittstelle in der Tabelle mit der Maus markieren. Bei Klick auf den Button **"Aktionen"** wird ein Menü dargestellt, in dem Sie die Aktion **"Schnittstelle entfernen"** auswählen können um die Export-Schnittstelle zu löschen.

Darüber hinaus können Sie die Schnittstelle auch in der Sidebar mit der linken Maustaste markieren und im folgenden Menü  die Aktion **"Schnittstelle entfernen"** auswählen.


### Export-Schnittstelle (de)aktivieren {#usage_realestate_export_enable}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary).


#### Export-Schnittstelle permanent (de)aktivieren {#usage_realestate_export_enable_permanent}

Öffnen Sie die zu aktivierende Schnittstelle zur Bearbeitung und (de)aktivieren Sie die Option **"Schnittstelle aktivieren"**. Nachdem die Änderung durch Klick auf den Button **"Speichern"** übernommen wurde, ist die Export-Schnittstelle permanent im Projekt (de)aktiviert.

Alternativ können klicken Sie mit der rechten Maustaste auf eine Schnittstelle und wählen im folgenden Menü **"Schnittstelle deaktivieren"**.


#### Export-Schnittstelle für einen Exportvorgang (de)aktivieren  {#usage_realestate_export_enable_temporarily}

Nachdem Sie **"Export starten"** geklickt haben, können Sie Schnittstellen für den nächsten Export ausschließen, indem Sie in der Exportvorbereitung diese mit dem **"roten Minus"** entfernen.


### Export-Schnittstelle exportieren {#usage_realestate_export_export}

Sie können angelegte Schnittstellen als gesonderte Sicherung oder zum Transfer in ein anderes ImmoTool auf Ihrem Computer ablegen. Markieren Sie hierfür eine oder mehrere Schnittstellen und klicken auf die Immobilie(n) mit der rechten Maustaste und wählen im erscheinenden Menü **"Schnittstelle auf Festplatte exportieren"**. Im folgenden Fenster wählen Sie den Speicherort und klicken auf **"Speichern"**.


### Export-Schnittstelle importieren {#usage_realestate_export_import}

Um die Einrichtung der Schnittstelle zu erleichtern unterstützt das Programm den Import von Schnittstellen. Sie können von teilnehmenden Partnern eine XML-Datei beziehen, die Sie direkt ins Programm importieren können. Dadurch können eventuelle Fehleingaben bei der Einrichtung einer Schnittstelle vermieden werden.

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary) und klicken mit der rechten Maustaste in der Sidebar auf **"Exporte sonstiges Schnittstelle importieren"**. Es öffnet sich ein Fenster, in dem Sie eine oder mehrere die Schnittstellen-Datei auswählen und auf den Button **"Öffnen"** klicken. Die ausgewählten Schnittstelle-Datein werden in das ImmoTool eingelesen.


### Formular für Export-Schnittstellen {#usage_realestate_export_form}

#### Allgemeine Einstellungen {#usage_realestate_export_form_general}

Die allgemeinen Einstellungen können im oberen Bereich des Formulars eingetragen werden:

{{< figure src="export_form_general.png" caption="Allgemeine Einstellungen der Export-Schnittstelle" >}}

-   **Titel:** \
    Tragen Sie hier einen Namen zu dieser Schnittstelle ein (z.B. "ImmobilienScout24").

-   **Format:** \
    Wählen Sie das vom jeweiligen Empfänger geforderte Format aus. Das gebräuchlichste ist **OpenImmo-XML**.

-   **Transport:** \
    Wählen Sie die vom jeweiligen Empfänger geforderte Transport-Art aus. Die gebräuchlichste ist extern auf einen FTP-Server.

-   **Modes:** \
    Wählen Sie hier zwischen Teil- und Vollabgleich. Es wird empfohlen Exporte im Teilabgleich zu senden.

-   **Limitierung:** \
    Sie können hier einstellen, wie viele Inserate maximal zum Empfänger gesendet werden. Sollten Sie eine Limitierung einstellen wollen, deaktivieren Sie die Option **"Keine Limitierung verwenden"** und tragen Sie die gewünschte Anzahl ein.

-   **Schnittstelle aktivieren** \
    Standardmäßig ist diese Option auf **"aktiv"** gesetzt. Wenn Sie diese Schnittstelle noch nicht aktivieren möchten, so entfernen Sie den Haken. Sie können diese Schnittstelle ggf. auch in der Übersicht der Schnittstellen temporär für einen einzelnen Exportvorgang aktivieren.

-   **Anbieter-Nr:** \
    Tragen Sie hier die Anbieter- / Kundennummer des jeweiligen Portals ein.

-   **OpenImmo-Nr:** \
    Diese Angabe wird meist nicht benötigt. Wenn doch, tragen Sie hier ebenfalls die Anbieter- / Kundennummer des jeweiligen Portals ein.

-   **Technik Mail:** \
    Tragen Sie hier die E-Mailadresse der Person ein, welche ggf. die Import-Meldungen erhält.

-   **Modus:** \
    Wählen Sie zwischen Voll- und Teilabgleich.

-   **Vollabgleich:** \
        Der gesamte Immobilienbestand, der zur Schnittstelle zugewiesen wurde, wird bei jedem Exportvorgang zum Empfänger gesendet.

-   **Teilabgleich:** \
        Es werden nur Immobilien exportiert, die zur Schnittstelle zugewiesen wurden und die seit dem letzten Exportvorgang über diese Schnittstelle geändert wurden.

-   **Zeilenumbruch:** \
    Wählen Sie die Methode des Zeilenumbruchs. Im Zweifelsfall belassen Sie die Standardeinstellung und überprüfen die Darstellung in jeweiligen Portal.

-   **Anhänge:** \
    Wenn nicht anders benannt, belassen Sie die Standardeinstellung.

-   **Markierung:** \
    Wenn nicht anders benannt, belassen Sie die Standardeinstellung. Sollten keine Bilder beim Empfänger dargestellt werden, so ändern Sie die Einstellung und führen Sie einen erneuten Exportvorgang durch.

-   **Sonstiges:** \
    Wenn nicht anders benannt, belassen Sie die Standardeinstellung.


{{< warning >}}
Die Option zur Limitierung schützt Sie nicht zwangsläufig vor der Überschreitung Ihres Kontingents bei dem Empfänger. Prüfen Sie bitte dennoch in regelmäßigen Abständen beim Empfänger, ob das Limit korrekt eingehalten wird.
{{< /warning >}}


#### Transport via FTP {#usage_realestate_export_form_ftp}

Wenn im Feld **"Transport"** die Übertragungs-Art **"FTP"** gewählt wurde, wird das folgende Formular im Tab **"Transport"** dargestellt:

{{< figure src="export_form_ftp.png" caption="FTP-Einstellungen der Export-Schnittstelle" >}}

-   **Hostname:** \
    Tragen Sie hier die Adresse des FTP-Servers ein. Manchmal wird auch der Begriff "Host" oder "Serveradresse" verwendet.

-   **Port:** \
    Standardmäßig ist Port **`21`** zu verwenden. Dies ist auch voreingestellt, und sollte nur auf ausdrückliche Aufforderung geändert werden.

-   **User:** \
    Tragen Sie hier Ihren FTP-Benutzernamen ein. Manchmal wird auch der Begriff "Loginnname" oder "Benutzer" verwendet.

-   **Passwort:** \
    Tragen Sie hier Ihr FTP-Passwort ein.

-   **Serverpfad:** \
    Standardmäßig ist **`/`** voreingestellt, was in den meisten Fällen auch nicht geändert werden muss.

-   **Passive FTP-Verbindung:** \
    Abhängig von der Konfiguration Ihres Netzwerkes und den Vorgaben des Empfängers kann es notwendig sein, diese Option zu deaktivieren. Sollte es beim Export zu Problemen kommen, deaktivieren Sie diese Option und versuchen es erneut.

-   **Testen:** \
    Wenn Sie die FTP-Zugangsdaten eingetragen habe, können Sie mit diesem Button die Verbindung testen. Sollte der Test negativ verlaufen, überprüfen Sie bitte Ihre Eingaben bevor Sie den Support in Anspruch nehmen.


#### Transport via HTTP {#usage_realestate_export_form_http}

Wenn im Feld **"Transport"** die Übertragungs-Art **"HTTP"** gewählt wurde, wird das folgende Formular im Tab **"Transport"** dargestellt:

{{< figure src="export_form_http.png" caption="HTTP-Einstellungen der Export-Schnittstelle" >}}

-   **URL:** \
    Tragen Sie hier die HTTP-Adresse des Empfängers ein, zu der die exportierten Immobilien gesendet werden sollen.

-   **User:** \
    Tragen Sie hier Ihren FTP-Benutzernamen ein. Manchmal wird auch der Begriff "Loginnname" oder "Benutzer" verwendet.

-   **Passwort:** \
    Tragen Sie hier Ihr HTTP-Passwort ein.

-   **Übertragung:** \
    Wählen Sie die [Art der HTTP-Anfrage](https://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP-Request-Methoden)) in diesem Feld aus.

    -   **via PUT-Anfrage:** \
        In diesem Falle werden die exportierten Dateien durch eine **"HTTP PUT"**-Anfrage zum Empfänger gesendet.

    -   **via POST-Anfrage:** \
        In diesem Falle werden die exportierten Dateien durch eine **"HTTP POST"**-Anfrage zum Empfänger gesendet.

    -   **via POST-Anfrage, als Formular (multipart/form-data):** \
        In diesem Falle werden die exportierten Dateien durch eine **"HTTP POST"**-Anfrage zum Empfänger gesendet. Dieser Mechanismus ist identisch zu einem Datei-Upload aus einem Web-Formular.

-   **Form-Variable:** \
    Wenn bei der **"Übertragung"** die Option **"via POST-Anfrage, als Formular (multipart/form-data)"** gewählt wurde, kann in diesem Eingabefeld der Name der Formular-Variablen eingetragen werden, unter dem die übermittelte Datei zum Empfänger gesendet wird. Beim Upload aus einem Web-Formular entspricht dies dem Namen des Datei-Eingabefelds.


#### Transport auf die Festplatte {#usage_realestate_export_form_local}

Wenn im Feld **"Transport"** die Übertragungs-Art **"lokal auf die Festplatte"** gewählt wurde, wird das folgende Formular im Tab **"Transport"** dargestellt:

{{< figure src="export_form_local.png" caption="Lokale Einstellungen der Export-Schnittstelle" >}}

-   **Zielordner:** \
    Wählen Sie hier das lokale Verzeichnis auf Ihrer Festplatte aus, in welches die exportierten Immobiliendaten abgelegt werden soll.


#### Änderungen speichern {#usage_realestate_export_form_submit}

Um die Änderungen im Formular dauerhaft zu speichern, klicken Sie oben rechts auf den Button **"Speichern"**.

{{< info >}}
Das Speichern ist zu jedem Zeitpunkt der Bearbeitung möglich. Sollten relevante Eingaben fehlen, so weist das Programm darauf hin.
{{< /info >}}

{{< warning >}}
Jede Änderung im Formular muss abschließend durch Klick auf **"Speichern"** dauerhaft gespeichert werden.
{{< /warning >}}
