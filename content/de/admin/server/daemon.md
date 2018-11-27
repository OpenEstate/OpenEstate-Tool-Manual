---

title: Einrichtung als Dienst
linktitle: Dienst
description: Administration von OpenEstate-ImmoTool…
weight: 30

menu:
  main:
    parent: admin-server
    identifier: admin-server-daemon

---

## *ImmoTool-Server* als Dienst einrichten {#admin_server_daemon}

In der alltäglichen Praxis ist es hilfreich, den ImmoTool-Server als Dienst in das Betriebssystem zu integrieren. Der ImmoTool-Server kann damit automatisch beim Booten des Betriebssystems gestartet werden. Ebenso kann der Administrator den Dienst von außen unkompliziert steuern (Start / Stopp / Neustart).


### Dienst unter Windows einrichten {#admin_server_daemon_windows}


#### Dienst unter Windows installieren {#admin_server_daemon_windows_install}

Um den *ImmoTool-Server* im Betriebssystem als Dienst zu registrieren, kann die Datei `server-daemon-install.bat` im Explorer mit einem Doppelklick gestartet werden.

Alternativ kann das `bin`-Verzeichnis des *ImmoTool-Servers* in der Eingabeaufforderung geöffnet werden - z.B.

```
cd C:\Programme\OpenEstate-ImmoServer\bin
```

Nach Eingabe von

```
server-daemon-install.bat
```

wird die Installation des Dienstes im Betriebssystem durchgeführt.


#### Dienst unter Windows deinstallieren {#admin_server_daemon_windows_uninstall}

Um den Dienst des *ImmoTool-Servers* aus dem Betriebssystem zu entfernen, kann die Datei `server-daemon-uninstall.bat` im Explorer mit einem Doppelklick gestartet werden.

Alternativ kann das `bin`-Verzeichnis des *ImmoTool-Servers* in der Eingabeaufforderung geöffnet werden - z.B.

```
cd C:\Programme\OpenEstate-ImmoServer\bin
```

Nach Eingabe von

```
server-daemon-uninstall.bat
```

wird der Dienst aus dem Betriebssystem entfernt.


#### Dienst unter Windows verwalten {#admin_server_daemon_windows_manage}

Nachdem der Dienst installiert wurde finden Sie einen Eintrag zum *ImmoTool-Server* in der Dienstverwaltung des Betriebssystems.

1.  Öffnen Sie die Systemsteuerung und klicken Sie auf `Verwaltung`.

    {{< figure src="daemon_windows-01.jpg" caption="Verwaltung in der Systemsteuerung" >}}

2.  Klicken Sie im Verwaltungsfenster auf `Dienste`.

    {{< figure src="daemon_windows-02.jpg" caption="Dienste in der Systemsteuerung" >}}

Aus der Dienstverwaltung des Betriebssystems kann der *ImmoTool-Server* manuell gestartet werden:

{{< figure src="daemon_windows-03.jpg" caption="Den Dienst manuell starten." >}}

Aus der Dienstverwaltung des Betriebssystems kann der *ImmoTool-Server* manuell beendet werden:

{{< figure src="daemon_windows-04.jpg" caption="Den Dienst manuell neu starten / stoppen." >}}

> **Hinweis**
>
> In der Standardinstallation wird der Dienst beim Hochfahren des Betriebssystems automatisch gestartet. Wenn kein automatischer Start gewünscht ist, klicken Sie mit rechter Maustaste auf den Dienst und wählen Sie `Eigenschaften`. Im darauf geöffneten Fenster kann der gewünschte `Starttyp` festgelegt werden.

> **Hinweis**
>
> Auf neueren Windows-Systemen muss eventuell muss ein Systembenutzer gewählt werden, der zum Start des *ImmoTool-Servers* verwendet werden soll. Klicken Sie dafür mit rechter Maustaste auf den Dienst, wählen Sie `Eigenschaften` und wählen Sie im folgenden Fenster den Reiter `Anmelden` aus. Aktivieren Sie die Option `Dieses Konto` und tragen Sie Namen und das Passwort des zu verwendenden Systembenutzers ein.
>
> {{< figure src="daemon_windows-05.jpg" caption="Systembenutzer für den Dienst auswählen" >}}


#### Dienst unter Windows mit Hilfsskript starten {#admin_server_daemon_windows_start}

Um den *ImmoTool-Server* im Betriebssystem als Dienst zu starten, kann die Datei `server-daemon-start.bat` im Explorer mit einem Doppelklick gestartet werden.

Alternativ kann das `bin`-Verzeichnis des *ImmoTool-Servers* in der Eingabeaufforderung geöffnet werden - z.B.

```
cd C:\Programme\OpenEstate-ImmoServer\bin
```

Nach Eingabe von

```
server-daemon-start.bat
```

