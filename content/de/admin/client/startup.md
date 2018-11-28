---

title: Programmstart
linktitle: Programmstart
description: Administration von OpenEstate-ImmoTool…
weight: 10

menu:
  main:
    parent: admin-client
    identifier: admin-client-startup

---

## ImmoTool starten {#admin_client_startup}

Die Dateien zum Start des ImmoTools sind im Unterverzeichnis `bin` des Programmverzeichnisses abgelegt - z.B.: `C:\Programme\OpenEstate-ImmoTool\bin`.


### ImmoTool unter Windows starten {#admin_client_startup_windows}

Starten Sie das ImmoTool unter **Windows** durch Doppelklick auf die Datei `ImmoTool.exe` oder `ImmoTool.bat` im Unterordner `bin`.

> **Hinweis**
>
> Bei Bedarf können Sie sich eine Verknüpfung zur `ImmoTool.exe` / `ImmoTool.bat` auf dem Desktop oder ins Startmenü hinterlegen, um das Programm später schnell und unkompliziert starten zu können (siehe [Anleitung bei Microsoft](http://windows.microsoft.com/de-de/windows/create-delete-shortcut#1TC=windows-7)).


### ImmoTool unter Mac OS X starten {#admin_client_startup_mac}

Starten Sie das ImmoTool unter **Mac OS X** durch Doppelklick auf das ImmoTool-Symbol.

{{< figure src="startup_mac.jpg" caption="Programmverzeichnis mit dem ImmoTool-Starter" >}}

> **Hinweis**
>
> Bei Bedarf können Sie das ImmoTool-Symbol ins Dock integrieren, um das Programm später schnell und unkompliziert starten zu können (siehe [Anleitung bei Apple](http://support.apple.com/kb/HT2474?viewlocale=de_DE)).


### ImmoTool unter Linux / Unix starten {#admin_client_startup_unix}

Starten Sie das ImmoTool unter **Linux**, **Unix** oder **Mac OS X** durch Ausführung der Datei `ImmoTool.sh` im Unterordner `bin`.

> **Hinweis**
>
> Bei Bedarf können Sie die `ImmoTool.sh` ins Startmenü hinterlegen, um das Programm später schnell und unkompliziert starten zu können. Die Vorgehensweise hängt jedoch von der eingesetzten Linux-Distribution ab - erfragen Sie dies ggf. bitte beim Anbieter Ihrer Linux-Distribution oder probieren Sie dafür ein allgemeines Programm wie [MenuLibre](http://wiki.ubuntuusers.de/MenuLibre) oder [KMenuEdit](http://wiki.ubuntuusers.de/Men%C3%BCeditor#KDE).


### Parameter zum Start des ImmoTools {#admin_client_startup_params}

Der Programmstart des ImmoTools via `ImmoTool.exe` / `ImmoTool.bat` / `ImmoTool.sh` kann durch verschiedene Parameter beeinflusst werden.

-   **-help**
    Stellt eine Zusammenfassung aller Parameter auf der Konsole dar und beendet das Programm.

-   **-noProject**
    Startet das Programm ohne automatisch ein Projekt zu öffnen. Statt dessen wird der [Projektassistent]({{< relref "../../usage/general/projects.md#usage_general_projects_wizard" >}}) dargestellt.

-   **-noUpdate**
    Deaktiviert die Funktion zur automatischen Aktualisierung im Programm.

-   **-project `<PROJEKT>`**
    Das Projekt, welches im Ordner `<PROJEKT>` abgelegt ist, wird beim Programmstart automatisch geöffnet.

-   **-projectLogin `<BENUTZER>`**
    Wenn das unter `-project` angegebene Projekt ein Mehrplatz-Projekt ist, meldet sich das ImmoTool beim Programmstart automatisch mit dem Benutzernamen `<BENUTZER>` an.

-   **-projectPass `<PASSWORT>`**
    Wenn das unter `-project` angegebene Projekt ein Mehrplatz-Projekt ist, meldet sich das ImmoTool beim Programmstart automatisch mit dem Passwort `<PASSWORT>` an.
