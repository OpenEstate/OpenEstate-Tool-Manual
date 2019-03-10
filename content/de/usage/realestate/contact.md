---

title: Ansprechpartner verwalten
linktitle: Ansprechpartner
description: Hinweise zur Verwaltung von Ansprechpartnern in OpenEstate-ImmoTool…
weight: 30

menu:
  main:
    parent: usage-realestate
    identifier: usage-realestate-contact

---

## Ansprechpartner verwalten {#usage_realestate_contact}

Ansprechpartner sind Kontaktdaten (in der Regel die Daten Ihrer Mitarbeiter), die gemeinsam mit einer Immobilie veröffentlicht werden. Zum Beispiel beim Inserieren auf einem Immobilienportal wird dem Interessenten der Ansprechpartner gemeinsam mit der Immobilie präsentiert. Im Falle einer Kontaktaufnahme zu einer Immobilie wird der jeweils zugewiesene Ansprechpartner vom Interessenten kontaktiert.


### Übersicht der Ansprechpartner {#usage_realestate_contact_table}

Innerhalb eines Projektes können beliebig viele Ansprechpartner verwaltet werden. Die Übersicht der gespeicherten Ansprechpartner kann auf zweierlei Wegen geöffnet werden:

-   Klicken Sie im Hauptmenü auf den Eintrag **"Immobilien → Ansprechpartner anzeigen"** um die Übersicht der Immobilien zu öffnen.

    {{< figure src="menu.png" caption="Übersicht der Immobilien über das Hauptmenü öffnen" >}}

-   Öffnen Sie die Immobilien-Ansicht und klicken in der Sidebar auf den Eintrag **"Ansprechpartner"**.

    {{< figure src="sidebar.png" caption="Übersicht der Immobilien über die Sidebar öffnen" >}}


Daraufhin wird eine tabellarische Übersicht der erfassten Ansprechpartner dargestellt:

{{< figure src="contact_table.png" caption="Übersicht der Ansprechpartner" >}}


#### Filterkriterien verwenden {#usage_realestate_contact_table_filter}

Oberhalb der Tabelle werden verschiedene Eingabefelder dargestellt, um den Bestand der Ansprechpartner eingrenzen zu können. Die Ansicht der Tabelle wird automatisch aktualisiert sobald ein Kriterium geändert wurde.


#### Aktionen ausführen {#usage_realestate_contact_table_actions}

Markieren Sie in der Tabelle einen oder mehrere Ansprechpartner. Klicken Sie danach auf den Button **"Aktionen"** oder mit der rechten Maustaste in die Tabelle um das Aktionsmenü darzustellen.

{{< figure src="contact_table_actions.png" caption="Aktionsmenü in der Übersicht der Ansprechpartner" >}}

Folgende Aktionen stehen zur Verfügung:

-   **Ansprechpartner öffnen.**

    Wählen Sie diese Aktion, um den markierten Ansprechpartner zur Bearbeitung zu öffnen.

-   **Ansprechpartner löschen.**

    Wählen Sie diese Aktion, um die markierten Ansprechpartner dauerhaft aus der Datenbank zu löschen.

{{< info >}}
Wenn mehrere Zeilen in der Tabelle markiert wurden (z.B. mit gedrückter STRG- / Shift-Taste), können Aktionen auf mehreren Ansprechpartnern durchgeführt werden.
{{< /info >}}


### Ansprechpartner erstellen {#usage_realestate_contact_add}

Klicken Sie im Hauptmenü auf **"Immobilien → Neuer Eintrag → Neuer Ansprechpartner"**. Alternativ können Sie die [Übersicht der Ansprechpartner](#usage_realestate_contact_table) öffnen und oben rechts auf den Button **"Neu"** klicken.

Nehmen Sie die gewünschten Einträge im [Formular für Ansprechpartner](#usage_realestate_contact_form) vor und klicken Sie abschließend auf den Button **"Speichern"**.


### Ansprechpartner bearbeiten {#usage_realestate_contact_edit}

Öffnen Sie die [Übersicht der Ansprechpartner](#usage_realestate_contact_table) und suchen Sie den zu bearbeitenden Ansprechpartner in der Tabelle. Durch einen Doppelklick auf den betreffenden Ansprechpartner wird das [Formular für Ansprechpartner](#usage_realestate_contact_form) zur Bearbeitung des Ansprechpartners geöffnet. Alternative können Sie den Ansprechpartner in der Tabelle mit der rechten Maustaste markieren und im erscheinenden Menü "**Ansprechpartner bearbeiten**" wählen.

Nehmen Sie die gewünschten Änderungen im [Formular für Ansprechpartner](#usage_realestate_contact_form) vor und klicken Sie abschließend auf den Button **"Speichern"**.


### Ansprechpartner löschen {#usage_realestate_contact_remove}

Öffnen Sie die [Übersicht der Ansprechpartner](#usage_realestate_contact_table) und suchen Sie den zu löschenden Ansprechpartner in der Tabelle. Klicken Sie mit der rechten Maustaste auf den betreffenden Ansprechpartner und wählen Sie im dargestellten Menü die Aktion **"Ansprechpartner löschen"**. Alternative können Sie den Ansprechpartner in der Tabelle mit der rechten Maustaste markieren und im erscheinenden Menü **"Entfernen"** wählen.


### Formular für Ansprechpartner {#usage_realestate_contact_form}


#### Personendaten {#usage_realestate_contact_form_person}

Im Tab **"Person"** können die allgemeinen Kontaktdaten des Ansprechpartners hinterlegt werden.

{{< figure src="contact_form.png" caption="Personendaten des Ansprechpartners" >}}


#### Betreute Immobilien {#usage_realestate_contact_form_realestate}

Im Tab **"Immobilien"** finden Sie eine tabellarische Übersicht aller Immobilien, die aktuell vom gewählten Ansprechpartner betreut werden. Die Verknüpfung einer Immobilie zu einem Ansprechpartner erfolgt im Immobilienformular unter **"Adressen → Ansprechpartner"**.

{{< figure src="contact_form_realestates.png" caption="Betreute Immobilien des Ansprechpartners" >}}


#### Notizen {#usage_realestate_contact_form_notes}

Im Tab **"Notizen"** kann zu dem Ansprechpartner ein beliebiger Notiztext hinterlegt werden. Dieser Text wird an keiner Stelle veröffentlicht.

{{< figure src="contact_form_notes.png" caption="Notizen zum Ansprechpartner" >}}



#### Änderungen speichern {#usage_realestate_contact_form_submit}

Um die Änderungen im Formular für Ansprechpartner dauerhaft zu speichern, klicken Sie oben rechts auf den Button **"Speichern"**.

{{< info >}}
Das Speichern ist zu jedem Zeitpunkt der Bearbeitung möglich. Sollten relevante Eingaben fehlen, so weist das Programm darauf hin.
{{< /info >}}

{{< warning >}}
Jede Änderung im Formular muss abschließend durch Klick auf **"Speichern"** dauerhaft gespeichert werden.
{{< /warning >}}

