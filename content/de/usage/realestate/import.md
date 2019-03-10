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

-   OpenEstate-XML (Version 1.0)
-   Openimmo-XML (Version 1.1 - 1.7b)
-   IS24-XML (Version rev189438)
-   IS24-CSV (Version 1.4.0.4)
-   ImmoXML (Version 3.0)
-   Immobiliara-XML (Version 2.5)
-   IDX  (Version 3.01)
-   Kyero-XML (Version 2.1 & 3.0)

Klicken Sie im Hauptmenü auf **"Immobilien → sonstiges → Immobilien importieren"**.

{{< figure src="menu_import.png" caption="Import über das Hauptmenü starten" >}}

Navigieren Sie im folgenden Dialogfenster zu der zu importirenden Immobiliendatei. Die Datei muss in einem der oben genannten Formate vorliegen. Die Datei kann ein ZIP-Archiv sein, welches eine XML- oder CSV-Datei enthält.

{{< figure src="import_form.png" caption="zu importierende Datei auswählen" >}}

Markieren Sie die Datei mit der Maus und klicken auf den Button **"Überprüfen"**. Das ImmoTool überprüft nun die Datei und übernimmt, wenn möglich, das Format und die Version in das Formular. Tragen Sie die entsprechenden Einstellungen manuell ein, wenn das ImmoTool diese nicht feststellen konnte. Wenn die Datei gültig ist, also eine Datei in einem der oben genannten Formate ist, klicken Sie auf **"Import starten"**. Es öffnet sich ein Dialogfenster, in welchem Ausgaben zum Import-Vorgang zu sehen sind. Sollte die zu importierende Datei einen Fehler auslösen, so wird dies hier protokolliert. Am Ende des Imports zeigt das ImmoTool Ihnen die Anzahl der importierten und ignorierten Immobilien an.

Unter dem Reiter **"Optionen"** können Sie festlegen, wie mit den zu importierenden Datei umzugehen ist.

{{< figure src="import_form_options.png" caption="Importoptionen festlegen" >}}


{{< info >}}
Prüfen Sie nach erfolgtem Import Ihren Immobilienbestand auf Korrektheit und nehmen Sie ggf. nachträgliche Korrekturen vor.
{{< /info >}}
