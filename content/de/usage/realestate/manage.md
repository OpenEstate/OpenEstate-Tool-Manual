---

title: Verwendung des Immobilien Add-Ons
linktitle: Verwaltung
description: Allgemeine Hinweise zur Verwendung des Immobilien Add-Ons von OpenEstate-ImmoTool…
weight: 20

menu:
  main:
    parent: usage-realestate
    identifier: usage-realestate-manage

---

## Immobilien verwalten {#usage_realestate_manage}


### Übersicht der Immobilien {#usage_realestate_manage_table}

Innerhalb eines Projektes können beliebig viele Immobilien verwaltet werden. Die Übersicht der gespeicherten Immobilien kann auf zweierlei Wegen geöffnet werden:

1.  Klicken Sie im Hauptmenü auf den Eintrag `Immobilien` → `Immobilienansicht öffnen` um die Übersicht der Immobilien zu öffnen.

    {{< figure src="menu.jpg" caption="Übersicht der Immobilien über das Hauptmenü öffnen" >}}

2.  Öffnen Sie die Immobilien-Ansicht und klicken Sie in der Sidebar auf den Eintrag `Immobilien`.

    {{< figure src="sidebar.jpg" caption="Übersicht der Immobilien über die Sidebar öffnen" >}}


Daraufhin wird eine tabellarische Übersicht der erfassten Immobilien dargestellt:

{{< figure src="realestate_table.jpg" caption="Übersicht der Immobilien" >}}


#### Filterkriterien verwenden {#usage_realestate_manage_table_filter}

Oberhalb der Tabelle werden verschiedene Eingabefelder dargestellt, um den Immobilienbestand eingrenzen zu können. Die Ansicht der Tabelle wird automatisch aktualisiert sobald ein Kriterium geändert wurde.

Unter Adresse können Sie entweder eine Postleitzahl oder einen Ort eintragen.


#### Aktionen ausführen {#usage_realestate_manage_table_actions}

Markieren Sie in der Tabelle eine oder mehrere Immobilien. Klicken Sie danach auf den Button `Aktionen` oder mit der rechten Maustaste in die Tabelle um das Aktionsmenü darzustellen.

{{< figure src="realestate_table_actions.jpg" caption="Aktionsmenü in der Übersicht der Immobilien" >}}

Folgende Aktionen stehen zur Verfügung:

-   **Immobilie öffnen**

    Wählen Sie diese Aktion, um die markierte(n) Immobilie(n) zur Bearbeitung zu öffnen.

-   **Status ändern**

    Ändern Sie den Status der markierte(n) Immobilie(n), ohne das Immobilienformular dafür öffnen zu müssen.

-   **Immobilie duplizieren**

    Wählen Sie diese Aktion, um eine Kopie der markierte(n) Immobilie(n) zu erzeugen.

-   **Entfernen**

    Wählen Sie diese Aktion, um die markierte(n) Immobilie(n) dauerhaft aus der Datenbank zu löschen.

-   **Exposé erzeugen**

    Erzeugen Sie ein Exposé im PDF-Format für die markierte(n) Immobilien.

-   **Ansprechpartner zuweisen**

    Ändern Sie den Ansprechpartner der markierte(n) Immobilie(n), ohne das Immobilienformular dafür öffnen zu müssen.

-   **Speichern unter**

    Speichern Sie die markierten Immobilien als CSV- oder Excel-Datei auf der Festplatte.

-   **Vermittlung öffnen**

    > **TODO**
    >
    > Aktion Vermittlung öffnen beschreiben


> **Tipp**
>
> Wenn mehrere Zeilen in der Tabelle markiert wurden (z.B. mit gedrückter STRG- / Shift-Taste und der linken Maustaste), können Aktionen auf mehreren Immobilien auf einmal durchgeführt werden.


#### Immobilien durchsuchen {#usage_realestate_manage_table_search}

Hierbei handelt es sich nicht um Suchaufträge eines Interessenten, sondern um eine frei definierbare Suche im Immobilienbestand um z.B. häufig gesuchte Immobilien schnell zu finden.

