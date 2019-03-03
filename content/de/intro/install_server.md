---

title: ImmoTool-Server installieren
linktitle: Server installieren
description: Wie OpenEstate-ImmoTool im Netzwerk installiert und eingerichtet werden kann…
weight: 60

menu:
  main:
    parent: intro
    identifier: intro-install-server

---

## ImmoTool-Server installieren {#intro_install_server}

Der ImmoTool-Server wird benötigt, wenn mehrere Mitarbeiter gleichzeitig auf einem gemeinsamen Datenbestand arbeiten sollen (siehe ["Betrieb an mehreren Arbeitsplätzen"]({{< relref "install_types.md#intro_install_types_network" >}})).

{{< info >}}
Wenn Sie das ImmoTool **nicht** im Netzwerk mit mehreren Mitarbeitern betreiben möchten, können Sie die Installation des ImmoTool-Servers überspringen und das ImmoTool als **Einzelplatz-Installation** betreiben (siehe ["Betrieb an einem einzelnen Arbeitsplatz"]({{< relref "install_types.md#intro_install_types_local" >}})). 
{{< /info >}}


### Programmpaket installieren {#intro_install_server_setup}

Laden Sie die zu Ihrem Betriebssystem passende Installationsdatei für den ImmoTool-Server herunter (siehe ["Programme herunterladen"]({{< relref "download.md#intro_download" >}})).


#### Installation unter Windows {#intro_install_server_setup_windows}

Laden Sie die zu Ihrem Windows passende **EXE**-Installationsdatei herunter. Unter einem 64bit-Windows sollte möglichst auch die 64bit-Installationsdatei verwendet werden.

Öffnen Sie die heruntergeladene EXE-Datei mit einem Doppelklick. Es startet daraufhin ein Installationsprogramm, welches Sie durch die weiteren Schritte der Installation leitet.

{{< figure src="install_server_windows.png" caption="Installation des ImmoTool-Servers unter Windows" >}}


#### Installation unter macOS {#intro_install_server_setup_mac}

Laden Sie die **DMG**-Installationsdatei herunter und öffnen Sie die Datei durch einen Doppelklick. Es öffnet sich daraufhin ein Fenster, über welches das Programm installiert werden kann.

{{< figure src="install_server_mac.jpg" caption="Installation des ImmoTool-Servers unter macOS" >}}

Ziehen Sie mit der Maus das Programmsymbol **"OpenEstate-ImmoServer"** in den Ordner **"Applications"**. Sie können das Programm dann zukünftig über den Finder im Ordner **"Programme"** öffnen.

Alternativ können Sie das Programmsymbol auch aus dem Installationsprogramm heraus auf die Arbeitsfläche oder an eine andere beliebige Stelle auf Ihrer Festplatte ziehen.


#### Installation unter Debian, Ubuntu & Co. {#intro_install_server_setup_debian}

Wenn Sie eine Debian-basierte Linux-Distribution nutzen (z.B. **Debian**, **Ubuntu** oder **Linux Mint**), empfehlen wir die Nutzung des Repositories (siehe ["Pakete aus Debian-Repository beziehen"]({{< relref "download.md#intro_download_debian" >}})). Nachdem das Repository erfolgreich eingerichtet wurde, kann das **Debian-Paket** über folgende Befehle installiert werden:

1.  Abruf der Paketliste:
    
    ```bash
    sudo apt update
    ```
    
2.  Installation des ImmoTools:

    ```bash
    sudo apt install openestate-immoserver
    ```

Sollten Sie das Repository nicht nutzen wollen, können Sie *alternativ* das **Debian-Paket** (bzw. die **DEB**-Installationsdatei) herunterladen und per Doppelklick oder durch folgenden Befehl installieren:

```bash
sudo dpkg -i openestate-immoserver_x.y.z_amd64.deb
```

Wobei **`x.y.z`** durch die jeweilige Versions-Nummer zu ersetzen ist.

{{< info >}}
Bei der Installation des Debian-Pakets wird das Programm im Verzeichnis **`/opt/OpenEstate-ImmoServer`** installiert.
{{< /info >}}

