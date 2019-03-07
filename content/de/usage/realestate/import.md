---

title: Immobilien importieren
linktitle: Importe
description: Hinweise zum Import von Immobilien in OpenEstate-ImmoTool…
weight: 60

menu:
  main:
    parent: usage-realestate
    identifier: usage-realestate-import

---

## Immobilien importieren {#usage_realestate_import}

Das ImmoTool kann externe Immobiliendaten in verschiedenen Formaten einlesen und in die Datenbank speichern. Derzeit unterstützt das Programm die folgenden Formate zum Import von Immobiliendaten:

-   OpenEstate-XML
-   Openimmo-XML 1.1 & 1.2
-   ImmoXML
-   IS24-XML (rev67445)
-   IS24-CSV (v1.4.0.4)

Klicken Sie im Hauptmenü auf **"Immobilien → Immobilien importieren"** und wählen Sie das Format aus, in dem die zu importierenden Immobiliendaten vorliegen.

{{< figure src="menu_import.jpg" caption="Import über das Hauptmenü starten" >}}

Wählen Sie im folgenden Dialogfenster die zu importierende Datei aus. Die Datei kann eine XML- oder CSV-Datei sein. Oder es kann ein ein ZIP-Archiv gewählt werden, welches eine XML- oder CSV-Datei enthält. Mit einem Klick auf **"Datei importieren"** wird der Import-Vorgang gestartet.

Es öffnet sich ein Dialogfenster, in welchem Ausgaben zum Import-Vorgang zu sehen sind. Sollte die zu importierende Datei einen Fehler auslösen, so wird dies hier protokolliert.

Wenn bei der Initialisierung des Imports kein Fehler auftritt öffnet sich ein weiteres Dialogfenster, in welchem Sie aufgefordert werden den Status der zu importierenden Immobilien zu wählen. Treffen Sie eine Auswahl und klicken Sie auf den Button **"Übernehmen"**.

{{< info >}}
Prüfen Sie nach erfolgtem Import Ihren Immobilienbestand auf Korrektheit und nehmen Sie ggf. nachträgliche Korrekturen vor.
{{< /info >}}

{{< todo >}}
Neue Vorgehensweise zum Immobilien-Import beschreiben.
{{< /todo >}}
