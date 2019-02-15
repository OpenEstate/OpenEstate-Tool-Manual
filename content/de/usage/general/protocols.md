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

Warnungen, Probleme oder Fehler, die während der Nutzung des Programms auftreten, werden im Hintergrund automatisch protokolliert. Die Protokolle werden im Unterverzeichnis `logs` des Programmes tageweise abgelegt.

Klicken Sie im Hauptmenü auf `Extras` → `Protokolle`, um die derzeit vorliegenden Protokolle einzusehen.

{{< figure src="menu_extras.jpg" caption="Protokolle im Extras-Menü aufrufen" >}}

Es werden verschiedene Arten von Protokoll-Dateien erstellt.

-   **System-Protokolle**
    Das Protokoll `system.log` speichert allgemeine Meldungen des Programms.

-   **Datenbank-Protokolle**
    Das Protokoll `exist.log` speichert Warnungen & Fehler der ImmoTool-Datenbank.

{{< info >}}
Die Protokoll-Dateien des aktuellen Tages haben kein Datum im Namen (z.B. `system.log`). Ältere Dateien tragen im Namen das jeweilige Datum der Erstellung (z.B. `system.log.2012-01-20`).
{{< /info >}}


### Protokoll speichern {#usage_general_protocols_export}

Auf Anfrage der Kunden-Supports kann es nötig werden die Protokolle zu übermitteln. Wählen Sie in der Auswahlbox die zu speichernde Protokoll-Datei und klicken Sie auf `Speichern`. Es erscheint ein Untermenü mit zwei Optionen.

-   **Speichern als Datei.**
    Das Protokoll wird in einer separaten Datei gespeichert und kann z.B. als Anhang einer E-Mail verschickt werden.

-   **Speichern in die Zwischenablage.**
    Das Protokoll wird in die Zwischenablage gespeichert und kann z.B. in den Text einer E-Mail kopiert werden.

