---

title: Installation am Arbeitsplatz
linktitle: Lokale Installation
description: OpenEstate-ImmoTool an einem Arbeitsplatz installieren…
weight: 50

menu:
  main:
    parent: intro
    identifier: intro-install-local

---

## ImmoTool als Einzelplatz-Version installieren {#intro_install_local}


### Was ist eine Einzelplatz-Installation? {#intro_install_local_info}

Bei einer Einzelplatz-Installation stellt das ImmoTool selbst alle nötigen Funktionen bereit. Weitere externe Programme (insbesondere ImmoTool-Server und AdminTool) müssen in diesem Falle **nicht** installiert werden.

Beim Programmstart wird automatisch eine Datenbank auf dem Rechner des Anwenders erstellt, in der alle erfassten Daten (Immobilien, Kunden, etc.) gespeichert werden.

> **Hinweis**
>
> Wenn Sie ImmoTool mit mehreren Mitarbeitern nutzen wollen, führen Sie bitte statt dessen eine [Netzwerk-Installation]({{< relref "install_network.md#intro_install_network" >}}) durch.


#### Vorteile einer Einzelplatz-Installation {#intro_install_local_pro}

-   Dies ist die einfachst mögliche Form, das ImmoTool in Betrieb zu nehmen, da nur ein einziges Programm installiert und gestartet werden muss.
-   Beim ersten Programmstart wird automatisch die Datenbank auf der Festplatte erzeugt und man kann sofort und ohne weiteren Aufwand mit der Arbeit beginnen.
-   Wenn Sie sich erst mal mit den Funktionen von ImmoTool vertraut machen möchten, ist eine Einzelplatz-Installation wegen der unkomplizierten Installation die beste Wahl. Im späteren Verlauf kann eine Einzelplatz-Installation jederzeit in eine Netzwerk-Installation umgewandelt werden.


#### Nachteile einer Einzelplatz-Installation {#intro_install_local_contra}

-   Die Datenbank einer Einzelplatz-Installation kann nicht von mehreren Benutzern / Mitarbeitern gleichzeitig geöffnet werden.
-   Es gibt keine Möglichkeiten zur Vergabe von Berechtigungen für verschiedene Benutzer. Bei einer Einzelplatz-Installation hat man grundsätzlich immer alle Berechtigungen.


### Programmpaket installieren

Das ImmoTool wird derzeit als [ZIP-Archiv](http://de.wikipedia.org/wiki/ZIP-Dateiformat) und [TAR.GZ-Archiv](http://de.wikipedia.org/wiki/Tar) [zum Download angeboten]({{< relref "download.md#intro_download" >}}). Entpacken Sie das heruntergeladene Archiv auf Ihrem Rechner.

Danach sollten Sie einen neuen Ordner namens `OpenEstate-ImmoTool` vorfinden. Verschieben Sie diesen Ordner an eine Stelle auf Ihrer Festplatte, von der Sie das Programm später leicht wieder finden können (z.B. in den Ordner "Eigenen Dateien").


### ImmoTool starten

Der entpackte Ordner `OpenEstate-ImmoTool` enthält diverse Dateien, über die das ImmoTool auf den verschiedenen Betriebssystemen gestartet werden kann:


#### ImmoTool unter Windows starten

Starten Sie das ImmoTool unter **Windows** durch Doppelklick auf die Datei `ImmoTool.exe` oder `ImmoTool.bat` im Unterordner `bin`.

> **Hinweis**
>
> Bei Bedarf können Sie sich eine Verknüpfung zur `ImmoTool.exe` / `ImmoTool.bat` auf dem Desktop oder ins Startmenü hinterlegen, um das Programm später schnell und unkompliziert starten zu können (siehe [Anleitung bei Microsoft](http://windows.microsoft.com/de-de/windows/create-delete-shortcut#1TC=windows-7)).


#### ImmoTool unter Mac OS X starten

Starten Sie das ImmoTool unter **Mac OS X** durch Doppelklick auf das ImmoTool-Symbol.

{{< figure src="../admin/client/startup_mac.jpg" caption="Programmverzeichnis mit dem ImmoTool-Starter" >}}

> **Hinweis**
>
> Bei Bedarf können Sie das ImmoTool-Symbol ins Dock integrieren, um das Programm später schnell und unkompliziert starten zu können (siehe [Anleitung bei Apple](http://support.apple.com/kb/HT2474?viewlocale=de_DE)).


#### ImmoTool unter Linux / Unix starten

Starten Sie das ImmoTool unter **Linux**, **Unix** oder **Mac OS X** durch Ausführung der Datei `ImmoTool.sh` im Unterordner `bin`.

> **Hinweis**
>
> Bei Bedarf können Sie die `ImmoTool.sh` ins Startmenü hinterlegen, um das Programm später schnell und unkompliziert starten zu können. Die Vorgehensweise hängt jedoch von der eingesetzten Linux-Distribution ab - erfragen Sie dies ggf. bitte beim Anbieter Ihrer Linux-Distribution oder probieren Sie dafür ein allgemeines Programm wie [MenuLibre](http://wiki.ubuntuusers.de/MenuLibre) oder [KMenuEdit](http://wiki.ubuntuusers.de/Men%C3%BCeditor#KDE).


### Sprache wählen

Beim ersten Programmstart prüft das `ImmoTool` ob eine Übersetzung zu der im Betriebssystem eingestellten Sprache vorliegt. Sollte dies nicht der Fall sein, erscheint das folgende Fenster, in dem Sie die im ImmoTool verwendete Sprache auswählen können:

> **TODO**
>
> Bild einfügen

Beachten Sie bitte, dass hier nur Sprachen zur Auswahl gestellt werden, für die aktuell eine vollständige Übersetzung vorliegt und für die ein Sprachpaket im Programm enthalten ist.


### Lizenzschlüssel eintragen

Beim ersten Programmstart werden Sie darüber hinaus darum gebeten, dass Ihren Lizenzschlüssel einzutragen. Sie erhalten einen persönlichen Lizenzschlüssel durch eine kostenlose Registrierung im [Anwender-Bereich von OpenEstate](http://dev.openestate.org/).

> **TODO**
>
> Bild einfügen

> **Hinweis**
>
> Die Eingabe eines Lizenzschlüssels ist freiwillig und kann auch übergangen werden. Das Programm kann dennoch im vollen Umfang genutzt werden. Es ist auch jederzeit möglich, dass im Nachhinein den Lizenzschlüssel im Programm zu hinterlegen.


### Einzelplatz-Projekt erzeugen

Der Projektassistent wird geöffnet und Sie können eine Datenbank für Ihre Arbeit mit dem ImmoTool erzeugen. Im Folgenden und innerhalb des Programms werden solche Datenbanken als **Projekt** bezeichnet.

> **TODO**
>
> Bild einfügen. Weitere Anmerkungen zum Projektassistenten einfügen
