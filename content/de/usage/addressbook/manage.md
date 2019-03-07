---

title: Verwendung des Adressbuch Add-Ons
linktitle: Verwaltung
description: Allgemeine Hinweise zur Verwendung des Adressbuch Add-Ons von OpenEstate-ImmoTool…
weight: 20

menu:
  main:
    parent: usage-addressbook
    identifier: usage-addressbook-manage

---

## Adressen verwalten {#usage_addressbook_manage}


### Übersicht der Adressen {#usage_addressbook_manage_table}

Innerhalb eines Projektes können beliebig viele Adressen gespeichert werden. Zur Verwaltung der hinterlegten Adressen gelangen Sie auf zweierlei Wegen:

-   Klicken Sie im Hauptmenü auf den Eintrag **"Adressbuch → Adressen"** um die Übersicht der Adressen zu öffnen.
-   Klicken Sie in der Sidebar **"Adressbuch"** auf den Eintrag **"Adressen"**.

Daraufhin wird eine tabellarische Übersicht der erfassten Adressen dargestellt:

{{< figure src="address_table.jpg" caption="Übersicht der Adressen" >}}


#### Filterkriterien verwenden {#usage_addressbook_manage_table_filter}

Oberhalb der Tabelle werden verschiedene Eingabefelder dargestellt, um die dargestellten Adressen eingrenzen zu können. Die Ansicht der Tabelle wird automatisch aktualisiert sobald ein Kriterium geändert wurde.


#### Aktionen ausführen {#usage_addressbook_manage_table_actions}

Markieren Sie in der Tabelle eine oder mehrere Adressen. Klicken Sie danach auf den Button **"Aktionen"** oder mit der rechten Maustaste in die Tabelle um das Aktionsmenü darzustellen.

{{< todo >}}
Screenshot & Inhalte einfügen
{{< /todo >}}

{{< tip >}}
Wenn mehrere Zeilen in der Tabelle markiert wurden (z.B. mit gedrückter STRG- / Shift-Taste), können Aktionen auf mehreren Adressen durchgeführt werden.
{{< /tip >}}


### Adresse erfassen {#usage_addressbook_manage_add}

