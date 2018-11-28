---

title: Einrichtung des Servers
linktitle: Einrichtung
description: Administration von OpenEstate-ImmoTool…
weight: 20

menu:
  main:
    parent: admin-server
    identifier: admin-server-setup

---

## ImmoTool-Server konfigurieren {#admin_server_setup}

Die Dateien zur Konfiguration des ImmoTool-Servers sind im Unterverzeichnis `etc` des Programmverzeichnisses abgelegt, z.B.: `C:\Programme\OpenEstate-ImmoServer\etc`

Im Einzelfall kann es hilfreich sein, die Konfiguration des ImmoTool-Servers auf die eigenen Bedürfnisse hin anzupassen. Für die meisten Fälle sollte die ausgelieferte Standard-Konfiguration jedoch ausreichend sein.


### Datenbanken konfigurieren {#admin_server_setup_databases}

In der Datei `etc/server.properties` können die vom ImmoTool-Server bereitgestellten Datenbanken konfiguriert werden. Standardmäßig stellt der ImmoTool-Server exakt eine Datenbank mit dem Namen *immotool* bereit.

Bei Bedarf können über diese Datei noch weitere Datenbanken eingerichtet werden, die ebenfalls von ImmoTool-Server bereitgestellt werden sollen. Weitere Informationen zu dieser Konfigurationsdatei finden Sie in der [Dokumentation von HSQLDB](http://hsqldb.org/doc/2.0/guide/listeners-chapt.html#listeners_server_props-sect).

Im Folgenden wird die Vorgehensweise beschrieben, um eine weitere Datenbank namens `immotool2` im ImmoTool-Server zu registrieren.

1.  Beenden Sie den ImmoTool-Server, sollte dieser aktuell in Betrieb sein.

2.  Öffnen Sie die Datei `etc/server.properties` mit einem Texteditor und tragen Sie am Ende der Datei Folgendes ein:

    ```
    # database #1
    server.database.1=file:./var/data/immotool2/db
    server.dbname.1=immotool2
    ```

    Damit wird eine zweite Datenbank mit der Bezeichnung `immotool2` registriert, deren Daten im Unterverzeichnis `var/data/immotool2` des ImmoTool-Servers abgelegt werden.

3.  Speichern Sie die geänderte Datei `etc/server.properties` ab und starten Sie den ImmoTool-Server neu.

4.  Via AdminTool & ImmoTool kann man nun eine Verbindung zur zweiten Datenbank herstellen. Beim Verbindungsaufbau muss dabei der neue Datenbankname `immotool2` angegeben werden.

Allgemein können in der Datei `etc/server.properties` beliebig viele Datenbanken mit frei wählbarem Namen registriert werden. Für jede weitere Datenbank muss der Zähler erhöht werden - z.B.:

```
# database #0
server.database.0=file:./var/data/immotool/db
server.dbname.0=immotool

# database #1
server.database.1=file:./var/data/mydb/db
server.dbname.1=mydb

# database #2
server.database.2=file:./var/data/anotherdb/db
server.dbname.2=anotherdb
```


### Protokollierungen konfigurieren {#admin_server_setup_logging}

Über die Datei `etc/log4j.properties` kann die Erzeugung der Protokolldateien konfiguriert werden. Standardmäßig werden die Protokolle des ImmoTool-Servers im Verzeichnis `var/log` als `hsqldb.log.*` abgelegt.

Weitere Informationen zu dieser Konfigurationsdatei finden Sie in der [Dokumentation von log4j](http://logging.apache.org/log4j/1.2/manual.html).


### Manager-Skripte konfigurieren {#admin_server_setup_manager}

In der Datei `etc/manager.conf` können die administrativen Zugangsdaten zur Datenbank hinterlegt werden, die von den Startdateien `bin/manager-*` verwendet werden.

Weitere Informationen zu dieser Konfigurationsdatei finden Sie in der [Dokumentation von HSQLDB](http://hsqldb.org/doc/2.0/util-guide/sqltool-chapt.html#sqltool_auth-sect).


### Wrapper konfigurieren {#admin_server_setup_wrapper}

In der Datei `etc/wrapper.conf` wird der YAJSW-Wrapper konfiguriert. Diese Komponente wird nur verwendet, wenn der ImmoTool-Server über Startskripte `bin/server-*` betrieben wird.

Weitere Informationen zu dieser Konfigurationsdatei finden Sie in der Dokumentation von [YAJSW](http://yajsw.sourceforge.net/YAJSW%20Configuration%20Parameters.html).


### SSL-Verschlüsselung konfigurieren {#admin_server_setup_ssl}

Wenn sich der ImmoTool-Server außerhalb des lokalen Firmen-Netzwerkes befindet oder Verbindungen über das Internet zulässt, empfiehlt es sich die Kommunikation zwischen ImmoTool & ImmoTool-Server zu verschlüsseln.

Es ist aber auch in anderen Fällen grundsätzlich sinnvoll eine Verschlüsselung durchzuführen, da es hierbei zu einem Gewinn an Sicherheit und Integrität bei der Datenübertragung kommt. Jedoch ist damit zu rechen, dass die Kommunikation geringfügig länger als bei einer unverschlüsselten Verbindung dauern wird.

> **Hinweis**
>
> Der ImmoTool-Server erlaubt **keine gleichzeitige Verwendung von verschlüsselten und unverschlüsselten Verbindungen**. Sie müssen sich für einen der beiden Wege entscheiden und entsprechend [alle ImmoTools in Ihrem Netzwerk konfigurieren](#admins.server.ssl.client).


#### SSL-Zertifikat erzeugen {#admin_server_setup_ssl_cert}

Um eine verschlüsselte Datenübertragung zu realisieren, muss auf dem ImmoTool-Server ein SSL-Zertifikat bereit liegen. Dieses stellt die Vertrauenswürdigkeit des ImmoTool-Servers gegenüber den darauf zugreifenden ImmoTools sicher.

Im Programmverzeichnis des ImmoTool-Servers finden Sie das Verzeichnis `etc/ssh`. Darin ist ein Skript `init_ssl.bat` / `init_ssl.sh` enthalten. Mit Hilfe dieses Skripts kann ein SSL-Schlüsselpaar und SSL-Zertifikat für den ImmoTool-Server erstellt werden.

Starten Sie das Skript `init_ssl.bat` (unter Windows) bzw. `init_ssl.sh` (unter Mac/Linux) via Doppelklick oder per Eingabeaufforderung / Terminal.

Nachdem das Skript (`init_ssl.bat` / `init_ssl.sh`) gestartet wurde sind folgende Eingaben vorzunehmen:

1.  Wählen Sie ein Passwort aus, mit welchem das erzeugte SSL-Schlüsselpaar vor unberechtigtem Zugriff abgesichert werden soll. Das gewählte Passwort wird zu einem späteren Zeitpunkt noch benötigt.

    {{< figure src="setup_ssl_cert-01.jpg" caption="Passwort zur Absicherung der SSL-Schlüssel wählen" >}}

2.  Tragen Sie als `Vor- und Nachname` den Hostnamen oder die IP-Adresse Ihres Servers ein.

    {{< figure src="setup_ssl_cert-02.jpg" caption="Name des abzusichernden Servers angeben (“Common Name”)" >}}

    Im SSL-Zertifikat wird diese Angabe als sogenannter "Common Name" (CN) verwendet.

    > **Wichtig**
    >
    > Der gewählte "Common Name" **muss** in Ihrem Netzwerk auf den ImmoTool-Server verweisen. Beim Aufbau einer verschlüsselten Verbindung über das ImmoTool **muss** dieser Name als Hostname verwendet werden.

    > **Hinweis**
    >
    > Wenn Sie statt eines Hostnamens eine IP-Adresse als "Common Name" verwenden, sollten Sie sicherstellen, dass die IP-Adresse in Ihrem Netzwerk permanent gleich bleibt. Mit jeder Änderung der IP-Adresse muss auch ein neues SSL-Zertifikat erzeugt werden.

3.  Verschiedene weitere Angaben werden abgefragt. Hier können beliebige Eingaben vorgenommen werden - passend zur jeweiligen Firma.

    {{< figure src="setup_ssl_cert-03.jpg" caption="Weitere Details zum SSL-Schlüssel angeben" >}}

4.  Es sollte **kein Schlüsselkennwort** eingegeben werden. Bestätigen Sie die Eingabe einfach mit `ENTER`.

    {{< figure src="setup_ssl_cert-04.jpg" caption="Passwort zur Absicherung der SSL-Schlüssels angeben" >}}

5.  Damit im letzten Schritt das SSL-Zertifikat zu dem SSL-Schlüsselpaar exportiert werden kann, tragen Sie nochmals das im ersten Schritt gewählte Passwort ein.

    {{< figure src="setup_ssl_cert-05.jpg" caption="Zertifikat zum SSL-Schlüssel exportieren" >}}

Nachdem das Skript erfolgreich ausgeführt wurde finden Sie im Verzeichnis `etc/ssl` zwei weitere Dateien.

-   `OpenEstate-ImmoServer.jks`
    Die Datei enthält das erzeugte SSL-Schlüsselpaar des ImmoTool-Servers.

-   `OpenEstate-ImmoServer.crt`
    Die Datei enthält das erzeugte SSL-Zertifikat des ImmoTool-Servers.

Das erzeugte SSL-Zertifikat des ImmoTool-Servers ist *für 999 Tage gültig*. Nach Ablauf dieser Zeit muss ein neues SSL-Zertifikat erzeugt werden. Führen Sie das Skript (`init_ssl.bat` / `init_ssl.sh`) erneut aus, um ein neues SSL-Zertifikat für die nächsten 999 Tage zu erzeugen. Nach der Neu-Erzeugung muss der ImmoTool-Server neu gestartet werden.

Sollte das Skript (`init_ssl.bat` / `init_ssl.sh`) nicht gestartet werden können, kann die Erzeugung der SSL-Daten alternativ über die folgenden Befehle auf der Eingabeaufforderung / Terminal erfolgen:

```
keytool -genkey \
  -alias OpenEstate-ImmoServer \
  -keyalg RSA -validity 999 \
  -keystore OpenEstate-ImmoServer.jks \
  -storetype JKS
```

```
keytool -export \
  -alias OpenEstate-ImmoServer \
  -keystore OpenEstate-ImmoServer.jks \
  -rfc -file OpenEstate-ImmoServer.crt
```


#### SSL-Verschlüsselung aktivieren {#admin_server_setup_ssl_enable}

Dem ImmoTool-Server muss mitgeteilt werden, dass eine verschlüsselte Kommunikation erfolgen soll. Öffnen Sie dafür die Datei `etc/server.properties` aus dem Programmverzeichnis des ImmoTool-Servers mit einem Texteditor. Die folgenden Einträge müssen vorgenommen werden:

```
# TLS/SSL (secure) sockets
server.tls=true
system.javax.net.ssl.keyStore=./etc/ssl/OpenEstate-ImmoServer.jks
system.javax.net.ssl.keyStorePassword=MEIN-SSL-PASSWORT
```

-   `server.tls`
    Durch den Wert `true` wird die SSL-Verschlüsselung im ImmoTool-Server aktiviert.

-   `system.javax.net.ssl.keyStore`
    Hier muss der Pfad zur JKS-Datei angegeben werden. Die Datei wurde zuvor mit dem Hilfsskript (`init_ssl.bat` / `init_ssl.sh`) erstellt und enthält die zur SSL-Verschlüsselung nötigen Daten.

-   `system.javax.net.ssl.keyStorePassword`
    Hier muss das Passwort eingetragen werden, dass Sie während der Erzeugung des SSL-Schlüsselpaares gewählt haben.

Damit die Änderungen an der Datei `etc/server.properties` wirksam werden, muss der ImmoTool-Server neu gestartet werden.

> **Hinweis**
>
> Wenn das Betriebssystem es ermöglicht, empfiehlt es sich die Zugriffsrechte auf die Datei `etc/server.properties` zu limitieren, sodass andere Benutzer des Betriebssystems nicht darauf zugreifen können. Unter Linux / Mac entspricht dies:
>
> ```
> chmod 600 server.properties
> ```


#### SSL-Verschlüsselung in ImmoTool / AdminTool aktivieren {#admin_server_setup_ssl_client}

Beim Aufbau der Verbindung muss als Protokoll `hsqls` ausgewählt werden, damit das ImmoTool / AdminTool eine verschlüsselte Verbindung zum ImmoTool-Server herstellen kann.

Beim Erzeugen eines neuen Projekts kann im [Projektassistenten](usage_general_projects.md#usage_general_projects_wizard) das Protokoll `hsqls` gewählt werden, um eine verschlüsselte Verbindung zum ImmoTool-Server herzustellen.

{{< figure src="setup_ssl_immotool-01.jpg" caption="SSL-Verschlüsselung via Projektassistent aktivieren" >}}

Beim Öffnen eines bestehenden Projekts kann bei der Anmeldung zusätzlich das Protokoll `hsqls` gewählt werden, um eine verschlüsselte Verbindung zum ImmoTool-Server herzustellen.

{{< figure src="setup_ssl_immotool-02.jpg" caption="SSL-Verschlüsselung bei der Anmeldung am Projekt aktivieren" >}}

Beim Verbindungsaufbau mit dem AdminTool kann das Protokoll `hsqls` gewählt werden, um eine verschlüsselte Verbindung zum ImmoTool-Server herzustellen.

{{< figure src="setup_ssl_admintool-01.jpg" caption="SSL-Verschlüsselung beim Verbindungsaufbau via AdminTool aktivieren" >}}