{{< info >}}
Bei der Installation des Debian-Pakets wird der ImmoTool-Server automatisch als Dienst im Betriebssystem registriert. Der ImmoTool-Server startet damit automatisch beim Hochfahren des Rechners (siehe ["ImmoTool-Server als Dienst einrichten"]({{< relref "../admin/server/service.md#admin_server_service" >}})). 

Ebenso wird automatisch eine tägliche Datensicherung eingerichtet, die jedoch noch konfiguriert werden muss (siehe ["Datensicherung eines laufenden ImmoTool-Servers"]({{< relref "../admin/backup.md#admin_backup_network_live" >}})).
{{< /info >}}


#### Installation unter Linux {#intro_install_server_setup_linux}

Wenn Sie keine Debian-basierte Linux-Distribution nutzen oder das Repository nicht einbinden wollen, können Sie alternativ die **TAR.GZ**-Installationsdateien herunterladen. Achten Sie darauf die richtige Installationsdatei für die verwendete Prozessor-Architektur zu verwenden (meist wird **x86-64** verwendet).

Nachdem Sie diese Datei auf Ihrem Rechner entpackt haben finden Sie einen Ordner namens **`OpenEstate-ImmoServer`**. Verschieben Sie diesen Ordner an eine Stelle Ihrer Wahl (z.B. ins Benutzerverzeichnis oder nach **`/opt/OpenEstate-ImmoServer`**).


### ImmoTool-Server starten {#intro_install_server_server_startup}

Für die erste Einrichtung bietet es sich an den ImmoTool-Server von Hand zu starten.

Erst wenn das Programm soweit erfolgreich eingerichtet wurde und von den Arbeitsplätzen erfolgreich auf den ImmoTool-Server zugegriffen werden kann, empfiehlt sich im nächsten Schritt die Einrichtung eines Dienstes, sodass der ImmoTool-Server automatisch beim Hochfahren des Rechners gestartet wird (siehe ["ImmoTool-Server als Dienst einrichten"]({{< relref "../admin/server/service.md#admin_server_service" >}})). 

{{< info >}}
Um mit dem ImmoTool-Server über das Netzwerk kommunizieren zu können, muss eventuell eine Regel in der Firewall hinterlegt werden. Benötigt wird in der Standardeinstellung eine Freigabe für eingehende Verbindungen auf Port-Nr **9001**.
{{< /info >}}


#### ImmoTool-Server unter Windows starten {#intro_install_server_startup_windows}

Bei der Installation unter Windows wird automatisch im Startmenü einen Ordner namens **"OpenEstate-ImmoServer"** mit verschiedenen Verknüpfungen erzeugt. Wählen Sie die Verknüpfung **"ImmoServer manuell starten"** aus dem Startmenü aus um den ImmoTool-Server von Hand zu starten.

Darüber hinaus können Sie das Programm auch über die Datei **`Start.exe`** (bzw. **`Start.bat`**) im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "../admin/server/directories.md#admin_server_directories_application" >}}) manuell starten.


#### ImmoTool-Server unter macOS starten {#intro_install_server_startup_mac}

Führen Sie einen Doppelklick auf das Programmsymbol mit der Bezeichnung **"OpenEstate-ImmoServer"** aus. Es öffnet sich daraufhin der Finder mit den vom ImmoTool-Server bereitgestellten Programmen.

{{< figure src="../admin/server/startup_mac_folder.png" caption="Starter für ImmoTool-Server im Finder" >}}

Wenn Sie in diesem Fenster auf das Programmsymbol **"Start"** klicken, wird der ImmoTool-Server manuell gestartet.


#### ImmoTool-Server unter Linux starten {#intro_install_server_startup_linux}

Wenn der ImmoTool-Server mit dem [**Debian**-Paket]({{< relref "install_server.md#intro_install_server_setup_debian" >}}) installiert wurde, ist auf dem Betriebssystem bereits ein Dienst für den ImmoTool-Server eingerichtet und gestartet worden. Sie müssen in diesem Falle keine weiteren Schritte durchführen um das Programm zu starten.

Bei allen Installations-Varianten für Linux kann der ImmoTool-Server über die Datei **`Start.sh`** im Unterordner **`bin`** des [Programm-Verzeichnisses]({{< relref "../admin/server/directories.md#admin_server_directories_application" >}}) manuell gestartet werden.