Alle bereits gespeicherten und aktiven Suchanfragen werden in der Selectbox Suche oder in der Sidebar dargestellt. Wählen Sie eine der Suchanfragen aus, um die Suche auf dem Immobilienbestand durchzuführen.

Um eine neue Suchanfrage zu erzeugen, klicken Sie auf den Button mit der Lupe neben der Selectbox für die Suchanfragen. Es öffnet sich daraufhin ein Dialogfenster zur Erstellung einer Suchanfrage.

{{< figure src="realestate_search.jpg" caption="Aktionsmenü in der Immobilienbestand durchsuchen" >}}

Folgende Angaben können im Formular hinterlegt werden:

-   **Name**
    Wenn die Suchanfrage dauerhaft gespeichert werden soll, wählen Sie eine möglichst passende Bezeichnung um diese später leicht wieder erkennen zu können.

-   **Vorlage wählen**

    > **TODO**
    >
    > Vorlage wählen beschreiben

-   **Suchanfrage dauerhaft speichern**

    Aktivieren Sie diese Option, wenn die Suchanfrage dauerhaft gespeichert werden soll. Andernfalls wird die Suchanfrage einmal ausgeführt und verworfen.

-   **Suchkriterien bearbeiten**

    Wählen Sie eines oder mehrere Kriterien zur Immobiliensuche aus.
    
