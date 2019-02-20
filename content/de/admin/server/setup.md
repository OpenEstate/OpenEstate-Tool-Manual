---

title: Konfiguration des ImmoTool-Servers
linktitle: Konfiguration
description: Konfiguration von OpenEstate-ImmoServer…
weight: 30

menu:
  main:
    parent: admin-server
    identifier: admin-server-setup

---

## ImmoTool-Server konfigurieren {#admin_server_setup}

Im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) des ImmoTool-Servers finden Sie diverse Dateien, über welche das Verhalten des ImmoTool-Servers auf Ihre Bedürfnisse hin angepasst werden kann.

{{< info >}}
Für die meisten Anwendungsfälle sollte die ausgelieferte Standard-Konfiguration des ImmoTool-Servers ausreichend sein. Änderungen an der Konfiguration sollten nur vorgenommen werden, wenn dies unbedingt nötig ist.
{{< /info >}}


### Datenbanken konfigurieren {#admin_server_setup_databases}

Im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) des ImmoTool-Servers finden Sie eine Datei namens `server.properties`. Über diese Datei können die vom ImmoTool-Server bereitgestellten Datenbanken konfiguriert werden.

Standardmäßig stellt der ImmoTool-Server exakt eine Datenbank mit dem Namen `immotool` bereit. Bei Bedarf können über `server.properties` Datei noch weitere Datenbanken eingerichtet werden, die ebenfalls von ImmoTool-Server bereitgestellt werden. Weitere Informationen zu dieser Konfigurationsdatei finden Sie in der [Dokumentation von HSQLDB](http://hsqldb.org/doc/2.0/guide/listeners-chapt.html#lsc_server_props).

Um zum Beispiel eine weitere Datenbank namens `immotool2` im ImmoTool-Server zu registrieren, kann wie folgt vorgegangen werden:

1.  Beenden Sie den ImmoTool-Server, sollte dieser aktuell in Betrieb sein.

2.  Öffnen Sie die Datei `server.properties` mit einem Texteditor und tragen Sie am Ende der Datei Folgendes ein:

    ```ini
    # database #1
    server.database.1=file:${openestate.server.varDir}/data/immotool2/db
    server.dbname.1=immotool2
    ```

    Damit wird eine zweite Datenbank mit der Bezeichnung `immotool2` registriert, deren Daten im [Daten-Verzeichnis]({{< relref "directories.md#admin_server_directories_data" >}}) des ImmoTool-Servers im Ordner `data/immotool2` abgelegt werden.

3.  Speichern Sie die geänderte Datei `server.properties` ab und starten Sie den ImmoTool-Server neu.

4.  Via AdminTool kann man nun eine Verbindung zur zweiten Datenbank herstellen und die nötigen Einrichtungen vornehmen (siehe ["ImmoTool-Server vorbereiten"]({{< relref "../../intro/install_server.md#intro_install_server_prepare" >}})). Beim Verbindungsaufbau mit dem AdminTool muss dabei der neue Datenbank-Name `immotool2` angegeben werden.

5.  Nachdem die Datenbank via AdminTool vorbereitet wurde, kann über das ImmoTool darauf zugegriffen werden (siehe ["Verbindung zum ImmoTool-Server herstellen"]({{< relref "../../intro/install_server.md#intro_install_server_immotool" >}})). Beim Verbindungsaufbau mit dem ImmoTool muss dabei der neue Datenbank-Name `immotool2` angegeben werden.

Allgemein können in der Datei `server.properties` **beliebig viele Datenbanken** mit frei wählbarem Namen registriert werden. Für jede weitere Datenbank muss der Zähler erhöht werden - z.B.:

```ini
# database #0
server.database.0=file:${openestate.server.varDir}/data/immotool/db
server.dbname.0=immotool

# database #1
server.database.1=file:${openestate.server.varDir}/data/mydb/db
server.dbname.1=mydb

# database #2
server.database.2=file:${openestate.server.varDir}/data/anotherdb/db
server.dbname.2=anotherdb
```

{{< info >}}
Die Zeichenkette `${openestate.server.varDir}` wird automatisch durch den Pfad zum aktuell konfigurierten [Daten-Verzeichnis]({{< relref "directories.md#admin_server_directories_data" >}}) ersetzt.
{{< /info >}}


### Protokollierung konfigurieren {#admin_server_setup_logging}

Im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) des ImmoTool-Servers finden Sie eine Datei namens `log4j.properties`. Über diese Datei kann die Protokollierung des ImmoTool-Servers konfiguriert werden.