### ImmoTool-Server vorbereiten {#intro_install_server_prepare}

Bevor der ImmoTool-Server genutzt werden kann, muss darauf eine Datenbank eingerichtet werden. Um diesen Schritt durchzuführen muss das [**AdminTool**]({{< relref "../admin/tool.md#admin_tool" >}}) gestartet werden, welches gemeinsam mit dem ImmoTool-Paket installiert wird.

Installieren Sie dafür das ImmoTool auf dem Server-Rechner oder einem anderen Rechner in Ihrem Netzwerk (siehe ["ImmoTool installieren"]({{< relref "install_client.md#intro_install_client" >}})) und starten Sie danach das AdminTool (siehe ["AdminTool starten"]({{< relref "../admin/tool.md#admin_tool_startup" >}})).

{{< figure src="install_server_admintool_connect.png" caption="Verbindung zur Datenbank mit AdminTool herstellen" >}}

Im dargestellten Fenster muss die Option **"Mit entfernter Datenbank verbinden (auf Server gespeichert)"** gewählt werden. Danach können die Verbindungsdaten des ImmoTool-Servers eingetragen werden: 

-   **Datenbank:** \
     Hier sollte die Option **"HSQL.remote"** gewählt werden.

-   **Protokoll:** \
     Im Normalfall muss hier **"hsql"** gewählt werden. Wenn eine Verschlüsselung auf dem Server eingerichtet wurde, muss hier **"hsqls"** gewählt werden (siehe ["SSL-Verschlüsselung einrichten"]({{< relref "../admin/server/setup.md#admin_server_setup_ssl" >}})).

-   **Hostname:** \
     Hier muss die IP-Adresse oder der Hostname des Rechners eingetragen werden, auf dem der ImmoTool-Server betrieben wird. Wenn das AdminTool vom gleichen Rechner gestartet wurde auf dem sich auch der ImmoTool-Server befindet, kann der Hostname **"localhost"** unverändert bleiben.

-   **Port-Nr:** \
     Die Port-Nummer lautet standardmäßig **"9001"**. Nur wenn im ImmoTool-Server ein anderer Wert konfiguriert wurde, muss der Standard-Wert geändert werden.

-   **DB-Name:** \
     Der Name der Datenbank lautet standardmäßig **"immotool"**. Nur wenn im ImmoTool-Server eine Datenbank unter einem anderen Namen konfiguriert wurde, muss der Standard-Wert geändert werden.

-   **Benutzer:** \
    Der Name des Administrator-Benutzers lautet **"SA"** und muss in der Regel nicht geändert werden.

-   **Passwort:** \
    Beim ersten Verbindungsaufbau mit dem ImmoTool-Server ist das Passwort leer. Nachdem ein Passwort in der Datenbank hinterlegt wurde, muss dieses hier eingetragen werden.

Nach einem Klick auf **"Verbinden"** verbindet sich das AdminTool mit dem ImmoTool-Server. 

Im ersten Schritt wird das Programm feststellen, dass der Administrator-Benutzer (**"SA"**) noch kein Passwort zugewiesen hat und um die Eingabe eines Passwortes bitten. Notieren Sie sich dieses Passwort!

{{< figure src="install_server_admintool_password.png" caption="Passwort des Administrators im AdminTool festlegen" >}}

Im folgenden Schritt wird das Programm feststellen, dass die Datenbank noch nicht eingerichtet wurde. Klicken Sie im Dialogfenster **"Neues Projekt erzeugen"** auf **"Übernehmen"** um die Datenbank zur Verwendung für das ImmoTool vorzubereiten. 

{{< figure src="install_server_admintool_setup.png" caption="Installation der Datenbank im ImmoTool-Server" >}}

Nachdem diese Schritte abgeschlossen sind, können Sie bei Bedarf über das AdminTool weitere Benutzerkonten in der Datenbank anlegen (siehe ["Benutzer bearbeiten"]({{< relref "../admin/tool.md#admin_tool_users" >}})).

