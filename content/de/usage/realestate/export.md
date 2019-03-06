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
Zu den uns bekannten funktionierenden Immobilienportalen finden Sie [Hilfestellungen und Anleitungen im OpenEstate-Wiki](http://wiki.openestate.org/Kategorie:ImmoTool_Portalexport). Berücksichtigt sind hier Portale, welche von uns getestet wurden oder zu welchen ImmoTool-Benutzer erfolgreich senden konnten.
{{< /info >}}


### Übersicht der Export-Schnittstellen {#usage_realestate_export_summary}

Zur Verwaltung der Export-Schnittstelle gelangen Sie auf zweierlei Wegen:

1.  Klicken Sie im Hauptmenü auf `Immobilien` → `Schnittstellen anzeigen`.

    {{< figure src="menu.png" caption="Schnittstellen über das Hauptmenü auflisten" >}}

2.  Klicken Sie in der Sidebar auf den Eintrag `Export-Schnittstellen`. Alternativ können Sie auch den Eintrag `Export-Schnittstellen` markieren und mit der rechten Maustaste `Schnittstellen anzeigen` betätigen.

    {{< figure src="sidebar.png" caption="Schnittstellen über die Sidebar auflisten" >}}


Es öffnet sich daraufhin ein Fenster mit den registrierten Export-Schnittstellen.

{{< figure src="export_table.jpg" caption="Übersicht der Export-Schnittstellen" >}}


### Exportvorgang starten {#usage_realestate_export_start}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary) und [aktivieren](#usage_realestate_export_enable) bzw. [deaktivieren](#usage_realestate_export_enable) Sie die Schnittstellen, welche für den Export verwendet / nicht verwendet werden sollen. Diese Einstellung können Sie aber auch nach der Zusammenstellung des Exports entscheiden und temporär (nur für den folgenden Export) ändern.Bei den aktivierten Schnittstellen ist die Schrift schwarz und bei den deaktivierten ist sie grau.

Klicken Sie auf `Export starten` um den Exportvorgang anzustoßen.

Es öffnet sich ein weiteres Fenster, in welchem die Immobilien für den Export zusammengestellt werden.

{{< figure src="export_summary.jpg" caption="Vorbereitung des Exportvorgangs" >}}

Nach Bedarf können einzelne Immobilien vom Export ausgeschlossen werden. Klicken Sie abschließend auf `Export starten` um den Exportvorgang mit den gewählten Immobilien / Schnittstellen zu starten.


### Export-Schnittstelle erstellen {#usage_realestate_export_add}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary) und klicken Sie oben rechts auf den Button `Neu`. Es öffnet sich danach ein [Formular zur Erfassung einer neuen Export-Schnittstelle](#usage_realestate_export_form).


### Export-Schnittstelle bearbeiten {#usage_realestate_export_edit}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary). Per Doppelklick auf eine der zuvor erfassten Export-Schnittstellen öffnet sich ein [Formular zur Bearbeitung der gewählten Export-Schnittstelle](#usage_realestate_export_form).


### Export-Schnittstelle löschen {#usage_realestate_export_remove}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary).

Bei Rechtsklick auf die betreffende Export-Schnittstelle in der Tabelle öffnet sich ein Menü, in dem Sie die Aktion `Entfernen` auswählen können um die Export-Schnittstelle zu entfernen.

Alternativ kann die betreffende Export-Schnittstelle in der Tabelle per Linksklick markiert werden. Bei Klick auf den Button `Aktionen` wird ein Menü dargestellt, in dem Sie die Aktion `Entfernen` auswählen können um die Export-Schnittstelle zu entfernen.

{{< warning >}}
Eine Löschung kann ohne vorherige Datensicherung nicht wieder rückgängig gemacht werden!
{{< /warning >}}


### Export-Schnittstelle (de)aktivieren {#usage_realestate_export_enable}

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary).


#### Export-Schnittstelle permanent (de)aktivieren {#usage_realestate_export_enable_permanent}

Öffnen Sie die zu aktivierende Schnittstelle zur Bearbeitung und (de)aktivieren Sie die Option `Die Export-Schnittstelle aktivieren`.

Nachdem die Änderung durch Klick auf den Button `Speichern` übernommen wurde, ist die Export-Schnittstelle permanent im Projekt (de)aktiviert.


#### Export-Schnittstelle für einen Exportvorgang (de)aktivieren  {#usage_realestate_export_enable_temporarily}

Links in der Übersicht der Schnittstellen können Sie eine oder mehrere Schnittstelle(n) für einen Exportvorgang (de)aktivieren. Diese Einstellung wird nicht dauerhaft gespeichert, sondern gilt nur solange die Übersicht der Schnittstellen geöffnet ist.


### Export-Schnittstelle importieren {#usage_realestate_export_import}

Um die Einrichtung der Schnittstelle zu erleichtern unterstützt das Programm den Import von Schnittstellen. Sie können von teilnehmenden Partnern eine XML-Datei beziehen, die Sie direkt ins Programm importieren können. Dadurch können eventuelle Fehleingaben bei der Einrichtung einer Schnittstelle vermieden werden.