Klicken Sie im Hauptmenü auf **"Adressen → Neu → Adresse"**. Alternativ können Sie die [Übersicht der Adressen](#usage_addressbook_manage_table) öffnen und oben rechts auf den Button **"Neu"** klicken.

Nehmen Sie die gewünschten Einträge im [Adressformular](#usage_addressbook_manage_form) vor und klicken Sie abschließend auf den Button **"Speichern"**.


### Adresse bearbeiten {#usage_addressbook_manage_edit}

Öffnen Sie die [Übersicht der Adressen](#usage_addressbook_manage_table) und suchen Sie die zu bearbeitende Adresse in der Tabelle. Durch einen Doppelklick auf die betreffende Adresse wird das [Adressformular](#usage_addressbook_manage_form) zur Bearbeitung der Adresse geöffnet.

Nehmen Sie die gewünschten Änderungen im [Adressformular](#usage_addressbook_manage_form) vor und klicken Sie abschließend auf den Button **"Speichern"**.


### Adresse duplizieren {#usage_addressbook_manage_copy}

Öffnen Sie die [Übersicht der Adressen](#usage_addressbook_manage_table) und suchen Sie die zu duplizierende Adresse in der Tabelle. Klicken Sie mit der rechten Maustaste auf die betreffende Adresse und wählen Sie im dargestellten Menü die Aktion **"Adresse duplizieren"**.

{{< info >}}
Die originale Adresse bleibt bei dieser Verfahrensweise unangetastet!
{{< /info >}}


### Adresse löschen {#usage_addressbook_manage_remove}

Öffnen Sie die [Übersicht der Adressen](#usage_addressbook_manage_table) und suchen Sie die zu löschende Adresse in der Tabelle. Klicken Sie mit der rechten Maustaste auf die betreffende Adresse und wählen Sie im dargestellten Menü die Aktion **"Adresse löschen"**.

{{< warning >}}
Eine Löschung kann ohne vorherige Datensicherung nicht wieder rückgängig gemacht werden!
{{< /warning >}}


### Adressformular {#usage_addressbook_manage_form}

Im Adressformular können die Details zu einer Adresse eingesehen und ggf. bearbeitet werden.

{{< figure src="address_form_general.jpg" caption="Adressformular" >}}


#### Eckdaten {#usage_addressbook_manage_form_general}

Im Tab **"Allgemein"** werden allgemeinen Eckdaten einer Adresse zusammengefasst.

-   Weisen Sie der Adresse eine Adressgruppe zu.
-   Füllen Sie die weiteren Eingabefelder nach Bedarf aus.


#### Details {#usage_addressbook_manage_form_details}

Im Tab **"Details"** können weitere Angaben wie z.B. Bankverbindung eingesehen / erfasst werden.


#### Verknüpfte Immobilien {#usage_addressbook_manage_form_realestate}

Im Tab **"Immobilien"** können die mit der Adresse verknüpften Immobilien eingesehen / erfasst werden. Allgemein kann jede Adresse mit einer oder mehreren Immobilien verknüpft werden.

Klicken Sie auf **"Neu"** um eine neue Verknüpfung zu erfassen oder öffnen Sie eine bestehende Verknüpfung per Doppelklick in die Tabelle. Es öffnet sich daraufhin das folgende Fenster:

{{< figure src="address_assign_realestate.jpg" caption="Verknüpfung einer Immobilie mit einer Adresse" >}}

Wählen Sie in der Auswahlbox **"Immobilie"** eine zu verknüpfende Immobilie aus. Unter **"Zuordnung"** geben Sie ggf. an, ob es sich bei dieser Adresse um einen Eigentümer / Interessent / Käufer / Mieter handelt. Klicken Sie abschließend auf **"Übernehmen"** um die bearbeite Verknüpfung ins Adressformular zu übernehmen.

Um eine Verknüpfung mit einer Immobilie zu löschen, markieren Sie die entsprechende Immobilie mit der Maus. Klicken Sie mit der rechten Maustaste oder klicken Sie auf den Button **"Aktionen"** und wählen Sie die Aktion **"Zuordnung löschen"** aus.


#### Verknüpfte Kalendereinträge {#usage_addressbook_manage_form_calendar}

Im Tab **"Kalender"** können die mit der Adresse verknüpften Kalendereinträge (Aufgaben oder Termine) eingesehen / erfasst werden. Allgemein kann jede Adresse kann mit einem oder mehreren Kalender-Einträgen verknüpft werden.

Klicken Sie auf **"Neu"** um eine neue Verknüpfung zu erfassen oder öffnen Sie eine bestehende Verknüpfung per Doppelklick in die Tabelle. Es öffnet sich daraufhin das folgende Fenster:

{{< figure src="address_assign_calendar.jpg" caption="Verknüpfung einer Immobilie mit einem Kalendereintrag" >}}

Wählen Sie die **"Gruppe"** und den **"Eintrag"** des zu verknüpfenden Kalender-Eintrags aus. Klicken Sie abschließend auf **"Übernehmen"** um die bearbeite Verknüpfung ins Adressformular zu übernehmen.

Um eine Verknüpfung zu einem Kalendereintrag zu löschen, markieren Sie den entsprechenden Kalendereintrag mit der Maus. Klicken Sie mit der rechten Maustaste oder klicken Sie auf den Button **"Aktionen"** und wählen Sie die Aktion **"Zuordnung löschen"** aus.


#### Notizen {#usage_addressbook_manage_form_notes}

Im Tab **"Notizen"** kann zu der Adresse ein beliebiger Notiztext hinterlegt werden.


#### Änderungen speichern {#usage_addressbook_manage_form_submit}

Um die Änderungen im Formular dauerhaft zu speichern, klicken Sie oben rechts auf den Button **"Speichern"**.

{{< info >}}
Das Speichern ist zu jedem Zeitpunkt der Bearbeitung möglich. Sollten relevante Eingaben fehlen, so weist das Programm darauf hin.
{{< /info >}}

{{< warning >}}
Jede Änderung im Formular muss abschließend durch Klick auf **"Speichern"** dauerhaft gespeichert werden.
{{< /warning >}}


### Was sind Adressgruppen? {#usage_addressbook_manage_groups_info}

Adressgruppen ermöglichen die thematische Zusammenfassung von verschiedenen Adressen. Grundsätzlich wird jede Adresse exakt einer Adressgruppe zugeordnet.

Mit der Installation des Programms werden die Adressgruppen **privat** und **geschäftlich** in das Programm integriert. Bei Bedarf können diese Gruppen entfernt oder umbenannt werden - bzw. es können weitere Adressgruppen erfasst werden.

Die aktuell im Programm erfassten Adressgruppen werden in der Sidebar dargestellt:

{{< figure src="group_table.jpg" caption="Übersicht der Adressgruppen" >}}

{{< todo >}}
Screenshot aktualisieren
{{< /todo >}}


### Adressgruppe erfassen {#usage_addressbook_manage_groups_add}

Klicken Sie im Hauptmenü auf **"Adressen → Neu → Adressgruppe"**.

Nehmen Sie die gewünschten Einträge im [Formular für Adressgruppen](#usage_addressbook_manage_groups_form) vor und klicken Sie abschließend auf den Button **"Speichern"**.


### Adressgruppe bearbeiten {#usage_addressbook_manage_groups_edit}

Öffnen Sie die Adressbuch-Ansicht in der Sidebar, klicken Sie mit der rechten Maustaste auf die zu bearbeitende Adressgruppe und wählen Sie im Menü die Aktion **"Adressgruppe bearbeiten"**.

Nehmen Sie die gewünschten Einträge im [Formular für Adressgruppen](#usage_addressbook_manage_groups_form) vor und klicken Sie abschließend auf den Button **"Speichern"**.


### Adressgruppe löschen {#usage_addressbook_manage_groups_remove}

Öffnen Sie die Adressbuch-Ansicht in der Sidebar, klicken Sie mit der rechten Maustaste auf die zu löschende Adressgruppe und wählen Sie im Menü die Aktion **"Adressgruppe löschen"**.

{{< warning >}}
Eine Löschung kann ohne vorherige Datensicherung nicht wieder rückgängig gemacht werden!
{{< /warning >}}


### Formular für Adressgruppen {#usage_addressbook_manage_groups_form}

Im Formular für Adressgruppen können die Details zu einer Adressgruppe eingesehen und ggf. bearbeitet werden.

{{< todo >}}
Screenshot einfügen
{{< /todo >}}


#### Eckdaten {#usage_addressbook_manage_groups_form_general}

Tragen Sie eine Bezeichnung für die Adressgruppe und ggf. einen Beschreibungstext ein.


#### Änderungen speichern {#usage_addressbook_manage_groups_form_submit}

Um die Änderungen im Formular dauerhaft zu speichern, klicken Sie auf den Button **"Speichern"**.