wird der Dienst im Betriebssystem gestartet.


#### Dienst unter Windows mit Hilfsskript beenden {#admin_server_daemon_windows_stop}

Um den *ImmoTool-Server* im Betriebssystem als Dienst zu stoppen, kann die Datei `server-daemon-stop.bat` im Explorer mit einem Doppelklick gestartet werden.

Alternativ kann das `bin`-Verzeichnis des *ImmoTool-Servers* in der Eingabeaufforderung geöffnet werden - z.B.

```
cd C:\Programme\OpenEstate-ImmoServer\bin
```

Nach Eingabe von

```
server-daemon-stop.bat
```

wird der Dienst im Betriebssystem beendet.


### Dienst unter Mac OS X einrichten {#admin_server_daemon_mac}

> **TODO**
>
> Anleitung für Mac OS X muss überarbeitet und überprüft werden.

> **Hinweis**
>
> In den folgenden Beispielen wird davon ausgegangen, dass der ImmoTool-Server im Verzeichnis `/Applications/OpenEstate-Server` installiert wurde. Sollte Sie ein anderes Installationsverzeichnis verwenden, müssen die folgenden Befehle entsprechend angepasst werden.

> **Hinweis**
>
> Standardmäßig wird der Dienst des ImmoTool-Servers unter Mac OS X im Verzeichnis `/Library/LaunchDaemons` registriert. Damit kann der Dienst beim Start von Mac OS X gestartet werden, ohne dass ein Mac-Benutzer angemeldet sein muss. Dies setzt jedoch voraus, dass die Befehle von einem Administrator ausgeführt werden. In den folgenden Beispielen wird deshalb jeder Befehl beginnend mit `sudo` gestartet. Sollten Sie bereits als Administrator angemeldet sein, kann auf die Angabe von `sudo` verzichtet werden.

