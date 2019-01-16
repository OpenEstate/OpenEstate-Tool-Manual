---

title: Verwendung des E-Mail Add-Ons
linktitle: Verwaltung
description: Allgemeine Hinweise zur Verwendung des E-Mail Add-Ons von OpenEstate-ImmoTool…
weight: 20

menu:
  main:
    parent: usage-email
    identifier: usage-email-manage

---

## E-Mails verwalten {#usage_email_manage}


### E-Mails lesen {#usage_email_manage_read}

Nachdem ein E-Mailkonto mit Mailempfang eingerichtet wurde kann auf den Inhalt der E-Mailkonten zugegriffen werden. Klicken Sie dafür im Hauptmenü auf `E-Mails` → `E-Mailansicht öffnen`.

-   E-Mailkonten mit Mailempfang via **IMAP** werden in der Sidebar mit den jeweiligen Unter-Ordnern dargestellt (z.B. Posteingang, Postausgang, etc.).
-   E-Mailkonten mit Mailempfang via **POP3** werden **nicht** in der Sidebar dargestellt. Empfange Mails werden in diesem Falle automatisch in den gewählten Posteingangs-Ordner gespeichert.

Wählen Sie in der Sidebar einen E-Mailordner aus, dessen Inhalt dargestellt werden soll. Es wird daraufhin die [Ansicht des E-Mailordners](#usage_email_manage_folder) geöffnet.


### Ansicht eines E-Mailordners {#usage_email_manage_folder}

Nachdem ein E-Mailordner in der Sidebar angeklickt wurde, wird eine tabellarische Übersicht der im Ordner enthaltenen E-Mails dargestellt:

{{< figure src="inbox.jpg" caption="Inhalt eines E-Mailordners anzeigen" >}}

> **TODO**
>
> weitere Inhalte einfügen (z.B. Aktionen in der Tabelle)


### Ansicht einer E-Mail {#usage_email_manage_message}

Klicken Sie in der [Ansicht des E-Mailordners](#usage_email_manage_folder) mit der linken Maustaste auf eine Mitteilung in der Tabelle. Unterhalb der Tabelle wird die angeklickte Nachricht dargestellt. Alternativ kann die Mitteilung durch einen Doppelklick mit der linken Maustaste als separates Fenster geöffnet werden.

{{< figure src="message.jpg" caption="E-Mail in HTML-Ansicht" >}}

> **TODO**
>
> weitere Inhalte einfügen (z.B. Zugriff auf Anhänge)


### E-Mails aus Adressbuch versenden {#usage_email_manage_addressbook}

In der [Übersicht der Adressen]({{< relref "../addressbook/manage.md#usage_addressbook_manage_table" >}}) und im [Formular für Adressen]({{< relref "../addressbook/manage.md#usage_addressbook_manage_form" >}}) kann über das Aktionsmenü die Erzeugung eine neuen E-Mail gestartet werden.

{{< figure src="compose_from_addressbook.jpg" caption="E-Mail aus dem Adressbuch verfassen" >}}

Auf diesem Wege erzeugt E-Mails werden beim Versand automatisch mit der gewählten Adresse verknüpft.


### E-Mail verfassen {#usage_email_manage_compose}

Nachdem mindestens ein E-Mailkonto mit Mailversand eingerichtet wurde können E-Mails erstellt und versendet werden. Klicken Sie dafür im Hauptmenü auf `E-Mails` → `E-Mail verfassen`. Daraufhin wird das folgende Formular zum Verfassen von E-Mails geöffnet:

{{< figure src="compose_form.jpg" caption="Formular zum Verfassen einer E-Mail-Nachricht" >}}


#### Absender wählen {#usage_email_manage_compose_sender}

Im Auswahleld `Absender` werden alle E-Mailkonten dargestellt, für die ein Mailversand eingerichtet wurde. Wählen Sie hier das E-Mailkonto aus, über welches die E-Mail versendet werden soll.


#### Empfänger bearbeiten {#usage_email_manage_compose_recipients}

Im oberen Bereich des Formulars können beliebig viele Empfänger für die Nachricht eingetragen werden.

> **TODO**
>
> weitere Inhalte einfügen (Hinzufügen, Entfernen, Bearbeiten von Empfängern; Anbindung an das Adressbuch Add-On)

Die folgenden Arten von Empfängern stehen zur Verfügung:

-   **TO**
    An diese Empfänger wird die Nachricht primär gesendet.

-   **CC**
    An diese Empfänger wird die Nachricht als Kopie gesendet.

-   **BCC**
    An diese Empfänger wird die Nachricht als Blindkopie gesendet. Diese Empfänger sind für die anderen TO- und CC-Empfänger **nicht** sichtbar.

-   **REPLY_TO**
    An diesen Empfänger wird bevorzugt eine Antwort auf die Nachricht gesendet. Beachten Sie bitte, dass der Empfänger dieser Empfehlung nicht folgen muss und auch einen anderen Empfänger beim Beantworten auswählen kann.

> **Hinweis**
>
> Jedem Adressaten werden auch alle anderen **TO**- und **CC**-Einträge angezeigt.


#### Text der Nachricht eingeben {#usage_email_manage_compose_message}

Im mittleren Bereich des Formulars wird ein Textfeld dargestellt, in welches der Text der E-Mail eingetragen werden kann. Zusätzlich muss ein **Betreff** oberhalb des Textfelds eingegeben werden.

Beim Verfassen einer Mitteilung kann man zwischen verschiedenen Vorgehensweisen im Umgang mit Text- & HTML-Modus wählen.

{{< figure src="compose_modes.jpg" caption="Verfahrensweisen zum Verfassen des Texts einer E-Mail" >}}

-   **nur HTML**
    Die E-Mail wird als HTML-formatierte Mitteilung eingegeben. Beim Versand wird automatisch eine alternative Variante des Texts ohne Formatierungen für Empfänger beigefügt, die keine HTML-Mitteilungen lesen können.

-   **nur Text**
    Die E-Mail wird als unformatierte Mitteilung eingegeben und als solche versendet.

-   **Text & HTML**
    Beim Verfassen kann die Nachricht im HTML-Format und als unformatierter Text getrennt voneinander eingegeben werden.


##### Text-Modus {#usage_email_manage_compose_message_plain}

Im Text-Modus kann nur einfacher Text eingegeben werden. Diese Darstellung ist barrierefrei und sollte mit jedem E-Mailprogramm funktionieren.

{{< figure src="compose_plain.jpg" caption="E-Mail als Text-Nachricht erstellen" >}}


##### HTML-Modus {#usage_email_manage_compose_message_html}

Im HTML-Modus können verschiedenste Formatierungen in der Nachricht eingefügt werden (Schriftarten, Aufzählungen, etc). Diese Darstellung kann beim Empfänger zu Problemen in der Darstellung führen.

{{< figure src="compose_html.jpg" caption="E-Mail als HTML-Nachricht erstellen" >}}


#### Anhänge verwalten {#usage_email_manage_compose_attachments}

Der Nachricht können beliebig viele Dateien als Anhang beigefügt werden. Klicken Sie dafür unten rechts auf den Button `Hinzufügen` und wählen Sie eine oder mehrere Dateien von der Festplatte aus.

Jede angehängte Datei wird unterhalb des Textbereiches als Symbol dargestellt. Um den Anhang nachträglich wieder zu entfernen, markieren Sie das jeweilige Symbol und klicken Sie auf Entfernen.

> **Hinweis**
>
> Abhängig vom E-Mailanbieter dürfen Anhänge nicht beliebig groß sein. In der Regel wird eine maximale Gesamtgröße für Anhänge vorgegeben, welches im Bereich von 5 bis 10 MB liegt. Erfragen Sie die genauen Limits bei Ihrem E-Mailanbieter.


#### Nachricht abschicken {#usage_email_manage_compose_send}

Nachdem die Eingaben im Formular vervollständigt wurden, klicken Sie oben rechts auf `Senden` um die Mitteilung zur verschicken.


#### Nachricht als Entwurf speichern {#usage_email_manage_compose_save}

Nachdem die Eingaben im Formular vervollständigt wurden, klicken Sie oben rechts auf `Speichern` um die Mitteilung als Entwurf zu speichern.

Es findet in diesem Falle kein Versand statt. Die Nachricht wird stattdessen im Entwurfs-Ordner des als Absender gewählten Mailkontos gespeichert. Wenn kein Entwurfs-Ordner ermittelt werden kann, wird alternativ der Entwurfs-Ordner im Benutzerkonto verwendet.

Die als Entwurf gespeicherte Nachricht kann zu einem späteren Zeitpunkt aus dem jeweiligen Ordner wieder geöffnet, weiter bearbeitet und versendet werden.