Wenn eventuelle Nacharbeiten abgeschlossen wurden, kann das AdminTool geschlossen werden. Ab diesem Zeitpunkt können sich Anwender über das ImmoTool mit dem ImmoTool-Server verbinden.


### Verbindung zum ImmoTool-Server herstellen {#intro_install_server_immotool}

Nachdem der ImmoTool-Server erfolgreich vorbereitet wurde (siehe ["ImmoTool-Server vorbereiten"]({{< relref "install_server.md#intro_install_server_prepare" >}})) kann über das ImmoTool auf die Datenbank zugegriffen werden.

Auf **jedem Arbeitsplatz** muss dafür das ImmoTool installiert werden (siehe ["ImmoTool installieren"]({{< relref "install_client.md#intro_install_client" >}})). Nach dem Programmstart (siehe ["ImmoTool starten"]({{< relref "install_client.md#intro_install_client_startup" >}})) muss ein sogenanntes **Mehrplatz-Projekt** angelegt werden. Öffnen Sie dafür den Projekt-Assistenten (falls dieser nicht automatisch startet via **"Hauptmenü → Projekt → neues Projekt"**).

{{< figure src="install_server_immotool_project.png" caption="Neues Mehrplatz-Projekt im Projekt-Assistenten einrichten" >}}

Folgende Einstellungen sind im Projekt-Assistenten vorzunehmen:

-   **Projekt-Name:** \
    Tragen Sie einen beliebigen Namen für das Projekt ein.

-   **Projekt-Art:** \
    Wählen Sie **"Neue Verbindung zu einem Mehrplatz-Projekt erzeugen."** aus.
    
-   **Datenbank:** \
    Hier sollte die Option **"HSQL.remote"** gewählt werden.

-   **Protokoll:** \
    Im Normalfall muss hier **"hsql"** gewählt werden. Wenn eine Verschlüsselung auf dem Server eingerichtet wurde, muss hier **"hsqls"** gewählt werden (siehe ["SSL-Verschlüsselung einrichten"]({{< relref "../admin/server/setup.md#admin_server_setup_ssl" >}})).
    
-   **Hostname:** \
    Hier muss die IP-Adresse oder der Hostname des Rechners eingetragen werden, auf dem der ImmoTool-Server betrieben wird. Wenn das ImmoTool vom gleichen Rechner gestartet wurde auf dem sich auch der ImmoTool-Server befindet, kann der Hostname **"localhost"** unverändert bleiben.
    
-   **Port-Nr:** \
    Die Port-Nummer lautet standardmäßig **"9001"**. Nur wenn im ImmoTool-Server ein anderer Wert konfiguriert wurde, muss der Standard-Wert geändert werden.
    
-   **DB-Name:** \
    Der Name der Datenbank lautet standardmäßig **"immotool"**. Nur wenn im ImmoTool-Server eine Datenbank unter einem anderen Namen konfiguriert wurde, muss der Standard-Wert geändert werden.
    
-   **Benutzer:** \
    Der Name des Benutzers, der sich auf der Datenbank anmeldet. Wenn über das AdminTool weitere Benutzer angelegt wurden, kann hier dessen Login-Name eingetragen werden. Andernfalls kann der Benutzer **"SA"**, um sich als Administrator anzumelden.
    
-   **Passwort:** \
    Das Passwort des Benutzers, der sich auf der Datenbank anmeldet. Wenn über das AdminTool weitere Benutzer angelegt wurden, kann hier dessen Passwort eingetragen werden. Andernfalls kann das zuvor gewählte Passwort des Benutzers **"SA"** verwendet werden.

Bevor das Projekt erzeugt werden kann, muss auf **"Anmelden"** geklickt werden. Wenn hier kein Fehler auftritt, kann das Projekt durch Klick auf **"Projekt erzeugen"** erzeugt werden. Das Mehrplatz-Projekt wird daraufhin erzeugt und automatisch geöffnet.

Bei zukünftigen Programmstarts kann das erzeugte Mehrplatz-Projekt im Programm geöffnet werden. Der Benutzer muss sich dann nur noch mit seinem Benutzernamen und Passwort authentifizieren. 

{{< figure src="install_server_immotool_login.png" caption="Anmeldung an einem bestehenden Mehrplatz-Projekt" >}}