Standardmäßig werden die Protokolle im [Protokoll-Verzeichnis]({{< relref "directories.md#admin_server_directories_log" >}}) abgelegt. In der Regel ist es nicht nötig, die Protokollierung des ImmoTool-Servers individuell anzupassen. Weitere Informationen zu dieser Konfigurationsdatei finden Sie in der [Dokumentation von log4j](https://logging.apache.org/log4j/1.2/manual.html).

{{< info >}}
Die Zeichenkette `${openestate.server.logDir}` in der Datei `log4j.properties` wird automatisch durch den Pfad zum [Protokoll-Verzeichnis]({{< relref "directories.md#admin_server_directories_log" >}}) ersetzt.
{{< /info >}}

{{< info >}}
Die Zeichenkette `${openestate.server.app}` in der Datei `log4j.properties` wird automatisch durch den Namen der aktuellen Anwendung ersetzt. Somit können für verschiedene Anwendungen unterschiedliche Protokoll-Dateien erzeugt werden.
{{< /info >}}


### Manager-Programme konfigurieren {#admin_server_setup_manager}

Der ImmoTool-Server stellt verschiedene Hilfsprogramme zur Verwaltung der Datenbanken bereit (sogenannte "Manager-Programme"). Diese Manager-Programme verbinden sich mit den Datenbanken des ImmoTool-Servers, um bestimmte administrative Aufgaben durchzuführen (z.B. ["Datensicherung eines laufenden ImmoTool-Servers"]({{< relref "../backup.md#admin_backup_network_live" >}})).

Damit die Manager-Programme ihre Aufgabe erfüllen können, müssen diese sich auf den Datenbanken des ImmoTool-Servers als Benutzer mit administrativen Rechten anmelden. Die dafür benötigten Zugangsdaten werden im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) in der Datei `manager.conf` hinterlegt.

Für jede vom ImmoTool-Server verwaltete Datenbank sind folgende Zeilen in der Datei `manager.conf` zu hinterlegen:

```ini
urlid immotool
url jdbc:hsqldb:hsql://localhost/immotool
username SA
password test1234
```

-   Der Wert hinter **urlid** gibt einen eindeutigen Namen für die Datenbank-Verbindung an. Verwenden Sie der Einfachheit halber am besten den gleichen Namen, der auch im ImmoTool-Server für die Datenbank verwendet wird.

-   Der Wert hinter **url** gibt die Adresse an, über welche eine Verbindung zur Datenbank hergestellt werden kann. 

    -   Da das Manager-Programm in der Regel über den gleichen Rechner ausgeführt wird, auf dem auch der ImmoTool-Server betrieben wird, kann als Adresse `localhost` verwendet werden.
    
    -   Hinter der Adresse `localhost` folgt ein Schrägstrich mit dem Namen der zu verwaltenden Datenbank (wie er als `server.dbname` in der Datei `server.properties` konfiguriert wurde).
    
    -   Sollte der ImmoTool-Server mit SSL-Verschlüsselung betrieben werden, muss `hsql://` durch `hsqls://` ersetzt werden.

-   Der Wert hinter **username** gibt den Namen des in der Datenbank konfigurierten Administrators an. Standardmäßig enthält jede verwaltete Datenbank einen Administrator-Benutzer mit dem Namen `SA`. Insofern ist hier in der Regel keine Änderung nötig.

-   Der Wert hinter **password** gibt das Passwort des als **username** angegebenen Benutzers an. Tragen Sie hier das Passwort ein, das Sie für den Administrator bei der Einrichtung der Datenbank im AdminTool vergeben haben (siehe ["ImmoTool-Server vorbereiten"]({{< relref "../../intro/install_server.md#intro_install_server_prepare" >}})).

Für die drei im Kapitel ["Datenbanken konfigurieren"]({{< relref "setup.md#admin_server_setup_databases" >}}) beschriebenen Beispiel-Datenbanken wären folgende Einträge in der Datei `manager.conf` zu hinterlegen:

```ini
urlid immotool
url jdbc:hsqldb:hsql://localhost/immotool
username SA
password test1234

urlid mydb
url jdbc:hsqldb:hsql://localhost/mydb
username SA
password test2345

urlid anotherdb
url jdbc:hsqldb:hsql://localhost/anotherdb
username SA
password test3456
```

(Die Passwörter müssten entsprechend ersetzt werden.)