Öffnen Sie die [Übersicht der Exporte](#usage_realestate_export_summary) und klicken Sie oben rechts auf den Button `Import`. Es öffnet sich ein Fenster, in dem die zuvor heruntergeladene Schnittstellen-Datei ausgewählt werden kann.

Nach Auswahl der Schnittstellen-Datei wird automatisch eine Export-Schnittstelle im Programm mit den jeweiligen Vorgaben des Empfängers erzeugt.


### Formular für Export-Schnittstellen {#usage_realestate_export_form}

#### Allgemeine Einstellungen {#usage_realestate_export_form_general}

Die allgemeinen Einstellungen können im oberen Bereich des Formulars eingetragen werden:

{{< figure src="export_form_general.jpg" caption="Allgemeine Einstellungen der Export-Schnittstelle" >}}

-   **Bezeichnung**

    Tragen Sie hier einen Namen zu dieser Schnittstelle ein (z.B. "ImmobilienScout24").

-   **Transport**

    Wählen Sie die vom jeweiligen Empfänger geforderte Transport-Art aus. Die gebräuchlichste ist extern auf einen FTP-Server.

-   **Format**

    Wählen Sie das vom jeweiligen Empfänger geforderte Format aus. Das gebräuchlichste ist `OpenImmo-XML`.

-   **Limitierung**

    Sie können hier einstellen, wie viele Inserate maximal zum Empfänger gesendet werden. Sollten Sie eine Limitierung einstellen wollen, entfernen Sie den Haken bei `Keine Limitierung verwenden` und tragen Sie die gewünschte Anzahl ein.

-   **Schnittstelle aktivieren**

    Standardmäßig ist diese Option auf `aktiv` gesetzt. Wenn Sie diese Schnittstelle noch nicht aktivieren möchten, so entfernen Sie den Haken. Sie können diese Schnittstelle ggf. auch in der Übersicht der Schnittstellen temporär für einen einzelnen Exportvorgang aktivieren.

{{< warning >}}
Die Option zur Limitierung schützt Sie nicht zwangsläufig vor der Überschreitung Ihres Kontingents bei dem Empfänger. Prüfen Sie bitte dennoch in regelmäßigen Abständen beim Empfänger, ob das Limit korrekt eingehalten wird.
{{< /warning >}}


#### Transport via FTP {#usage_realestate_export_form_ftp}

Wenn im Feld `Transport` die Übertragungs-Art `FTP` gewählt wurde, wird das folgende Formular im Tab `Transport` dargestellt:

{{< figure src="export_form_ftp.jpg" caption="FTP-Einstellungen der Export-Schnittstelle" >}}

-   **Adresse**

    Tragen Sie hier die Adresse des FTP-Servers ein. (z.B.: “import.openindex.de”) Manchmal wird auch der Begriff “Host” statt “Adresse” verwendet.

-   **Port**

    Standardmäßig ist Port 21 zu verwenden. Dies ist auch voreingestellt, und sollte nur auf ausdrückliche Aufforderung geändert werden.

-   **Login**

    Tragen Sie hier Ihren FTP-Benutzernamen ein.

-   **Passwort**

    Tragen Sie hier Ihr FTP-Passwort ein.

-   **Serverpfad**

    Standardmäßig ist `/` voreingestellt, was in den meisten Fällen auch nicht geändert werden muss.

-   **Passive FTP-Verbindung**

    Abhängig von der Konfiguration Ihres Netzwerkes und den Vorgaben des Empfängers kann es notwendig sein, diese Option zu deaktivieren. Sollte es beim Export zu Problemen kommen, deaktivieren Sie diese Option und versuchen es erneut.

-   **Testen**

    Wenn Sie die FTP-Zugangsdaten eingetragen habe, können Sie mit diesem Button die Verbindung testen. Sollte der Test negativ verlaufen, überprüfen Sie bitte Ihre Eingaben bevor Sie den Support in Anspruch nehmen.


#### Transport via HTTP {#usage_realestate_export_form_http}

Wenn im Feld `Transport` die Übertragungs-Art `HTTP` gewählt wurde, wird das folgende Formular im Tab `Transport` dargestellt:

{{< figure src="export_form_http.jpg" caption="HTTP-Einstellungen der Export-Schnittstelle" >}}

-   **HTTP-Adresse**

    Tragen Sie hier die URL des Empfängers ein, zu der die exportierten Immobilien gesendet werden sollen.

-   **Login**

    Tragen Sie hier Ihren Benutzernamen ein.

-   **Passwort**

    Tragen Sie hier Ihr Passwort ein.

-   **Übertragung**

    Wählen Sie die Art der HTTP-Übertragung in diesem Feld aus.

    -   **via PUT-Anfrage**
    
        In diesem Falle werden die exportierten Dateien durch eine `HTTP PUT`-Anfrage zum Empfänger gesendet (siehe [HTTP-Request-Methoden](http://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP-Request-Methoden)).

    -   **via POST-Anfrage**
    
        In diesem Falle werden die exportierten Dateien durch eine `HTTP POST`-Anfrage zum Empfänger gesendet (siehe [HTTP-Request-Methoden](http://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP-Request-Methoden)).

    -   **via POST-Anfrage, als Formular (multipart/form-data)**
    
        In diesem Falle werden die exportierten Dateien durch eine `HTTP POST`-Anfrage zum Empfänger gesendet (siehe [HTTP-Request-Methoden](http://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol#HTTP-Request-Methoden)). Dieser Mechanismus ist identisch zu einem Datei-Upload aus einem Web-Formular.

-   **Form-Variable**
    Wenn bei der `Übertragung` die Option `via POST-Anfrage, als Formular (multipart/form-data)` gewählt wurde, kann in diesem Eingabefeld der Name der Formular-Variablen eingetragen werden, unter dem die übermittelte Datei zum Empfänger gesendet wird. Beim Upload aus einem Web-Formular entspricht dies dem Namen des Datei-Eingabefelds.


#### Transport auf die Festplatte {#usage_realestate_export_form_local}

Wenn im Feld `Transport` die Übertragungs-Art `lokal auf die Festplatte` gewählt wurde, wird das folgende Formular im Tab`Transport` dargestellt:

{{< todo >}}
Bild einfügen
{{< /todo >}}

-   **Zielverzeichnis**
    Wählen Sie hier das lokale Verzeichnis auf Ihrer Festplatte aus, in welches die exportierten Immobiliendaten abgelegt werden soll.


#### Einstellungen zum OpenImmo-XML-Format {#usage_realestate_export_form_openimmo}

Wenn im Feld `Format` die Übertragungs-Art `OpenImmo-XML` gewählt wurde, wird das folgende Formular im Tab `Format` dargestellt:

{{< figure src="export_form_openimmo.jpg" caption="Einstellungen in Export-Schnittstelle zum OpenImmo-Format" >}}

-   **Anbieter-Nr**

    Tragen Sie hier die Anbieter- / Kundennummer des jeweiligen Portals ein.

-   **OpenImmo-Nr**

    Diese Angabe wird meist nicht benötigt. Wenn doch, tragen Sie hier ebenfalls die Anbieter- / Kundennummer des jeweiligen Portals ein.

-   **Technik Mail**

    Tragen Sie hier die E-Mailadresse der Person ein, welche ggf. die Import-Meldungen erhält.

-   **Modus**

    Wählen Sie zwischen Voll- und Teilabgleich.

    -   **Vollabgleich**
    
        Der gesamte Immobilienbestand, der zur Schnittstelle zugewiesen wurde, wird bei jedem Exportvorgang zum Empfänger gesendet.

    -   **Teilabgleich**
    
        Es werden nur Immobilien exportiert, die zur Schnittstelle zugewiesen wurden und die seit dem letzten Exportvorgang über diese Schnittstelle geändert wurden.

-   **Zeilenumbruch**

    Wählen Sie die Methode des Zeilenumbruchs. Im Zweifelsfall belassen Sie die Standardeinstellung und überprüfen die Darstellung in jeweiligen Portal.

-   **Anhänge**

    Wenn nicht anders benannt, belassen Sie die Standardeinstellung.

-   **Markierung**

    Wenn nicht anders benannt, belassen Sie die Standardeinstellung. Sollten keine Bilder beim Empfänger dargestellt werden, so ändern Sie die Einstellung und führen Sie einen erneuten Exportvorgang durch.

-   **Sonstiges**

    Wenn nicht anders benannt, belassen Sie die Standardeinstellung.


#### Einstellungen zu exportierten Bildern {#usage_realestate_export_form_images}

Wählen Sie im unteren Bereich des Formulars den Tab `Bilder` um Einstellungen für exportierte Bilder anzupassen.

-   Zur Immobilie können Bilder gespeichert werden, welche nicht auf den Portalen veröffentlicht werden sollen, weil z.B. eine Begrenzung der Anzahl der Bilder vorgegeben ist. Wenn Sie diese aber auf Ihrer Website darstellen wollen, so aktivieren Sie die Option Allgemein.

-   Es kann sinnvoll sein, die Bilder für den Website-Export zu verkleinern. Wenn Sie dies wünschen, so aktivieren Sie die Option `Skalierung` und tragen Sie die Maximalwerte für die Breite und Höhe (in Pixeln) ein.

-   Wenn Sie Ihr Firmenlogo als Wasserzeichen in die Bilder einfügen möchten, so aktivieren Sie die Option `Wasserzeichen`. Tragen Sie die Größe des Wasserzeichens ein, wählen die Position innerhalb der Bilder und den gewünschten Transparenz-Wert.


#### Änderungen speichern {#usage_realestate_export_form_submit}

Um die Änderungen im Formular dauerhaft zu speichern, klicken Sie oben rechts auf den Button `Speichern`.

{{< info >}}
Das Speichern ist zu jedem Zeitpunkt der Bearbeitung möglich. Sollten relevante Eingaben fehlen, so weist dass Programm darauf hin.
{{< /info >}}

{{< warning >}}
Jede Änderung im Immobilienformular muss mindestens am Ende der Bearbeitung durch Klick auf Speichern dauerhaft gespeichert werden.
{{< /warning >}}