-   **Suchkriterien hinzufügen**

    Betätigen Sie den Button `Kriterium hinzufügen` um weiteren Kriterien für die Suche zu definieren. Es erscheint dann ein weiteres Feld mit der Bezeichnung `Kriterium wählen. Wenn Sie dieses Feld markieren werden Ihnen weitere Kriterien zu Auswahl gestellt.
    
Durch betätigen eines roten Kreuzes können Sie ein Kriterium abwählen - es wird immer der letzte Eintrag dieses Kriterium gelöscht - und mit dem grünen Minus einem Kriterium einen weiteren Wert hinzufügen.

Klicken Sie abschließend auf `Übernehmen` um die Suchanfrage auf dem Immobilienbestand auszuführen. Das Resultat der Suche wird in der Übersicht der Immobilien dargestellt.


### Immobilie erfassen {#usage_realestate_manage_add}

Das Formular zum Anlegen einer Immobilie können Sie auf folgenden Wegen öffnen.

1. Klicken Sie im Hauptmenü auf `Immobilien` → `Neuer Eintrag` → `neue Immobilie`.

2. Klicken Sie in der Sidebar mit der rechten Maustaste auf Immobilien und wählen `Immobilien` → `Neuer Eintrag` → `neue Immobilie`.

3. Klicken Sie im Kopfbereich der Übersicht der Immobilien auf den Button mit dem grünen Kreuz `Neu`.

Nehmen Sie die gewünschten Einträge im [Immobilienformular](#usage_realestate_manage_form) vor und klicken Sie abschließend auf den Button `Speichern`.


### Immobilie bearbeiten {#usage_realestate_manage_edit}

Öffnen Sie die [Übersicht der Immobilien](#usage_realestate_manage_table) und suchen Sie die zu bearbeitende Immobilie in der Tabelle.

Eine Immobilie können Sie auf drei Wegen öffnen.

1. Durch einen Doppelklick auf die betreffende Immobilie wird das [Immobilienformular](#usage_realestate_manage_form) zur Bearbeitung der Immobilie geöffnet.

2. Markieren Sie die Immobilie in der Liste und klicken mit der rechten Maustaste auf diese. im dargestellten Menü wählen Sie `Immobilie öffnen`.

3. Markieren Sie die Immobilie in der Liste und betätigen Sie die Enter-Taste.

Nehmen Sie die gewünschten Änderungen im [Immobilienformular](#usage_realestate_manage_form) vor und klicken Sie abschließend auf den Button `Speichern`.


### Immobilie duplizieren {#usage_realestate_manage_copy}

Öffnen Sie die [Übersicht der Immobilien](#usage_realestate_manage_table) und suchen Sie die zu duplizierende Immobilie in der Tabelle.

Eine Immobilie können Sie auf zwei Wegen öffnen.

1. Klicken Sie mit der rechten Maustaste auf die betreffende Immobilie und wählen Sie im dargestellten Menü die Aktion `Immobilie duplizieren`.

2. Klicken Sie im oberen Bereich der Übersicht der Immobilien auf `Anktionen → Immobilie duplizieren`.

> **Hinweis**
>
> Die originale Immobilie bleibt bei dieser Verfahrensweise unangetastet!

Nehmen Sie an der duplizierten Immobilie die gewünschten Änderungen vor und speichern diese. Es wird eine neue Immobilie in der Datenbank angelegt.


### Immobilie löschen {#usage_realestate_manage_remove}

Öffnen Sie die [Übersicht der Immobilien](#usage_realestate_manage_table) und suchen Sie die zu löschende Immobilie in der Tabelle.

Eine Immobilie können Sie auf zwei Wegen löschen.

1. Klicken Sie mit der rechten Maustaste auf die betreffende Immobilie und wählen Sie im dargestellten Menü die Aktion `Entfernen`.

2. Klicken Sie im oberen Bereich der Übersicht der Immobilien auf `Anktionen → Entfernen`.


> **Achtung**
>
> Eine Löschung kann ohne vorherige Datensicherung nicht wieder rückgängig gemacht werden!


### Immobilienformular {#usage_realestate_manage_form}

#### Eckdaten {#usage_realestate_manage_form_general}

Im Tab `Allgemein` werden allgemeinen Eckdaten einer Immobilie zusammengefasst.

{{< figure src="realestate_form.jpg" caption="Immobilienformular mit Eckdaten" >}}

-   **Titel**
    Hinterlegen Sie einen aussagekräftigen und nicht zu langen Titel für diese Immobilie.

    Der Titel wird in allen Sprachen angezeigt, welche in den Sprach-Einstellungen aktiviert wurden. Durch einen Mausklick auf die Checkbox neben der Landesflagge können Sie für diese Immobilie eine oder mehrere Sprachen aktivieren. Eine Sprache muss mindestens aktiviert werden.

    > **Hinweis**
    >
    > Der Titel kann in allen Sprachen abgelegt werden, welche in den Sprach-Einstellungen aktiviert wurden. Hauptmenü `Extras` → `Einstellungen` → `Immobilien` → `Sprachen`

-   **Objekt-Nr**
    Dieses Feld ist für von Ihnen selbst vergebene interne Objektnummer vorgesehen. Von Portalen kann die Objekt-Nr zur Identifikation Ihrer Inserate verwendet werden.

    > **Tipp**
    >
    > Wenn Sie wünschen, dass die Objektnummer statt der Datenbank-ID für den Export zu den Portalen verwendet wird, nehmen Sie in der Schnittstelle die entsprechende Einstellung vor.


-   **Währung**
    EUR ist voreingestellt, und sollte nur geändert werden, wenn Schnittstellen zu Portalen mit anderen Währungen verfügbar sind.

-   **Objekt-ID**
    Die Objekt-ID wird beim Speichern von System vergeben, und dient internen Zwecken. Diese kann von Ihnen nicht geändert werden.

-   **Import-ID**
    Die Import-ID wird ggf. beim Import von Immobilien automatisch vergeben und kann von Ihnen nicht geändert werden.

-   **Status**
    Wählen Sie einen Status für diese Immobilie.

-   **Gültig von / Gültig bis**
    Wählen Sie ggf. je ein Datum für den Beginn und das Ende des Zeitraums der Vermittlung dieser Immobilie.

-   **Gruppennummer**
    Vergeben Sie ggf. eine Gruppennummer damit diese Immobilie mit anderen Immobilien des Bestands z.B. bei ImmobilienScout24 gruppiert dargestellt wird.

-   **Adresseingabe**
    Geben Sie hier die Adresse der Immobilie ein und wählen ein Land.
    
    Manche Portale, wie z.B. Immobiliare.it und ImmobilienScout24, benötigen spezifische regionale Angaben für Immobilien. Wenn Sie ein solches Portal beliefern, wählen Sie in der Selectbox `Immobilien-Adresse` das jeweilige Portal und ordnen Sie es der entsprechenden Region zu bis keine weitere Zuordnung in den Unter-Regionen mehr möglich ist.

-   **Geokoordinaten**
    Geben Sie die Geokoordinaten der Immobilie ein, falls diese Ihnen bekannt sein sollten.

-   **Geokoordinaten ermitteln**
    Um die Geokoordinaten zu einer Immobilie zu ermitteln betätigen Sie den Button `Geokoordinaten ermitteln`. Im folgenden Fenster können Sie nach betätigen des Buttons `Suchen` angeben ob Sie nach einem Ort oder einer Postleitzahl suchen. Gemäß Ihrer Auswahl öffnet sich in der Karte das entsprechende Suchformular. Geben Sie Suchkriterien ein und starten Sie die Suche über den Button `Ausführen`. Mit dem Button `Abbrechen` im Suchformular können Sie das Suchformular schließen. Im Suchergebnis wählen Sie ein passendes Ergebnis. Es wird Ihnen dann ein Ausschnitt einer Karte gezeigt. Diesen können Sie mit dem Mausrad vergrößern oder verkleinern und mit der linken Maustaste verschieben. Wenn Sie die gewünschte Adresse gefunden haben markieren Sie diese und betätigen den Button `Koordinaten übernehmen`. Die Koordinaten werden in das Immobilienformular übernommen.

> **Hinweis**
>
> Nach dem Versand der Immobilie an Portale sollten Sie die Objekt-Nr nicht mehr ändern, da dieses Inserat sonst in den Portalen ggf. neu angelegt wird, und dann doppelt vorhanden sein kann. Sollte eine neue Vergabe der Nummer notwendig sein, so löschen Sie diese Immobilie zuerst in den Portalen.

> **Hinweis**
>
> Der Status einer Immobilie muss auf `in Vermittlung` gesetzt sein damit die Immobilie beim Export zu den Immobilienportalen berücksichtigt wird.

> **Hinweis**
>
> Um die spezifischen Regionen eines Immobilienportals verfügbar zu haben, müssen die jeweiligen Erweiterung in die Datenbank installiert werden. Diese finden Sie unter [dev.openestate.org](http://dev.openestate.org/applications/1/#download) im Abschnitt **Geodaten**.


> **TODO**
>
> Link zum Download der Geodaten korrigieren



#### Spezifikation {#usage_realestate_manage_form_attributes}

Im Tab `Immobilie` werden spezifische Eigenschaften der Immobilie zusammengefasst.

1.  Spezifizieren Sie zuerst die Immobilienart so genau wie es ihnen möglich ist - z.B. `Wohnimmobilie` → `Wohnung` → `Erdgeschosswohnung`.

    {{< figure src="realestate_form_type.jpg" caption="Auswahl der Immobilienart" >}}

2.  Wählen Sie danach die passende Vermarktungsart - z.B. `Miete`

3.  Nach der Eingabe dieser Informationen werden weitere Eigenschaften / Attribute zu dieser Auswahl in der unteren Tabelle dargestellt.

    {{< figure src="realestate_form_attributes.jpg" caption="Attribute zur Immobilie erfassen" >}}

4.  Tragen Sie die ihnen bekannten Daten in die Tabelle ein. Klicken Sie für die Eingabe auf das jeweilige Feld in der Spalte Wert.

    -   Bei Eingaben der Art Länge und Fläche können Sie rechts in diesem Feld mit den Pfeiltasten die Einheit wählen.

        {{< figure src="realestate_form_attributes_unit.jpg" caption="Einheit eines Flächen-Attributs ändern" >}}
    
    -   In Feldern zur Eingabe eines Datums muss das Datum im Format `TT.MM.JJJJ` eingetragen werden.
    
    -   Bei Feldern mit mehrfacher Auswahl öffnet sich nach dem Anklicken des Feldes eine Liste, in welcher Sie Angaben wählen und abwählen können.

        {{< figure src="realestate_form_attributes_multiple.jpg" caption="Attribute mit mehreren Optionen" >}}

    -   Bei Feldern mit einfacher Auswahl wird nur eine Angabe übernommen. Wird ein Zweite aktiviert wird die Erste deaktiviert.
    
5.  Attribute mit freier Texteingabe befinden sich unter den Tabs mit den Landesflaggen.


#### Beschreibungstext {#usage_realestate_manage_form_descriptions}

Nachdem eine Immobilien- & Vermarktungsart gewählt wurde können zusätzliche beschreibende Texte zur Immobilie hinterlegt werden.

Wählen Sie dafür die Tabs mit den Landesflaggen und füllen die gewünschten Felder mit den entsprechenden Inhalten aus.

Mit den blauen Pfeilen können Sie die Gruppen ausblenden / einblenden bzw. die Textfelder vergrößern / verkleinern.

Bei der Eingabe wird Ihnen die Anzahl der noch möglichen Zeichen angezeigt.

> **Hinweis**
>
> Es können Texte in allen Sprachen eingetragen werden, die in den Sprach-Einstellungen aktiviert wurden. Hauptmenü `Extras` → `Einstellungen` → `Immobilien` → `Sprachen`


#### Energieausweis {#usage_realestate_manage_form_energy-performance-certificate}

{{< figure src="realestate_form_energy.jpg" caption="Angaben zum Energieausweis erfassen" >}}

Wenn ein Energieausweis vorhanden ist aktivieren Sie das entsprechende Feld.

Danach wählen Sie die Art des Ausweises und tragen die Daten in die jeweiligen Felder ein.


#### Fotos & Dateien {#usage_realestate_manage_form_media}

Im Tab `Medien` können beliebig viele Bilder und Dateien zur Immobilie hinterlegt werden.

{{< figure src="realestate_form_images.jpg" caption="Bilder zur Immobilie erfassen" >}}


##### Fotos & Dateien hinzufügen {#usage_realestate_manage_form_media_files_add}

Klicken Sie auf den Button `Importieren` um eine Bild oder andere Dateien von Ihrer Festplatte in das ImmoTool zu laden und mit der Immobilie zuzuordnen.

Beim Import der Dateien erkennt das Programm automatisch, ob es sich um Bilder oder andere Anhänge handelt.

> **Tipp**
>
> Sie können mehrere Bilder auf einmal importieren, wenn Sie bei der Datei-Auswahl die `STRG` / `Shift` Taste gedrückt halten und mit der Maus die gewählten Bilder anklicken.

> **Hinweis**
>
> Es werden die gängigen Bildformate (JPG, PNG, GIF, TIF, BMP) abhängig von der verwendeten Java-Version unterstützt.

> **Hinweis**
>
> Importierte Fotos werden in der Datenbank gespeichert und die Originale müssen nicht dauerhaft auf der Festplatte verfügbar bleiben. Es empfiehlt sich jedoch dennoch, die importierten Dateien auch außerhalb des ImmoTools gespeichert zu halten.


##### Fotos & Dateien bearbeiten {#usage_realestate_manage_form_media_files_edit}

Nach dem Import können Sie jedes Foto einzeln durch Anklicken in der Übersicht aufrufen und weiter bearbeiten.

1.  Geben Sie zum Foto einen kurzen Beschreibungstext im Feld Titel in den gewünschten Sprachen ein. Dieser Bild-Titel wird z.B. zu Immobilienportalen gesendet und in Exposés dargestellt.

2.  Wählen Sie unter `Dateityp` die Art des Bildes - z.B. "Innenansicht" - aus.

3.  Legen Sie unter `Bild veröffentlichen` fest, ob das jeweilige Bild zu Immobilienportalen exportiert oder in Exposés dargestellt werden kann.

4.  Unter `Aktionen` können Sie mit den rötlichen Pfeiltasten das gewählte Bild horizontal / vertikal spiegeln bzw. nach rechts / links um 90 Grad drehen.

> **Hinweis**
>
> Die Titel der Bilder können in allen Sprachen abgelegt werden, welche in den Sprach-Einstellungen aktiviert wurden. `Extras` → `Einstellungen` → `Immobilien` → `Sprachen`


##### Fotos & Dateien entfernen {#usage_realestate_manage_form_media_files_remove}

Wählen Sie das zu entfernende Foto in der Vorschau aus und klicken Sie auf `Entfernen`. Das Bild wird ohne weitere Rückfrage unwiderruflich im ImmoTool gelöscht.


##### Fotos & Dateien sortieren {#usage_realestate_manage_form_media_files_sort}

Sie können die Sortierung der Fotos jederzeit ändern indem Sie die Bilder einzeln in der Übersicht markieren und dann mit den blauen Pfeilen (hoch / runter) an die gewünschte Position verschieben.
Eine Positionsänderung können Sie auch vornehmen indem Sie das Bild mit der Maus markieren und verschieben.


##### Fotos & Dateien exportieren {#usage_realestate_manage_form_media_files_export}

Sollten Sie ein Bilder für eine andere Anwendung benötigen, so klicken Sie oberhalb der großen Bild-Vorschau auf `Aktionen` →  `Exportieren`, wählen im erscheinenden Dialogfenster das Ziel aus, vergeben einen Dateinamen und speichern das Bild.


##### Fotos & Dateien austauschen {#usage_realestate_manage_form_media_files_change}

Einzelne Bilder können Sie gegen ein Anderes austauschen indem Sie es markieren und unter `Aktionen` →  `Austauschen` im folgenden Dialogfenster zum neuen Bild navigieren und es mit `Öffnen` gegen das Alte austauschen. Das Bild wird ohne weitere Rückfrage unwiderruflich im ImmoTool ausgetauscht.


##### Fotos & Dateien Format bearbeiten {#usage_realestate_manage_form_media_files_edit_format}

Das ImmoTool erkennt das Format der importierten Datei und fügt dieses unter `Format` ein. Dieses Feld sollte nur bearbeitet werden, wenn dies zwingend notwendig ist. Markieren Sie hierfür die Checkbox `Format bearbeiten` und tragen die entsprechende Angabe ein. 


#### Ansprechpartner {#usage_realestate_manage_form_contact}

Im Tab `Adressen` → `Ansprechpartner` kann der Ansprechpartner (Sie oder ein Mitarbeiter) zur Immobilie hinterlegt werden.

Der Ansprechpartner wird beim Export an Immobilienportale bzw. bei Exposé-Darstellungen für die Interessenten veröffentlicht. Sollte keine Ansprechpartner ausgewählt werden, wird statt dessen auf die Firmendaten unter `Extras` → `Anbieterprofil` zurückgegriffen.

{{< figure src="realestate_form_contact.jpg" caption="Kontaktperson zur Immobilie zuweisen" >}}


##### Einen Ansprechpartner zuweisen  {#usage_realestate_manage_form_contact_select}

Markieren Sie das Optionsfeld `Ansprechpartner auswählen`. Im daneben stehenden Auswahlfeld kann der gewünschte Ansprechpartner ausgewählt werden. Die Daten des gewählten Ansprechpartners werden im darunter stehenden Formular angezeigt und können hier bearbeitet werden.


##### Einen neuen Ansprechpartner erfassen {#usage_realestate_manage_form_contact_add}

Markieren Sie das Optionsfeld `neuer Ansprechpartner`. Im darunter stehenden Formular können die Daten des neuen Ansprechpartners eingegeben werden. Beim Speichern der Immobilie wird auch der hier eventuell neu angelegte Ansprechpartner gespeichert. 


##### Keinen Ansprechpartner angeben {#usage_realestate_manage_form_contact_nobody}

Markieren Sie das Optionsfeld `Keinen Ansprechpartner verwenden`. Sollte keine Ansprechpartner ausgewählt werden, wird statt dessen auf die Firmendaten zurückgegriffen. `Extras` → `Anbieterprofil`

> **Hinweis**
>
> Beim Speichern der Immobilie werden Änderungen bei einem bestehenden und bei einem neu angelegte Ansprechpartner dauerhaft gespeichert. 


#### Adressen {#usage_realestate_manage_form_addresses}

Im Tab `Adressen` können zu der Immobilie beliebig viele Adressen als Kontakte verknüpft werden.

{{< figure src="realestate_form_addresses.jpg" caption="Zugewiesene Adressen einer Immobilie" >}}


##### Bestehende Adresse zuordnen / verknüpfen {#usage_realestate_manage_form_addresses_assign}

Sollte die gewünschte Adresse bereits im Adressbuch verfügbar sein klicken Sie auf `Neue Zuordnung` und wählen im sich öffnenden Fenster die Adressgruppe, in welcher sich die Adresse befindet, und anschließend die Adresse selbst. Im Feld `Zuordnung` kann die Art des zugewiesenen Kontakts gewählt werden.

Nach Betätigung des Button `Übernehmen` wird diese Adresse der Immobilie zugeordnet und erscheint nun in der Tabelle `Bereits zugeordnete Adressen`.

{{< figure src="realestate_form_addresses_assign.jpg" caption="Adressen einer Immobilie zuweisen" >}}


##### Adresse anlegen {#usage_realestate_manage_form_addresses_add}

Ist die gewünschte Adresse noch nicht vorhanden, so klicken Sie auf den Reiter neue Adresse, und belegen die gewünschten Felder mit Einträgen. Danach klicken Sie auf den Button `Adresse zuordnen & speichern` um die Adresse in die Datenbank zu speichern und der Immobilie zuzuordnen.

{{< figure src="realestate_form_addresses_add.jpg" caption="Neue Adresse erfassen und zuweisen" >}}


##### Verknüpfung zur Adresse bearbeiten {#usage_realestate_manage_form_addresses_edit}

Um die Verknüpfung zu bearbeiten markieren Sie den Eintrag in der Liste mit der rechten Maustaste und wählen Sie `Zuordnung bearbeiten`. Alternativ markieren Sie den entsprechenden Eintrag mit der Maus, klicken auf den Button `Aktionen` und wählen Sie `Zuordnung bearbeiten` aus.

Es öffnet sich daraufhin ein Fenster, über welches die Verknüpfung bearbeitet werden kann. Bestätigen Sie Ihre Änderungen abschließend durch Klick auf den Button `Übernehmen`.


##### Verknüpfung zur Adresse löschen {#usage_realestate_manage_form_addresses_remove}

Um eine Verknüpfung mit einer Adresse zu löschen, markieren Sie den Eintrag in der Liste mit der rechten Maustaste und wählen Sie `Zuordnung entfernen`. Alternativ markieren Sie den entsprechenden Eintrag mit der Maus, klicken Sie auf den Button `Aktionen` und wählen Sie `Zuordnung entfernen` aus.

> **TODO**
>
> Tab Vermittlungsauftrag, Suchaufträge, Adresse und neu Adressen beschreiben. Ehemals Adressen.


#### Exporte {#usage_realestate_manage_form_export}

Im Tab `Exporte` → `Schnittstellen` können Einstellungen zum Export für eine Immobilie hinterlegt werden.

{{< figure src="realestate_form_exports.jpg" caption="Schnittstellen zum Export zuweisen" >}}


##### Schnittstellen {#usage_realestate_manage_form_export_interfaces}

Hier können Sie diese Immobilie den vorhandenen Schnittstelle zuordnen. Wählen Sie zwischen folgenden Optionen:

-   **Die Immobilie IMMER exportieren**

    Diese Immobilie wird bei jedem Export an alle eingerichtete / aktive Portale gesendet.

-   **Die Immobilie MIT den ausgewählten Schnittstellen exportieren**

    Diese Immobilie wird an die ausgewählten Portale gesendet, wenn diese Schnittstellen aktiv sind. Um eine Schnittstelle zuzuordnen markieren Sie diese mit der Maus.

-   **Die Immobilie NICHT mit den ausgewählten Schnittstellen exportieren**

    Diese Immobilie wird nicht an die ausgewählten Portale gesendet. Um eine Schnittstelle zuzuordnen markieren Sie diese mit der Maus.

-   **Die Immobilie NIE exportieren**

    Diese Immobilie wird bei keinem Export berücksichtigt.


##### Historie der Exporte {#usage_realestate_manage_form_export_history}

An dieser Stelle wird die Historie der bereits durchgeführten Exporte für die Immobilie dargestellt.

{{< figure src="realestate_form_exports_history.jpg" caption="Historie der Exporte zur Immobilie" >}}


#### Kalender {#usage_realestate_manage_form_calendars}

Im Tab `Kalender` können zu der Immobilie beliebig viele Kalendereinträge verknüpft werden.

{{< figure src="realestate_form_calendar.jpg" caption="Zugewiesene Termine der Immobilie" >}}


##### Bestehenden Kalendereintrag zuordnen / verknüpfen {#usage_realestate_manage_form_calendars_assign}

Sollte der gewünschte Kalendereintrag bereits im Kalender verfügbar sein klicken Sie auf `Neue Zuordnung` und wählen im sich öffnenden Fenster den Kalender, in welchem sich der Kalendereintrag befindet, und anschließend den Eintrag selbst. Nach Betätigung des Buttons `Übernehmen` wird dieser Kalendereintrag der Immobilie zugeordnet, und erscheint nun im Fenster zugeordnete Kalendereinträge.

{{< figure src="realestate_form_calendar_assign.jpg" caption="Vorhandenen Kalendereintrag der Immobilie zuweisen" >}}


##### Kalendereintrag anlegen {#usage_realestate_manage_form_calendars_add}

Ist der gewünschte Kalendereintrag (Aufgabe / Termin) noch nicht vorhanden, so klicken Sie auf den Reiter `neue Aufgabe` oder `neuer Termin`, und belegen die gewünschten Felder mit Einträgen. Danach klicken Sie auf den Button `Aufgabe speichern & zuordnen` bzw. `Termin speichern & zuordnen` um den Kalendereintrag zu speichern und der Immobilie zuzuordnen.

{{< figure src="realestate_form_calendar_add_task.jpg" caption="Neue Aufgabe der Immobilie zuweisen" >}}

{{< figure src="realestate_form_calendar_add_event.jpg" caption="Neuen Termin der Immobilie zuweisen" >}}


##### Kalendereintrag bearbeiten {#usage_realestate_manage_form_calendars_edit}

Um die Verknüpfung zu bearbeiten, markieren Sie den Eintrag in der Liste mit der rechten Maustaste und wählen `Zuordnung bearbeiten`. Alternativ markieren Sie den entsprechenden Eintrag mit der Maus, klicken auf den Button `Aktionen` und wählen Sie `Zuordnung bearbeiten`aus.

Bearbeiten Sie nun die Verknüpfung und speichern Sie diese mit dem Button `Übernehmen`.


##### Kalendereintrag löschen {#usage_realestate_manage_form_calendars_remove}

Um die Verknüpfung zu löschen, markieren Sie den Eintrag in der Liste mit der rechten Maustaste und wählen `Zuordnung entfernen`. Alternativ markieren Sie den entsprechenden Eintrag mit der Maus, klicken auf den Button `Aktionen` und wählen Sie `Zuordnung entfernen` aus.

> **TODO**
>
> Tab Kalender beschreiben.

> **TODO**
>
> Tab Aktionen beschreiben.


#### Notizen {#usage_realestate_manage_form_notes}

Im Tab `Notizen` können zu der Immobilie beliebige    Notizen hinterlegt werden.

{{< figure src="realestate_form_notes.jpg" caption="Notizen zur Immobilie hinterlegen" >}}

> **Hinweis**
>
> Der hinterlegte Notiztext wird vom Programm  **nicht veröffentlicht** - z.B. an Immobilienportale exportiert oder in Exposés dargestellt.


#### Änderungen speichern {#usage_realestate_manage_form_submit}

Um die Änderungen im Formular dauerhaft zu speichern, klicken Sie oben rechts auf den Button `Speichern`.

> **Hinweis**
>
> Das Speichern ist zu jedem Zeitpunkt der Bearbeitung möglich. Sollten relevante Eingaben fehlen, so weist dass Programm darauf hin.

> **Achtung**
>
> Jede Änderung im Formular muss am Ende der Bearbeitung durch Klick auf `Speichern` dauerhaft gespeichert werden.