Weitere Informationen zu dieser Konfigurationsdatei finden Sie in der [Dokumentation von HSQLDB](http://hsqldb.org/doc/2.0/util-guide/sqltool-chapt.html#sqltool_auth-sect).

{{< warning >}}
Die Datei `manager.conf` enthält sensible Zugangsdaten. Sie sollten daher die Berechtigungen im Betriebssystem für diese Datei anpassen. Es sollten nur Betriebssystem-Benutzer diese Datei lesen können, die auch die Manager-Programme ausführen.
{{< /warning >}}


### SSL-Verschlüsselung einrichten {#admin_server_setup_ssl}

Wenn sich der ImmoTool-Server außerhalb des lokalen Firmen-Netzwerkes befindet oder Verbindungen über das Internet zulässt, empfiehlt es sich die Kommunikation zwischen ImmoTool & ImmoTool-Server zu verschlüsseln.

Es kann auch in anderen Fällen grundsätzlich sinnvoll sein eine Verschlüsselung durchzuführen, da es hierbei zu einem Gewinn an Sicherheit und Integrität bei der Datenübertragung kommt. Jedoch ist damit zu rechen, dass die Kommunikation geringfügig länger als bei einer unverschlüsselten Verbindung dauern wird.

{{< info >}}
Der ImmoTool-Server erlaubt **keine** gleichzeitige Verwendung von verschlüsselten und unverschlüsselten Verbindungen. Sie müssen sich für einen der beiden Wege entscheiden und entsprechend **alle** ImmoTool-Installationen in Ihrem Netzwerk konfigurieren (siehe ["SSL-Verschlüsselung in ImmoTool aktivieren"]({{< relref "setup.md#admin_server_setup_ssl_immotool" >}})).
{{< /info >}}


#### SSL-Zertifikat erzeugen {#admin_server_setup_ssl_cert}

Um eine verschlüsselte Datenübertragung zu realisieren, muss auf dem ImmoTool-Server ein SSL-Zertifikat vorhanden sein. Dieses stellt die Vertrauenswürdigkeit des ImmoTool-Servers gegenüber den darauf zugreifenden Programmen sicher.

Der ImmoTool-Server stellt ein Programm bereit, über welches das benötigte SSL-Zertifikat erzeugt werden kann.

-   Unter Windows können Sie im Startmenü auf **"OpenEstate-ImmoServer → Verwaltung → SSL-Zertifikat erzeugen"** klicken, um das Programm zur Erzeugung des SSL-Zertifikats zu starten.

-   Unter macOS finden Sie das Programm nach Doppelklick auf das Programmsymbol **"OpenEstate-ImmoServer"** unter dem Namen **"SslInit"**.

-   Alternativ können Sie im [Programm-Verzeichnis]({{< relref "directories.md#admin_server_directories_application" >}}) den Ordner `bin` öffnen. Dort finden Sie das Programm unter dem Namen `SslInit.exe` / `SslInit.bat` / `SslInit.sh`.

Nachdem das Programm gestartet wurde, öffnet sich eine Konsole / ein Terminal. 

{{< figure src="setup_ssl_cert_settings.png" caption="Einstellungen zum SSL-Zertifikat vornehmen" >}}

1.  Tragen Sie die **IP-Adresse** (bzw. den Hostnamen) ein, über welche eine Verbindung vom ImmoTool mit dem ImmoTool-Server erfolgt. Das SSL-Zertifikat wird für exakt diese IP-Adresse (bzw. exakt diesen Hostnamen) erzeugt. In allen Programmen muss dann diese IP-Adresse (bzw. dieser Hostname) für den Verbindungsaufbau verwendet werden.

2.  Im folgenden Schritt ist ein **Keystore-Passwort** einzutragen, über welches das Zertifikat abgesichert wird. Notieren Sie sich das verwendete Passwort für die spätere Verwendung.

Nachdem diese Eingaben vorgenommen wurden erstellt das Programm im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) einen Ordner namens `ssl` und hinterlegt dort die erzeugten Dateien. Abschließend wird folgende Zusammenfassung dargestellt: 

{{< figure src="setup_ssl_cert_summary.png" caption="Zusammenfassung zum SSL-Zertifikat" >}}

{{< warning >}}
Der Ordner `ssl` im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) enthält sensible Daten. Sie sollten daher die Berechtigungen im Betriebssystem für diesen Ordner anpassen. Es sollten nur Betriebssystem-Benutzer auf diesen Ordner zugreifen können, die auch den ImmoTool-Server ausführen.
{{< /warning >}}

{{< info >}}
Sollte das Programm zur Erzeugung des SSL-Zertifikats nicht gestartet werden können, können die benötigten Dateien alternativ über die folgenden Befehle erzeugt werden:

