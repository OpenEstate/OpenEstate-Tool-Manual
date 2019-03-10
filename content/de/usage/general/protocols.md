---

title: Protokolle des Programms einsehen
linktitle: Protokolle
description: Protokolle von OpenEstate-ImmoTool verwalten…
weight: 80

menu:
  main:
    parent: usage-general
    identifier: usage-general-protocols

---

## Protokolle {#usage_general_protocols}

Warnungen, Probleme oder Fehler, die während der Nutzung des Programms auftreten, werden im Hintergrund automatisch protokolliert. Die Protokolle werden im Unterordner **`logs`** des [Daten-Verzeichnisses]({{< relref "../../admin/client/directories.md#admin_client_directories_data" >}}) tageweise abgelegt.

Klicken Sie im Hauptmenü auf **"Extras → Protokolle"** um die derzeit vorliegenden Protokolle einzusehen.

{{< figure src="menu_extras.png" caption="Protokolle im Extras-Menü aufrufen" >}}

Die Protokoll-Datei **`ImmoTool.log`** speichert allgemeine Meldungen des ImmoTools. Für andere Programme (AdminTool / Handbuch) werden separate Protokoll-Dateien erzeugt (**`AdminTool.log`** / **`Manual.log`**).

{{< figure src="protocols.png" caption="Protokolle anzeigen" >}}

Abhängig von der Konfiguration können eventuell weitere Protokoll-Dateien vorliegen (z.B. **`ImmoTool-mail.log`**).
    
{{< info >}}
Die Protokoll-Dateien des aktuellen Tages haben kein Datum im Namen (z.B. **`ImmoTool.log`**). Ältere Dateien tragen im Namen das jeweilige Datum der Erstellung (z.B. **`ImmoTool.2012-01-20.log`**). Ältere Protokoll-Dateien werden vom Programm automatisch gelöscht.
{{< /info >}}


### Protokoll speichern {#usage_general_protocols_export}

Auf Anfrage der Kunden-Supports kann es nötig werden die Protokolle zu übermitteln. Wählen Sie in der Auswahlbox die zu speichernde Protokoll-Datei und klicken Sie auf **"Speichern"**. Es erscheint ein Untermenü mit zwei Optionen.

-   **Als Datei speichern:** \
    Das Protokoll wird in einer separaten Datei gespeichert und kann z.B. als Anhang einer E-Mail verschickt werden.

-   **In die Zwischenablage speichern:** \
    Das Protokoll wird in die Zwischenablage gespeichert und kann z.B. in den Text einer E-Mail kopiert werden.
