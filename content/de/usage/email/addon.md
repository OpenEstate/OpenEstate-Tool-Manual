---

title: Allgemeines zum E-Mail-Addon
linktitle: Allgemeines
description: Allgemeine Hinweise zum E-Mail-Addon von OpenEstate-ImmoTool…
weight: 10

menu:
  main:
    parent: usage-email
    identifier: usage-email-addon

---

## Über das E-Mail Add-On {#usage_email_addon}

Die Funktionen zum Empfang und Versand von E-Mails werden vom "E-Mail Add-On" in das ImmoTool integriert. In diesem Kapitel werden diese Funktionen dokumentiert.

Die folgenden Bestandteile werden in das Programm integriert, wenn das "E-Mail Add-On" installiert und aktiviert wurde:

{{< figure src="menu.jpg" caption="Menüeintrag der E-Mailverwaltung" >}}

{{< figure src="sidebar.jpg" caption="Ansichtsbereich der E-Mailverwaltung" >}}

> **Hinweis**
>
> Um das "E-Mail Add-On" verwenden zu können benötigen Sie eine E-Mailadresse, die einen Zugriff über die Mailprotokolle **POP3**, **IMAP** und/oder **SMTP** ermöglicht. Dies ist bei den meisten E-Mailanbietern der Fall. Die relevanten technischen Details einiger E-Mailanbieter finden Sie im Kapitel über [E-Mailanbieter]({{< relref "providers.md#usage_email_providers" >}}).


### Einstellungen {#usage_email_addon_settings}

Die folgenden Einstellungen werden vom "E-Mail Add-On" in die [Programm-Einstellungen]({{< relref "../general/settings.md#usage_general_settings" >}}) eingefügt.

> **TODO**
>
> Inhalte einfügen


### Fragen & Antworten zum E-Mail Add-On {#usage_email_addon_faq}

> **TODO**
>
> Inhalte einfügen


#### Soll ich IMAP oder POP3 für den Mailempfang verwenden?

Wenn Sie die Wahl haben, empfiehlt es sich das **IMAP**-Protokoll zu verwenden. Dieses Protokoll ermöglicht die Verwendung von Ordnern im Mailkonto und macht weniger Probleme bei der gleichzeitigen Verwendung unterschiedlicher Mailprogramme.

Das **POP3**-Protokoll unterstützt nur die wichtigsten Grundfunktionen - insbesondere das Abholen & Löschen von Nachrichten aus dem E-Mailkonto. Mit POP3-Mailkonten können deshalb nicht alle Funktionen des ImmoTools verwendet werden. Zum Beispiel steht bei **POP3** keine Ordnerverwaltung auf den Mailservern zur Verfügung - statt dessen werden E-Mails in einen lokalen Mailordner heruntergeladen.