```bash
keytool -genkey \
  -alias OpenEstate-ImmoServer \
  -keyalg RSA -validity 999 \
  -keystore keystore.jks \
  -storetype JKS

keytool -export \
  -alias OpenEstate-ImmoServer \
  -keystore keystore.jks \
  -rfc -file private.crt
```

Das dafür verwendete keytool-Programm befindet sich im `bin`-Verzeichnis der Java-Laufzeitumgebung.

Die nach Ausführung des keytool-Programms erzeugten Dateien sind entsprechend in den Unterordner `ssl` des [Konfigurations-Verzeichnisses]({{< relref "directories.md#admin_server_directories_etc" >}}) zu kopieren.
{{< /info >}}


#### SSL-Verschlüsselung aktivieren {#admin_server_setup_ssl_enable}

Dem ImmoTool-Server muss mitgeteilt werden, dass eine verschlüsselte Kommunikation erfolgen soll. Öffnen Sie dafür die Datei `server.properties` im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) mit einem Texteditor. Die folgenden Zeilen müssen bearbeitet werden:

```
# TLS/SSL (secure) sockets
server.tls=true
system.javax.net.ssl.keyStore=${openestate.server.etcDir}/ssl/keystore.jks
system.javax.net.ssl.keyStorePassword=test1234
```

-   Der Wert hinter **server.tls** muss auf `true` gesetzt werden um SSL-Verschlüsselung im ImmoTool-Server zu aktivieren.

-   Hinter **system.javax.net.ssl.keyStore** ist der Pfad anzugeben, unter dem die Keystore-Datei (`keystore.jks`) zu finden ist. In der Regel muss dieser Wert **nicht** verändert werden.

-   Hinter **system.javax.net.ssl.keyStorePassword** muss das Passwort eingetragen werden, dass Sie während der Erzeugung des SSL-Zertifikats gewählt haben.

Damit die Änderungen an der Konfiguration wirksam werden, muss der ImmoTool-Server neu gestartet werden.


#### SSL-Verschlüsselung im ImmoTool nutzen {#admin_server_setup_ssl_immotool}

Beim Erzeugen eines neuen Projekts im ImmoTool muss im [Projektassistenten]({{< relref "../../usage/general/projects.md#usage_general_projects_wizard" >}}) das **Protokoll "hsqls"** gewählt werden, um eine verschlüsselte Verbindung zum ImmoTool-Server herzustellen.

{{< figure src="setup_ssl_immotool_project.png" caption="SSL-Verschlüsselung via Projektassistent aktivieren" >}}

Beim Öffnen eines bestehenden Projekts kann auch nachträglich die Verschlüsselung aktiviert werden. Klicken Sie dafür auf **"Verbindungsdaten des Servers bearbeiten""** und wählen Sie als **Protokoll "hsqls"** aus. Diese Einstellung wird dauerhaft für das Projekt gespeichert und muss später nicht erneut vorgenommen werden.

{{< figure src="setup_ssl_immotool_login.png" caption="SSL-Verschlüsselung bei Anmeldung am Projekt aktivieren" >}}


#### SSL-Verschlüsselung im AdminTool nutzen {#admin_server_setup_ssl_admintool}

Beim Verbindungsaufbau mit dem AdminTool muss das **Protokoll "hsqls"** gewählt werden, um eine verschlüsselte Verbindung zum ImmoTool-Server herzustellen.

{{< figure src="setup_ssl_admintool.png" caption="SSL-Verschlüsselung im AdminTool aktivieren" >}}


#### SSL-Verschlüsselung in Manager-Programmen nutzen {#admin_server_setup_ssl_manager}

Die Manager-Programme werden über die Datei `manager.conf` im [Konfigurations-Verzeichnis]({{< relref "directories.md#admin_server_directories_etc" >}}) des ImmoTool-Servers konfiguriert.

Bearbeiten Sie diese Datei mit einem Texteditor und ändern Sie die Werte hinter **url** für alle konfigurierten Datenbanken. Statt `hsql://` muss `hsqls://` verwendet werden. Im Beispiel aus Kapitel ["Manager-Programme konfigurieren"]({{< relref "setup.md#admin_server_setup_manager" >}}) wären z.B. folgende Anpassungen vorzunehmen:

```ini
urlid immotool
url jdbc:hsqldb:hsqls://localhost/immotool
username SA
password test1234

urlid mydb
url jdbc:hsqldb:hsqls://localhost/mydb
username SA
password test2345

urlid anotherdb
url jdbc:hsqldb:hsqls://localhost/anotherdb
username SA
password test3456
```
