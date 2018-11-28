---

title: Einrichtung von E-Mailkonten
linktitle: E-Mailkonten
description: Hinweise zur Einrichtung von E-Mailkonten in OpenEstate-ImmoTool…
weight: 30

menu:
  main:
    parent: usage-email
    identifier: usage-email-account

---

## E-Mailkonten einrichten {#usage_email_accounts}


### Was sind E-Mailkonten? {#usage_email_accounts_info}

Um E-Mails mit dem ImmoTool empfangen und versenden zu können, muss dem Programm mitgeteilt werden über welchen E-Mailserver dies stattfinden soll. Der E-Mailserver wird in der Regel von Ihrem E-Mailanbieter bereitgestellt (z.B. GMX / GMail / Hotmail).

Für jede E-Mailadresse, die mit dem ImmoTool genutzt werden soll, können Sie im Programm ein sogenanntes "E-Mailkonto" einrichten. Es können beliebig viele solcher E-Mailkonten im Programm erfasst werden.

> **Hinweis**
>
> Die technischen Details zur Einrichtung des E-Mailkontos erfahren Sie von Ihrem E-Mailanbieter. Die relevanten technischen Details einiger E-Mailanbieter finden Sie im Kapitel über [E-Mailanbieter]({{< relref "providers.md#usage_email_providers" >}}).


### E-Mailkonto hinzufügen {#usage_email_accounts_add}

