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

Das ImmoTool kann externe Immobiliendaten in verschiedenen Formaten einlesen und in die Datenbenk speichern. Derzeit unterstützt das Programm die folgenden Formate zum Import von Immobiliendaten:

-   OpenEstate-XML
-   Openimmo-XML 1.1 & 1.2
-   ImmoXML
-   IS24-XML (rev67445)
-   IS24-CSV (v1.4.0.4)


### Immobilien aus einer Datei importieren {#usage_realestate_import_file}

Klicken Sie im Hauptmenü auf `Immobilien` → `Immobilien importieren` und wählen Sie das Format aus, in dem die zu importierenden Immobiliendaten vorliegen.

{{< figure src="menu_import.jpg" caption="Import über das Hauptmenü starten" >}}

Wählen Sie im folgenden Dialogfenster die zu importierende Datei aus. Die Datei kann eine XML- oder CSV-Datei sein. Oder es kann ein ein ZIP-Archiv gewählt werden, welches eine XML- oder CSV-Datei enthält. Mit einem Klick auf `Datei importieren` wird der Importvorgang gestartet.

Es öffnet sich ein Infofenster, in welchem Ausgaben zum Importvorgang zu sehen sind. Sollte die zu importierende Datei einen Fehler auslösen, so wird dies hier protokolliert.

Wenn bei der Innitialisierung des Imports kein Fehler auftritt öffnet sich ein weiteres Dialogfenster, in welchem Sie aufgefordert werden den Status der zu importierenden Immobilien zu wählen. Treffen Sie eine Auswahl und klicken Sie auf den Button `Übernehmen`.

> **Hinweis**
>
> Prüfen Sie nach erfolgtem Datenimport Ihren Immobilienbestand auf Korrektheit und nehmen Sie ggf. nachträgliche Korrekturen vor.


### Immobilien aus vorhandener Maklersoftware importieren {#usage_realestate_import_ftp}

Moderne Softwarelösungen für Immobilienmakler bieten in der Regel eine Funktion zum Datenexport via `FTP` und im Format `OpenImmo-XML`. In der Regel wird diese Funktion in der Maklersoftware genutzt, um Immobilien an verschiedene Immobilienportale zu versenden.

Statt aus einer anderen Maklersoftware heraus ein Immobilienportal zu beliefern, kann ein Export direkt zum ImmoTool durchgeführt werden. Für diesen Zweck liefert das ImmoTool einen eigenen minimalen FTP-Server mit, zu dem die Immobiliendaten aus einer anderen Maklersoftware gesendet werden können - als wäre das ImmoTool ein Immobilienportal.

> **Achtung**
>
> Diese Programmfunktion befindet sich noch in einem experimentellen Status! Bitte teilen Sie uns Ihre Erfahrungen mit.

> **Hinweis**
>
> Dieses Verfahren funktioniert nicht, wenn Sie eine Online-Software verwenden. Sowohl das ImmoTool als auch die andere Software müssen sich auf dem gleichen Rechner oder in Ihrem lokalen Netzwerk befinden.

Klicken Sie im Hauptmenü auf `Immobilien` → `Immobilien importieren` → `via Maklersoftware-Export`. Darauf wird das folgende Fenster dargestellt:

{{< figure src="import_ftp.jpg" caption="Immobilien via FTP importieren" >}}

Gehen Sie wie folgt vor, um die Immobilien aus einer externen Maklersoftware zum ImmoTool zu übertragen:

1.  Installieren Sie in Ihrer externen Maklersoftware eine Export-Schnittstelle. Beachten Sie dabei:

    -   Der Export kann im Format `Openimmo-XML`, `IS24-XML` oder `IS24-CSV` erfolgen.

    -   Die Adresse des FTP-Servers entspricht in der Regel `127.0.0.1`. Alternativ können Sie die IP-Adresse Ihres Rechners in Ihrem Netzwerk eintragen.

    -   Tragen Sie als Port des FTP-Servers den gleichen Wert ein, der im Import-Fenster des ImmoTools angezeigt wird.

    -   Die Zugangsdaten für den FTP-Server können frei gewählt werden.

2.  Klicken Sie im Import-Fenster des ImmoTools auf `FTP-Server starten` um den FTP-Server auf dem gewählten Port zu starten.

3.  Exportieren Sie nun mit Ihrer externen Maklersoftware Ihre Inserate. Sobald Aktivitäten stattfinden werden diese im Import-Fenster des ImmoTools protokolliert.

4.  Nachdem Sie Ihre Daten aus der externen Maklersoftware übertragen haben, klicken Sie im Import-Fenster des ImmoTools auf `FTP-Server stoppen`. Das Programm ermittelt daraufhin, ob es während der FTP-Sitzung zu Dateiübertragungen kam.

5.  Sollten importierbare Dateien empfangen worden sein, werden Sie gefragt, ob diese importiert werden sollen. Beantworten Sie diese Frage mit `Ja`  und das Programm wird versuchen die übertragenen Dateien zu importieren.

> **Hinweis**
>
> Beim Schließen des Import-Fensters werden nicht importierte Dateien gelöscht!

> **Hinweis**
>
> Um eine Port-Nr kleiner als `1000` verwenden zu können, muss das Programm mit Administratorrechten gestartet werden. Dabei handelt es sich um eine Sicherheitsbeschränkung von Java.

> **Hinweis**
> Prüfen Sie nach erfolgtem Datenimport Ihren Immobilienbestand auf Korrektheit und nehmen Sie ggf. nachträgliche Korrekturen vor.
