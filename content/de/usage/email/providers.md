---

title: Bekannte E-Mailanbieter
linktitle: E-Mailanbieter
description: Technische Details bekannter E-Mailanbieter…
weight: 40

menu:
  main:
    parent: usage-email
    identifier: usage-email-providers

---

## E-Mailanbieter {#usage_email_providers}

Im Folgenden finden Sie die technischen Eckdaten verschiedener E-Mailanbieter, die zur Einrichtung eines E-Mailkontos im ImmoTool verwendet werden können.

Selbstverständlich können auch beliebige andere E-Mailanbieter mit dem ImmoTool verwendet werden, wenn diese die üblichen Protokolle ([IMAP](http://de.wikipedia.org/wiki/Internet_Message_Access_Protocol), [POP3](http://de.wikipedia.org/wiki/Post_Office_Protocol), [SMTP](http://de.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)) unterstützen.


### E-Mailempfang via IMAP {#usage_email_providers_imap}

Die folgende Tabelle enthält einer Übersicht der IMAP-Einstellungen von verschiedenen bekannten E-Mailanbietern. Abhängig von der gewählten Verschlüsselungstechnik ("Krypto") muss eine bestimmte Port-Nr bei der [Einrichtung des Mailempfangs via IMAP](usage_email_accounts.md#usage_email_accounts_setup_imap) verwendet werden.

| Anbieter | Anmeldung | Krypto     | Server                | Port  |
| -------- | --------- | ---------- | --------------------- | -----:|
| [GMail]  | `LOGIN`¹  | `IMAPS`    | `imap.googlemail.com` | `993` |
| [GMX]    | `LOGIN`¹  | `IMAPS`    | `imap.gmx.net`        | `993` |
| [Web.de] | `LOGIN`¹  | `STARTTLS` | `imap.web.de`         | `143` |
|          |           | `IMAPS`    | `imap.web.de`         | `993` |
| [Yahoo]  | `LOGIN`¹  | `IMAPS`    | `imap.mail.yahoo.com` | `993` |

**¹** Für die Anmeldung beim IMAP-Server muss die E-Mailadresse als Login-Name und das gewählte Passwort im Programm eingetragen werden.


### E-Mailempfang via POP3 {#usage_email_providers_pop3}

Die folgende Tabelle enthält einer Übersicht der POP3-Einstellungen von verschiedenen bekannten E-Mailanbietern. Abhängig von der gewählten Verschlüsselungstechnik ("Krypto") muss eine bestimmte Port-Nr bei der [Einrichtung des Mailempfangs via POP3](usage_email_accounts.md#usage_email_accounts_setup_pop3) verwendet werden.

| Anbieter | Anmeldung | Krypto     | Server                | Port  |
| -------- | --------- | ---------- | --------------------- | -----:|
| [GMail]  | `LOGIN`¹  | `POP3S`    | `pop.googlemail.com`  | `995` |
| [GMX]    | `LOGIN`¹  | `POP3S`    | `pop.gmx.net`         | `995` |
| [Web.de] | `LOGIN`¹  | `STARTTLS` | `pop3.web.de`         | `110` |
|          |           | `POP3S`    | `pop3.web.de`         | `995` |
| [Yahoo]  | `LOGIN`¹  | `POP3S`    | `pop.mail.yahoo.com`  | `995` |

**¹** Für die Anmeldung beim POP3-Server muss die E-Mailadresse als Login-Name und das gewählte Passwort im Programm eingetragen werden.


### E-Mailversand via SMTP {#usage_email_providers_smtp}

Die folgende Tabelle enthält einer Übersicht der SMTP-Einstellungen von verschiedenen bekannten E-Mailanbietern. Abhängig von der gewählten Verschlüsselungstechnik ("Krypto") muss eine bestimmte Port-Nr bei der [Einrichtung des Mailversands via SMTP](usage_email_accounts.md#usage_email_accounts_setup_smtp) verwendet werden.

| Anbieter | Anmeldung | Krypto     | Server                | Port  |
| -------- | --------- | ---------- | --------------------- | -----:|
| [GMail]  | `LOGIN`¹  | `SMTPS`    | `smtp.gmail.com`      | `465` |
|          |           | `STARTTLS` | `smtp.gmail.com`      | `587` |
| [GMX]    | `LOGIN`¹  | *keine*    | `mail.gmx.net`        | `25`  |
|          |           | `SMTPS`    | `mail.gmx.net`        | `465` |
| [Web.de] | `LOGIN`¹  | *keine*    | `smtp.web.de`         | `25`  |
|          |           | `STARTTLS` | `smtp.web.de`         | `587` |
| [Yahoo]  | `LOGIN`¹  | *keine*    | `smtp.mail.yahoo.com` | `25`  |
|          |           | `SMTPS`    | `smtp.mail.yahoo.com` | `465` |

**¹** Für die Anmeldung beim SMTP-Server muss die E-Mailadresse als Login-Name und das gewählte Passwort im Programm eingetragen werden.


[GMail]:  http://mail.google.com/
[GMX]:    http://www.gmx.net/
[Web.de]: http://web.de/
[Yahoo]:  http://yahoo.com/

