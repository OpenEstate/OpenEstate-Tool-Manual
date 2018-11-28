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

Im ImmoTool können mehrere Projekte parallel verwaltet werden. Jedes verwaltete Projekt besitzt eine eigenständige Datenbank und wird in separaten Verzeichnissen auf der Festplatte abgespeichert.

Abhängig vom Anwendungsfall kann es sinnvoll sein, die Immobilien nach Tätigkeit (Makler und / oder Vermittler) oder nach Kunden in getrennten Projekten zu verwalten. In diesen Fällen können mehrere Projekte parallel, z.B. ein Projekt als Verwalter und eines als Makler, eingerichtet werden.

Mindestens ein Projekt muss angelegt werden, um mit dem Programm arbeiten zu können.


### Der Projektassistent {#usage_general_projects_wizard}

Der Projektassistent hilft Ihnen bei der Erstellung eines neuen Projektes.

**Erster Start**

Beim ersten Start des Programmes öffnet sich der Projektassistent, und Sie werden aufgefordert ein Projekt anzulegen.

**Ein neues Projekt erzeugen**

Wenn Sie die Angaben in allen Karteireitern vorgenommen haben, speichern Sie Ihr Projekt mit dem Button Projekt erzeugen. Das erzeugte Projekt wird daraufhin automatisch geöffnet.

**Folgende Starts**

Bei folgenden Starts wird das zuletzt verwendete Projekt automatisch geladen.


### Ein neues Projekt erzeugen {#usage_general_projects_create}

**Projektdaten bearbeiten**

**Projekt-Name**

Tragen Sie hier den Namen Ihres Projektes ein. Verwenden Sie möglichst keine Umlaute oder Sonderzeichen.

**Verzeichnis**

Es ist standardmäßig ein Pfad voreingestellt. Diesen können Sie im Regelfall einfach beibehalten. Bei Bedarf kann ein anderer Pfad gewählt werden, z.B. eine externe Datenquelle in Ihrem System.

**Lizenz bestätigen**

Bitte bestätigen Sie die Nutzungslizenz des ImmoTools, bevor Sie Ihr Projekt erzeugen.

{{< figure src="projects_wizard_general.jpg" caption="Projekt-Asssistent / Eigenschaften des Projekts" >}}

**Firmendaten bearbeiten**

Tragen Sie hier Ihre Unternehmensdaten ein. Die installierten Add-Ons greifen an verschiedenen Stellen auf diese Eingaben zurück. Farblich hinterlegte Felder sind Pflichtangaben.

{{< figure src="projects_wizard_company.jpg" caption="Projekt-Asssistent / Firmendaten des Projekts" >}}

**Add-Ons auswählen**

{{< figure src="projects_wizard_addons.jpg" caption="Projekt-Asssistent / Aktivierte Addons" >}}

Hier befindet sich die Übersicht der aktuell verfügbaren Add-Ons. Standardmäßig sind alle bei der Installation verfügbare Add-Ons aktiviert. Deaktivieren Sie die Add-Ons, welche Sie nicht in Ihrem Projekt verwenden möchten.

> **Hinweis**
>
> Eine nachträgliche Änderung dieser Einstellungen ist jederzeit möglich, siehe Add-Ons / Module.

**Das neue Projekt speichern & öffnen**

Speichern Sie das neu angelegte Projekt mit dem Button Projekt erzeugen.


### Ein bereits existierendes Projekt öffnen {#usage_general_projects_open}

> **TODO**
>
> Inhalte einfügen


### Das zuletzt verwendete Projekt öffnen {#usage_general_projects_recent}

> **TODO**
>
> Inhalte einfügen


### Fragen & Antworten zu Projekten {#usage_general_projects_faq}


#### Wo wird mein Projekt gespeichert? {#usage_general_projects_faq_location}

Der Speicherort des Projektes kann im Projektassistenten gewählt werden (siehe Projektdaten bearbeiten). Wenn nichts Anderes eingestellt wurde, wird das Projekt im Unterordner `projects` des Programmverzeichnisses abgelegt.

Wenn das Programm z.B. in Windows unter `C:\Programme\OpenEstate-ImmoTool` installiert ist, wird ein Projekt mit dem Namen test standardmäßig im Ordner `C:\Programme\OpenEstate-ImmoTool\projects\test` abgelegt.


#### Wie kann ich mein Projekt an eine andere Stelle verschieben? {#usage_general_projects_faq_move}

Verschieben (oder kopieren) Sie das Projektverzeichnis mit dem Betriebssystem (z.B. Windows Explorer) an eine andere Stelle (z.B. auf einen USB-Stick).

Wenn das alte Projektverzeichnis nicht mehr existiert, sollte das Programm beim nächsten Start einen Fehler feststellen. Die Frage, ob ein neues Projekt erzeugt werden soll, kann mit `Ja` beantwortet werden. Darauf öffnet sich der [Projektassistent](#usage_general_projects_wizard).

Klicken Sie im Projektassistenten unten rechts auf `Projekt öffnen` und wählen Sie das Projekt-Verzeichnis aus (z.B. auf dem USB-Stick). Damit wird das Projekt vom neuen Speicherort im Programm geöffnet.

Beim nächsten Programmstart wird das Projekt dann automatisch vom neuen Speicherort geöffnet.