> **Tipp**
>
> Weitere Informationen zu [launchd](http://de.wikipedia.org/wiki/Launchd) finden Sie unter [launchd Daemonverwaltung unter Mac OS X](http://www.apfelwiki.de/Main/Launchd), [Einführung zu launchd](http://www.macosxhints.ch/index.php?page=2&hintid=1759) und [Manual page for “launchctl”](http://developer.apple.com/library/mac/#documentation/Darwin/Reference/Manpages/man1/launchctl.1.html).


#### Dienst unter Mac OS X installieren {#admin_server_daemon_mac_install}

Öffnen Sie das `bin`-Verzeichnis des *ImmoTool-Servers* im Terminal, z.B.:

```
cd /Applications/OpenEstate-Server/bin
```

Folgender Befehl installiert den Dienst im Betriebssystem:

```
sudo ./server-daemon-install.sh
```

Oder alternativ:

```
sudo sh server-daemon-install.sh
```

Mit folgendem Befehel können Sie prüfen, ob der Dienst im Betriebssystem installiert wurde:

```
sudo launchctl list
```

Es sollte eine Auflistung aller installierten Dienste dargestellt werden. Bei einer korrekten Installation sollten Sie den Dienst *wrapper.OpenEstate-Server* vorfinden.


#### Dienst unter Mac OS X deinstallieren {#admin_server_daemon_mac_uninstall}

Nachdem der Dienst installiert wurde, kann dieser mit dem Hilfsprogramm `launchctl` aus dem Terminal heraus wieder deinstalliert werden:

```
sudo launchctl unload /Library/LaunchDaemons/wrapper.OpenEstate-Server
```

Alternativ kann der installierte Dienst aus dem Programmverzeichnis des *ImmoTool-Servers* heraus deinstalliert werden. Wählen Sie dieses über das Terminal aus:

```
cd /Applications/OpenEstate-Server/bin
```

Folgender Befehl entfernt den zuvor installierten Dienst aus dem Betriebssystem:

```
sudo ./server-daemon-uninstall.sh
```

Oder alternativ:

```
sudo sh server-daemon-uninstall.sh
```

#### Dienst unter Mac OS X mit Hilfsskript starten {#admin_server_daemon_mac_start}

Nachdem der Dienst installiert wurde, kann dieser mit dem Hilfsprogramm `launchctl` aus dem Terminal heraus gestartet werden:

```
sudo launchctl start wrapper.OpenEstate-Server
```

Alternativ kann der installierte Dienst aus dem Programmverzeichnis des *ImmoTool-Servers* heraus gestartet werden. Wählen Sie dieses über das Terminal aus:

```
cd /Applications/OpenEstate-Server/bin
```

Und starten Sie den *ImmoTool-Server* mit folgendem Befehl:

```
sudo ./server-daemon-start.sh
```

Oder alternativ:

```
sudo sh server-daemon-start.sh
```


#### Dienst unter Mac OS X mit Hilfsskript beenden {#admin_server_daemon_mac_stop}

Nachdem der Dienst installiert wurde, kann dieser mit dem Hilfsprogramm `launchctl` aus dem Terminal heraus gestoppt werden:

```
sudo launchctl start wrapper.OpenEstate-Server
```

Alternativ kann der installierte Dienst aus dem Programmverzeichnis des *ImmoTool-Servers* heraus gestoppt werden. Wählen Sie dieses über das Terminal aus:

```
cd /Applications/OpenEstate-Server/bin
```

Und beenden Sie den gestarteten *ImmoTool-Server* mit folgendem Befehl:

```
sudo ./server-daemon-stop.sh
```

Oder alternativ:

```
sudo sh server-daemon-stop.sh
```


### Dienst unter Linux einrichten {#admin_server_daemon_linux}

> **TODO**
>
> Anleitung für Linux muss überarbeitet und überprüft werden. Darüber hinaus ist zu berücksichtigen, dass unter Linux verschiedene Init-Systeme berücksichtigt werden müssen (inbesondere SysVInit, Upstart, Systemd).

> **Hinweis**
>
> In den folgenden Beispielen wird davon ausgegangen, dass der ImmoTool-Server im Verzeichnis `/opt/OpenEstate-Server` installiert wurde. Sollte Sie ein anderes Installationsverzeichnis verwenden, müssen die folgenden Befehle entsprechend angepasst werden.


#### Vorbereitungen zur Einrichtung des Dienstes unter Linux {#admin_server_daemon_linux_preparation}

Auf unixoiden Betriebssystemen werden die Dienste in einem zentralen Verzeichnis hinterlegt. Normalerweise sind diese Skripte unter einem der folgenden Verzeichnissen zu finden:

-   `/etc/init.d`
-   `/etc/rc.d`

Bringen Sie in Erfahrung, an welcher Stelle auf Ihrem Betriebssystem die Dienste hinterlegt werden. Bearbeiten Sie die Datei `etc/wrapper.conf` mit einem Editor und tragen Sie darin den Pfad hinter der Variablen `wrapper.daemon.dir` ein. Zum Beispiel:

```
wrapper.daemon.dir = /etc/init.d
```

oder

```
wrapper.daemon.dir = /etc/rc.d
```


#### Dienst unter Linux installieren {#admin_server_daemon_linux_install}

Öffnen Sie das `bin`-Verzeichnis des ImmoTool-Servers in einer Konsole, z.B.:

```
cd /opt/OpenEstate-Server/bin
```

Folgender Befehl installiert den Dienst im zuvor konfigurierten Verzeichnis (z.B. `/etc/init.d`):

```
./server-daemon-install.sh
```

Oder alternativ:

```
sh server-daemon-install.sh
```


#### Dienst unter Linux deinstallieren {#admin_server_daemon_linux_uninstall}

Öffnen Sie das `bin`-Verzeichnis des ImmoTool-Servers in einer Konsole, z.B.:

```
cd /opt/OpenEstate-Server/bin
```

Folgender Befehl entfernt den Dienst aus dem zuvor konfigurierten Verzeichnis (z.B. `/etc/init.d`):

```
./server-daemon-uninstall.sh
```

Oder alternativ:

```
sh server-daemon-uninstall.sh
```


#### Dienst unter Linux starten {#admin_server_daemon_linux_start}

Nachdem der Dienst installiert wurde, kann dieser aus dem Dienste-Verzeichnis (z.B. `/etc/init.d`) heraus gestartet werden:

```
/etc/init.d/OpenEstate-Server start
```

Alternativ kann der Dienst aus dem Programmverzeichnis des ImmoTool-Servers heraus gestartet werden. Wählen Sie dieses über die Konsole:

```
cd /opt/OpenEstate-Server/bin
```

Und starten Sie den ImmoTool-Server mit folgendem Befehl:

```
./server-daemon-start.sh
```

Oder alternativ:

```
sh server-daemon-start.sh
```

Der Neustart eines bereits gestarteten ImmoTool-Servers kann durchgeführt werden mit:

```
/etc/init.d/OpenEstate-Server restart
```


#### Dienst unter Linux stoppen {#admin_server_daemon_linux_stop}

Nachdem der Dienst installiert und gestartet wurde, kann dieser aus dem Dienste-Verzeichnis (z.B. `/etc/init.d`) heraus gestoppt werden:

```
/etc/init.d/OpenEstate-Server stop
```

Alternativ kann der Dienst aus dem Programmverzeichnis des ImmoTool-Servers heraus beendet werden. Wählen Sie dieses über die Konsole:

```
cd /opt/OpenEstate-Server/bin
```

Und beenden Sie den gestarteten ImmoTool-Server mit folgendem Befehl:

```
./server-daemon-stop.sh
```

Oder alternativ:

```
sh server-daemon-stop.sh
```