Klicken Sie im Hauptmenü auf `E-Mails` → `E-Mailkonten verwalten` um das [Dialogfenster zur Bearbeitung der Mailkonten](#usage_email_accounts_setup) zu öffnen.

Klicken Sie in dem Fenster unten links auf den Button `Aktionen` → `Hinzufügen` um ein neues Mailkonto vorzubereiten. Nehmen Sie die nötigen Änderungen vor und klicken Sie abschließend auf `Übernehmen`.


### E-Mailkonto bearbeiten {#usage_email_accounts_edit}

Klicken Sie im Hauptmenü auf `E-Mails` → `E-Mailkonten verwalten` um das [Dialogfenster zur Bearbeitung der Mailkonten](#usage_email_accounts_setup) zu öffnen.

Wählen Sie auf der linken Seite des Fensters das zu bearbeitende E-Mailkonto aus. Nehmen Sie die nötigen Änderungen auf der rechten Seite des Fensters vor und klicken Sie abschließend auf `Übernehmen`.


### E-Mailkonto löschen {#usage_email_accounts_remove}

Klicken Sie im Hauptmenü auf `E-Mails` → `E-Mailkonten verwalten` um das [Dialogfenster zur Bearbeitung der Mailkonten](#usage_email_accounts_setup) zu öffnen.

Wählen Sie auf der linken Seite des Fensters das zu bearbeitende E-Mailkonto aus. Klicken Sie unten links auf den Button `Aktionen` → `Entfernen` um ein neues Mailkonto zu entfernen und klicken Sie abschließend auf `Übernehmen`.


### E-Mailkontoverwaltung {#usage_email_accounts_setup}

Klicken Sie im Hauptmenü auf `E-Mails` → `E-Mailkonten verwalten` um das Dialogfenster zur Bearbeitung der Mailkonten zu öffnen.

{{< figure src="account_dialog.jpg" caption="Dialogfenster zur Verwaltung der E-Mailkonten" >}}

Auf der linken Seite des Dialogfensters wird eine Liste der aktuell erfassten E-Mailkonten dargestellt. Wird auf der linken Seite ein E-Mailkonto gewählt, werden auf der rechten Seite die zugehörigen Formulare zur Bearbeitung des E-Mailkontos dargestellt.


#### Allgemeine Angaben {#usage_email_accounts_setup_general}

Verschiedene allgemeine Angaben können zu jedem E-Mailkonto hinterlegt werden.

{{< figure src="account_general.jpg" caption="Allgemeine Einstellungen eines E-Mailkontos" >}}

-   **Bezeichnung**
    Die Bezeichng wird innerhalb des Programmes an verschiedenen Stellen verwendet. Wählen Sie hier einen möglichst prägnanten und kurzen Namen aus.

-   **Ihr Name**
    Dieser Name wird bei versendeten E-Mails als Absender übermittelt.

-   **E-Mail**
    Diese E-Mailadresse wird bei versendeten E-Mails als Absender übermittelt. Einige E-Mailanbieter schreiben hier eine bestimmten Adresse vor, bei anderen E-Mailanbietern kann die Adresse frei gewählt werden.

-   **Antwort an**
    Wenn hier eine E-Mailadresse angegeben wurde, werden ausgehende Mails mit dem Vermerk versehen, dass eine Antwort möglichst an diese Adresse zurück zu senden ist.

-   **Signatur**
    Der hier eingetragene Text wird beim Verfassen einer neuen E-Mail automatisch unterhalb des Mail-Textes angefügt.


#### Empfang via IMAP {#usage_email_accounts_setup_imap}

Um eingehende Nachrichten über das **IMAP**-Protokoll vom E-Mailserver abholen zu können, öffnen Sie den Bereich `Empfang` und wählen Sie `IMAP` als Protokoll aus. Daraufhin wird ein Formular dargestellt, über welches die Anbindung des IMAP-Mailservers eingestellt werden kann.

{{< figure src="account_imap.jpg" caption="IMAP-Einstellungen eines E-Mailkontos" >}}

-   **Server**
    Tragen Sie hier die IP-Adresse oder den Hostnamen des IMAP-Mailservers ein.

-   **Port**
    Tragen Sie hier die Port-Nummer des IMAP-Mailservers ein.

-   **Anmeldung**
    Tragen Sie hier die Art der Anmeldung am IMAP-Mailserver ein.

-   **Benutzer**
    Tragen Sie hier Ihren IMAP-Benutzernamen ein, wenn eine Anmeldung am IMAP-Mailserver stattfindet.

-   **Paswort**
    Tragen Sie hier Ihr IMAP-Passwort ein, wenn eine Anmeldung am IMAP-Mailserver stattfindet.

-   **Krypto**
    Wählen Sie aus, ob die Kommunikation mit dem IMAP-Mailserver verschlüsselt stattfindet.


> **Hinweis**
>
> Die nötigen Einstellungen erfahren Sie von Ihrem E-Mailanbieter. Die IMAP-Einstellungen einiger E-Mailanbieter finden Sie im Kapitel über [E-Mailanbieter]({{< relref "providers.md#usage_email_providers_imap" >}}).


Folgende Port-Nummern werden bei IMAP meist für die verschiedenen Verschlüsselungsverfahren verwendet:

| Verschlüsselung | Port-Nr |
| --------------- | -------:|
| unverschlüsselt | `143`   |
| STARTTLS        | `143`   |
| IMAPS           | `993`   |


#### Empfang via POP3 {#usage_email_accounts_setup_pop3}

Um eingehende Mails über das **POP3**-Protokoll vom E-Mailserver abholen zu können, öffnen Sie den Bereich `Empfang` und wählen Sie `POP3` als Protokoll aus. Daraufhin wird ein Formular dargestellt, über welches die Anbindung des POP3-Mailservers eingestellt werden kann.

{{< figure src="account_pop3.jpg" caption="POP3-Einstellungen eines E-Mailkontos" >}}

-   **Server**
    Tragen Sie hier die IP-Adresse oder den Hostnamen des POP3-Mailservers ein.

-   **Port**
    Tragen Sie hier die Port-Nummer des POP3-Mailservers ein.

-   **Anmeldung**
    Tragen Sie hier die Art der Anmeldung am POP3-Mailserver ein.

-   **Benutzer**
    Tragen Sie hier Ihren POP3-Benutzernamen ein, wenn eine Anmeldung am POP3-Mailserver stattfindet.

-   **Paswort**
    Tragen Sie hier Ihr POP3-Passwort ein, wenn eine Anmeldung am POP3-Mailserver stattfindet.

-   **Krypto**
    Wählen Sie aus, ob die Kommunikation mit dem POP3-Mailserver verschlüsselt stattfindet.

> **Hinweis**
>
> Die nötigen Einstellungen erfahren Sie von Ihrem E-Mailanbieter. Die POP3-Einstellungen einiger E-Mailanbieter finden Sie im Kapitel über [E-Mailanbieter]({{< relref "providers.md#usage_email_providers_pop3" >}}).

Folgende Port-Nummern werden bei POP3 meist für die verschiedenen Verschlüsselungsverfahren verwendet:

| Verschlüsselung | Port-Nr |
| --------------- | -------:|
| unverschlüsselt | `110`   |
| STARTTLS        | `110`   |
| POP3S           | `995`   |


#### Versand via SMTP {#usage_email_accounts_setup_smtp}

Um ausgehende Mails über das **SMTP**-Protokoll versenden zu können, öffnen Sie den Bereich `Versand` und wählen Sie `SMTP` als Protokoll aus. Daraufhin wird ein Formular dargestellt, über welches die Anbindung des SMTP-Mailservers eingestellt werden kann.

{{< figure src="account_smtp.jpg" caption="SMTP-Einstellungen eines E-Mailkontos" >}}

-   **Server**
    Tragen Sie hier die IP-Adresse oder den Hostnamen des SMTP-Mailservers ein.

-   **Port**
    Tragen Sie hier die Port-Nummer des SMTP-Mailservers ein.

-   **Anmeldung**
    Tragen Sie hier die Art der Anmeldung am SMTP-Mailserver ein.

-   **Benutzer**
    Tragen Sie hier Ihren SMTP-Benutzernamen ein, wenn eine Anmeldung am SMTP-Mailserver stattfindet.

-   **Paswort**
    Tragen Sie hier Ihr SMTP-Passwort ein, wenn eine Anmeldung am SMTP-Mailserver stattfindet.

-   **Krypto**
    Wählen Sie aus, ob die Kommunikation mit dem SMTP-Mailserver verschlüsselt stattfindet.

> **Hinweis**
>
> Die nötigen Einstellungen erfahren Sie von Ihrem E-Mailanbieter. Die SMTP-Einstellungen einiger E-Mailanbieter finden Sie im Kapitel über [E-Mailanbieter]({{< relref "providers.md#usage_email_providers_smtp" >}}).

Folgende Port-Nummern werden bei SMTP meist für die verschiedenen Verschlüsselungsverfahren verwendet:

| Verschlüsselung | Port-Nr       |
| --------------- | -------------:|
| unverschlüsselt | `25`          |
| STARTTLS        | `25` & `587`  |
| SMTPS           | `465` & `587` |


#### E-Mailordner zuweisen {#usage_email_accounts_folders}

Für jedes E-Mailkonto können verschiedene Standard-Mailordner eingestellt werden.

{{< figure src="account_folders.jpg" caption="Ordner-Einstellungen eines E-Mailkontos" >}}

-   **Postausgang**
    Wenn eine E-Mail über das Mailkonto versendet wird, speichert das Programm eine Kopie der versendeten Nachricht in diesem Ordner ab.

-   **Entwürfe**
    Wenn eine E-Mail während der Bearbeitung gespeichert wird, speichert das Programm die ungesendete Nachricht in diesem Ordner ab.

-   **Papierkorb**
    Wenn eine E-Mail aus dem Mailkonto gelöscht wird, verschiebt das Programm die Nachricht in diesen Ordner statt diese sofort zu löschen.

Um einen anderen E-Mailordner zu wählen, klicken Sie auf den jeweiligen Button. Es öffnet sich daraufhin ein Fenster, über welches der Zielordner ausgewählt werden kann.

Wenn für eine der Aktionen kein Mailordner verwendet werden soll, kann rechts neben dem jeweiligen Button auf `inaktiv` geklickt werden.


#### Erweiterte Einstellungen {#usage_email_accounts_setup_extended}

Abhängig vom E-Mailanbieter können weitere Einstellungen hinterlegt werden. Im Regelfall ist dies jedoch nicht nötig.

{{< figure src="account_properties.jpg" caption="Erweiterte Einstellungen eines E-Mailkontos" >}}

Klicken Sie oberhalb der Tabelle auf den Button `+` um einen leeren Eintrag in die Tabelle einzufügen. Um einen markierten Eintrag zu entfernen, klicken Sie auf den Button `-`.

Die möglichen Einstellungen sind in der Javamail-API dokumentiert:

-   [Javamail-Einstellungen für IMAP](http://javamail.kenai.com/nonav/javadocs/com/sun/mail/imap/package-summary.html)
-   [Javamail-Einstellungen für POP3](http://javamail.kenai.com/nonav/javadocs/com/sun/mail/pop3/package-summary.html)
-   [Javamail-Einstellungen für SMTP](http://javamail.kenai.com/nonav/javadocs/com/sun/mail/smtp/package-summary.html)


#### Änderungen speichern {#usage_email_accounts_setup_submit}

Um die Änderungen im Formular dauerhaft zu speichern, klicken Sie auf den Button `Übernehmen`.
