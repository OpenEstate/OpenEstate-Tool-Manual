---

title: Zertifikate im Programm verwalten
linktitle: Zertifikate
description: Zertifikate in OpenEstate-ImmoTool verwalten…
weight: 70

menu:
  main:
    parent: usage-general
    identifier: usage-general-certificates

---

## Zertifikate {#usage_general_certificates}


### Was sind Zertifikate? {#usage_general_certificates_info}

ImmoTool unterstützt an verschiedenen Stellen [SSL-Verschlüsselung](http://de.wikipedia.org/wiki/Transport_Layer_Security) (z.B. beim Immobilienexport oder E-Mailabruf). Ein wesentlicher Bestandteil der Verschlüsselung sind [digitale Zertifikate](http://de.wikipedia.org/wiki/Digitales_Zertifikat). Damit wird die [Authentizität](http://de.wikipedia.org/wiki/Authentizit%C3%A4t) und [Integrität](http://de.wikipedia.org/wiki/Integrit%C3%A4t_%28Informationssicherheit%29) der jeweiligen Gegenstelle sichergestellt.

{{< info >}}
Ein Zertifikat besitzt immer eine bestimmte Lebensdauer. Sobald diese "Lebenszeit" abgelaufen ist, muss die Gegenstelle ein neues Zertifikat bereitstellen. Das neue Zertifikat wird dann erneut beim erstmaligen Verbindungsaufbau heruntergeladen und Ihnen zur Prüfung vorgelegt.
{{< /info >}}


### Prüfung eines Zertifikats {#usage_general_certificates_validation}

Sobald das Programm **erstmals** mit einer Gegenstelle verschlüsselt kommuniziert, wird das folgende Fenster mit den Details des Zertifikats der Gegenstelle dargestellt:

{{< figure src="certificates_import.jpg" caption="Zertifikat von Google prüfen" >}}

Dieses Fenster stellt verschiedene Informationen dar, mit der die Gegenstelle (in diesem Falle "google.com") identifiziert werden kann. An dieser Stelle muss der Anwender die Angaben prüfen und kann entscheiden, ob er der Gegenstelle sein Vertrauen aussprechen möchte.

- Um der Gegenstelle das Vertrauen auszusprechen, kann auf **"Übernehmen"** geklickt werden. Danach beginnt das ImmoTool die verschlüsselte Kommunikation mit der jeweiligen Gegenstelle.

- Um der Gegenstelle kein Vertrauen auszusprechen, kann auf **"Abbrechen"** geklickt werden. Das ImmoTool wird in diesem Falle die verschlüsselte Kommunikation abbrechen.

{{< warning >}}
Es ist Vorsicht geboten, wenn sich das Zertifikat einer Gegenstelle ändert und Sie dieses erneut bestätigen / prüfen sollen. Um sich vor sogenannten [Man-in-the-middle-Angriffen](http://de.wikipedia.org/wiki/Man-in-the-middle-Angriff) zu schützen, sollten Sie sich im Zweifelsfall von der jeweiligen Gegenstelle die Korrektheit des neuen Zertifikats bestätigen lassen.
{{< /warning >}}


### Verwaltung der Zertifikate {#usage_general_certificates_management}

Klicken Sie im Hauptmenü auf **"Extras → Zertifikate"** um die bereits bestätigten Zertifikate einsehen und bearbeiten zu können. Es öffnet sich daraufhin ein Fenster, das ungefähr wie folgt aussieht:

{{< figure src="certificates_dialog.jpg" caption="Verwaltung der Zertifikate" >}}

Auf der linken Seite wird eine Liste der bereits erfassten Zertifikate dargestellt. Wählen Sie einen der Einträge in der Liste aus, um auf der rechten Seite weitere Details über das gewählte Zertifikat dargestellt zu bekommen.

Um die Änderungen der vertrauenswürdigen Zertifikaten (Importe, Löschungen, etc.) dauerhaft zu speichern, muss auf **"Übernehmen"** geklickt werden. Wenn die Änderungen nicht gespeichert werden sollen, kann auf **"Abbrechen"** geklickt werden.


#### Zertifikat importieren {#usage_general_certificates_management_import}

Klicken Sie auf den Button **"Einfügen"**. Es erscheint daraufhin ein Untermenü mit folgenden Einträgen:


-   **Zertifikat aus Datei laden**
    Verwenden Sie diese Option, um das Zertifikat aus einer Datei zu importieren, die auf Ihrem Rechner abgelegt ist.


-   **Zertifikat von Server herunterladen**
    Verwenden Sie diese Option, um das Zertifikat von einem Server herunterzuladen. Dabei muss Hostname / IP-Adresse des Servers sowie dessen Port-Nr angegeben werden.


#### Zertifikat entfernen {#usage_general_certificates_management_remove}

Markieren Sie das zu entfernende Zertifikat in der Liste und klicken Sie auf **"Entfernen"** um den gewählten Eintrag aus dem Programm zu entfernen.


#### Zertifikat exportieren {#usage_general_certificates_export}

Markieren Sie das zu entfernende Zertifikat in der Liste und klicken Sie auf **"Export"** um den gewählten Eintrag als separate Datei auf Ihrem Rechner zu speichern.

