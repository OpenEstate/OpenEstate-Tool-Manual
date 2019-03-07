---

title: Verwaltung von Projekten
linktitle: Projekte
description: Verwaltung von Projekten in OpenEstate-ImmoTool…
weight: 20

menu:
  main:
    parent: usage-general
    identifier: usage-general-projects

---

## Verwaltung von Projekten {#usage_general_projects}


### Was sind Projekte? {#usage_general_projects_info}

Ein Projekt ist im ImmoTool eine Datenbank. Im ImmoTool können mehrere Projekte parallel verwaltet werden. Jedes verwaltete Projekt besitzt eine eigenständige Datenbank und wird in separaten Verzeichnissen auf der Festplatte abgespeichert.

Abhängig vom Anwendungsfall kann es sinnvoll sein, die Immobilien nach Tätigkeit (Makler und Verwalter in einer Person) oder nach Kunden in getrennten Projekten zu verwalten. In diesen Fällen können mehrere Projekte parallel, z.B. ein Projekt als Verwalter und eines als Makler, eingerichtet werden.

Mindestens ein Projekt muss angelegt werden, um mit dem Programm arbeiten zu können.


### Der Projektassistent {#usage_general_projects_wizard}

Der Projektassistent hilft Ihnen bei der Erstellung eines neuen Projektes.

#### Erster Start {#usage_general_projects_wizard_startup_first}

Beim ersten Start des Programmes öffnet sich der Projektassistent, und Sie werden aufgefordert ein Projekt anzulegen.

#### Folgende Starts {#usage_general_projects_wizard_startup_later}

Bei folgenden Starts wird das zuletzt verwendete Projekt automatisch geladen.


### Ein neues Projekt erzeugen {#usage_general_projects_create}


#### Projektdaten bearbeiten {#usage_general_projects_create_settings}

-   **Projekt-Name**
    Tragen Sie hier den Namen Ihres Projektes ein. Verwenden Sie keine Umlaute, Leerzeichen oder Sonderzeichen.

-   **Projekt-Ordner**
    Es ist standardmäßig ein Pfad voreingestellt. Diesen können Sie im Regelfall einfach beibehalten. Bei Bedarf kann ein anderer Pfad gewählt werden, z.B. eine externe Datenquelle in Ihrem System.

-   **Lizenz bestätigen**
    Bitte bestätigen Sie die Nutzungslizenz des ImmoTools, bevor Sie Ihr Projekt erzeugen.

-   **Das Projekt automatisch beim Programmstart öffnen**
    Markieren sie die Checkbox, wenn Sie dieses Projekt bei jedem Programmstart automatisch öffnen möchten.

{{< figure src="projects_wizard_general.png" caption="Projekt-Assistent / Eigenschaften des Projekts" >}}


#### Firmendaten bearbeiten {#usage_general_projects_create_company}

Tragen Sie hier Ihre Firmendaten ein. Die installierten Add-Ons greifen an verschiedenen Stellen auf diese Eingaben zurück.

{{< figure src="projects_wizard_company.png" caption="Projekt-Assistent / Firmendaten des Projekts" >}}


#### Add-Ons auswählen {#usage_general_projects_create_addons}

Hier befindet sich die Übersicht der aktuell verfügbaren Add-Ons. Standardmäßig sind alle bei der Installation verfügbare Add-Ons aktiviert. Deaktivieren Sie die Add-Ons, welche Sie nicht in Ihrem Projekt verwenden möchten.

{{< figure src="projects_wizard_addons.png" caption="Projekt-Assistent / Aktivierte Add-Ons" >}}

{{< info >}}
Eine nachträgliche Änderung der Auswahl der Add-Ons ist jederzeit möglich, siehe Add-Ons / Module.
{{< /info >}}

{{< todo >}}
Link Add-Ons / Module in Info einfügen
{{< /todo >}}


#### Das neue Projekt speichern & öffnen {#usage_general_projects_create_submit}

Wenn Sie die Angaben in allen Tabs vorgenommen haben, speichern Sie Ihr Projekt mit dem Button Projekt erzeugen. Das erzeugte Projekt wird daraufhin automatisch geöffnet.


### Ein Projekt öffnen {#usage_general_projects_open}

Projekte können Sie entweder über den Projektassistenten oder direkt im Hauptmenü öffnen. 

-   Den Projektassistenten öffnen Sie im Hauptmenü unter **"Programm → Neues Projekt"**. 
-   Direkt öffnen Sie Projekte im Hauptmenü unter **"Programm → Projekt öffnen"**. 
-   Zuletzt verwendete Projekte öffnen Sie im Hauptmenü unter  **"Programm → zuletzt verwendet..."**.


#### Ein bereits existierendes Projekt öffnen {#usage_general_projects_open_exist}

Über den Projektassistenten.

{{< figure src="projects_wizard_open-project.png" caption="Projekt-Assistent / Firmendaten des Projekts" >}}

Oder direkt im Hauptmenü.

{{< figure src="projects_open-project.png" caption="Projekt-Assistent / Firmendaten des Projekts" >}}


#### Das zuletzt verwendete Projekt öffnen {#usage_general_projects_open_recent}

Über den Projektassistenten.

{{< figure src="projects_wizard_open-recent-project.png" caption="Projekt-Assistent / Firmendaten des Projekts" >}}

Oder direkt im Hauptmenü.

{{< figure src="projects_open-recent-project.png" caption="Projekt-Assistent / Firmendaten des Projekts" >}}


{{< todo >}}
Inhalte einfügen
{{< /todo >}}


### Fragen & Antworten zu Projekten {#usage_general_projects_faq}


#### Wo wird mein Projekt gespeichert? {#usage_general_projects_faq_location}

Standardmäßig werden Projekte in das Verzeichnis **`OpenEstate-Files`** im Benutzerverzeichnis des im Betriebssystem angemeldeten Benutzer abgelegt. Sie können beim Anlegen eines Projekts ggf. eine beliebige andere Stelle angeben. Darauf sollten Sie aber verzichten, wenn dies nicht zwingend notwendig ist.


#### Wie kann ich mein Projekt an eine andere Stelle verschieben? {#usage_general_projects_faq_move}

Verschieben oder kopieren Sie das Projektverzeichnis an eine beliebige Stelle, z.B. auf einen USB-Festplatte.

Da nach dem verschieben das Projektverzeichnis nicht mehr an seiner alten Stelle existiert, wird das Programm beim nächsten Start eine Fehlermeldung ausgeben. Die Frage, ob ein neues Projekt erzeugt werden soll, beantwortet mit **"Ja"**. 

Darauf öffnet sich der [Projektassistent](#usage_general_projects_wizard). Klicken Sie im Projektassistenten auf den Tab **"Projekt öffnen"** und wählen das Projekt-Verzeichnis an seiner neuen Position aus und klicken auf **"Projekt öffnen"**. Dann wird das Projekt vom neuen Speicherort im Programm geöffnet. 

Beim nächsten Programmstart wird das Projekt automatisch vom neuen Speicherort geöffnet, wenn Sie zuvor im Projektassistenten die Checkbox **"Das Projekt automatisch beim Programmstart öffnen"** aktiviert haben.
