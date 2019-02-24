---

title: Sammlung von Fachbegriffen
linktitle: Fachbegriffe
description: Fachbegriffe im OpenEstate-ImmoTool…
weight: 10

menu:
  main:
    parent: appendix
    identifier: appendix-glossary

---


## Glossar {#appendix_glossary}

### Atom {#appendix_glossary_atom}

ist ein verbreitetes Format für den Austausch von Nachrichten. Viele Webseiten stellen ihre Nachrichten als sogenannter "Atom-Feed" bereit. Weitere Informationen finden Sie bei [wikipedia.org](http://de.wikipedia.org/wiki/Atom_%28Format%29).


### Einzelplatz-Projekt {#appendix_glossary_project_local}

steht exklusiv dem Anwender zur Verfügung, der das Einzelplatz-Projekt im ImmoTool geöffnet hat. Ein gemeinsamer Zugriff durch andere ImmoTool-Anwender ist nicht möglich.

Die Datenbank eines Einzelplatz-Projektes wird direkt im Projektverzeichnis gespeichert. Ein ImmoTool-Server muss für ein Einzelplatz-Projekt deshalb **nicht** installiert werden.


### Hostname {#appendix_glossary_hostname}

ist ein eindeutiger Name für einen Rechner im Netzwerk. Beim Aufruf eines Hostnamens wird dieser zu einer IP-Adresse übersetzt / aufgelöst. Der Hostname `openestate.org` entspricht z.B. der IP-Adresse `188.40.136.84`.

Die Verwendung von Hostnamen hat den Vorteil, dass man diese sich leichter merken kann als eine IP-Adresse. Ebenso kann ein Administrator bei Verwendung von Hostnamen die IP-Adresse jederzeit ändern, ohne dass die Teilnehmer im Netzwerk davon gestört werden.

Weitere Informationen finden Sie bei [wikipedia.org](http://de.wikipedia.org/wiki/Hostname).


### HSQLDB {#appendix_glossary_hsqldb}

ist eine in Java geschriebene Datenbank. Das ImmoTool verwendet diese Software zur Speicherung der Projektdaten. Weitere Informationen finden Sie bei [hsqldb.org](http://hsqldb.org/).


### ImmoTool-Server {#appendix_glossary_immotool_server}

ist eine Anwendung, die eine HSQL-Datenbank im Netzwerk zur Verfügung stellt. Dies ermöglicht den Zugriff mehrerer ImmoTool-Anwender auf einen gemeinsamen Datenbestand (Mehrplatz-Projekt).


### ImmoXML {#appendix_glossary_immoxml}

ist ein Format für den Austausch von Immobiliendaten. Die Spezifikation basiert auf Version 1.1 von OpenImmo-XML. Weitere Informationen finden Sie bei [immoxml.de](http://immoxml.de/).


### IP-Adresse {#appendix_glossary_ip}

wird zur Identifikation eines einzelnen Computers im Netzwerk / Internet verwendet. Weitere Informationen finden Sie bei [wikipedia.org](http://de.wikipedia.org/wiki/IP-Adresse).

{{< tip >}}
{{< figure src="ip_windows-01.jpg" caption="Klicken Sie auf `Start` → `Einstellungen` → `Netzwerkverbindungen`." >}}

{{< figure src="ip_windows-02.jpg" caption="Wählen Sie in der Übersicht die verwendete LAN-Verbindung mit Doppelklick aus." >}}

{{< figure src="ip_windows-03.jpg" caption="Im Reiter `Netzwerkunterstützung` wird die IP-Adresse der Netzwerkkarte dargestellt." >}}
{{< /tip >}}

{{< tip >}}
{{< figure src="ip_unix-01.jpg" caption="Öffnen Sie eine Kommandozeile und geben Sie den Befehl `ifconfig` ein. Darauf werden Informationen zu den installierten Netzwerk-Schnittstellen (inkl. der IP-Adressen) dargestellt. In der Regel ist die verwendete Netzwerkkarte mit `eth0` benannt." >}}
{{< /tip >}}


### IS24-CSV {#appendix_glossary_is24_csv}

ist ein Format für den Austausch von Immobiliendaten. Das Format ist veraltet / obsolet und wird von ImmobilienScout24 nicht mehr gepflegt.


### IS24-XML {#appendix_glossary_is24_xml}

ist ein Format für den Austausch von Immobiliendaten. Das Format wird hauptsächlich zum Datenaustausch mit ImmobilienScout24 benötigt. Weitere Informationen finden Sie bei [immobilienscout24.de](http://www.immobilienscout24.de/immobilientransfer/).


### Java {#appendix_glossary_java}

ist die Programmiersprache, welche zu Erstellung des ImmoTools verwendet wurde. Um ein Java-Programm ausführen zu können, muss eine Java-Laufzeitumgebung installiert werden. Weitere Informationen finden Sie bei [java.com](http://java.com/).


### Java-Laufzeitumgebung {#appendix_glossary_java_runtime}

ist eine Sammlung verschiedener Programme & Bibliotheken, um Anwendungen ausführen zu können, die in Java programmiert wurden.


### Kommandozeile {#appendix_glossary_console}

ist ein Eingabebereich für die Steuerung des Betriebssystems. Weitere Informationen finden Sie bei [wikipedia.org](http://de.wikipedia.org/wiki/Kommandozeile).

{{< tip >}}
{{< figure src="terminal_windows-01.jpg" caption="Klicken Sie auf `Start` → `Ausführen...`." >}}

{{< figure src="terminal_windows-02.jpg" caption="Tragen Sie den Befehl `cmd` ein und klicken Sie auf `OK`." >}}

{{< figure src="terminal_windows-03.jpg" caption="Die geöffnete Kommandozeile." >}}
{{< /tip >}}

{{< tip >}}
{{< figure src="terminal_mac-01.jpg" caption="Aus dem `Finder` (im Bereich `Dienstprogramme`) heraus kann das Programm `Terminal` gestartet werden." >}}

{{< figure src="terminal_mac-02.jpg" caption="Eine in Mac OS X geöffnete Kommandozeile." >}}
{{< /tip >}}


### Mehrplatz-Projekt {#appendix_glossary_project_remote}

wird von einem ImmoTool-Server zur Verfügung gestellt, damit mehrere ImmoTool-Anwender innerhalb des Netzwerkes gemeinsam auf dem gleichen Datenbestand arbeiten können. Jeder ImmoTool-Anwender kann eigene Zugriffsrechte in einem Mehrplatz-Projektes besitzen.

Um auf ein Mehrplatz-Projekt zugreifen zu können, muss ein ImmoTool-Server in Betrieb genommen werden.


### OpenEstate-XML {#appendix_glossary_openestate_xml}

ist das vom ImmoTool verwendete Format um Immobiliendaten zu erfassen. Weitere Informationen finden Sie bei [openestate.org](http://openestate.org/).


### OpenImmo-XML {#appendix_glossary_openimmo_xml}

ist ein verbreitetes Format für den Austausch von Immobiliendaten. Weitere Informationen finden Sie bei [openimmo.de](http://openimmo.de/).


### OpenJDK {#appendix_glossary_java_openjdk}

ist eine Java-Laufzeitumgebung unter einer "Open Source Lizenz" auf deren Grundlage Oracle Java erstellt wird. Diese Variante von Java ist besonders verbreitet unter Linux und wird von den meisten Distributionen als Installations-Paket bereitgestellt. Weitere Informationen finden Sie bei [openjdk.java.net](http://openjdk.java.net).


### Oracle Java {#appendix_glossary_java_oracle}

ist eine Java-Laufzeitumgebung, die ursprünglich von [Sun Microsystems](http://de.wikipedia.org/wiki/Sun_Microsystems) entwickelt wurde und mittlerweile von [Oracle](http://www.oracle.com/de/) betreut wird. Die Installations-Pakete von Oracle Java können bei [java.com](http://www.java.com/de/download/manual.jsp) heruntergeladen werden.


### PDF-Dokument {#appendix_glossary_pdf}

ist ein verbreitetes Format zur Speicherung und Weitergabe von Dokumenten. Das ImmoTool kann an verschiedenen Stellen Dateien in diesem Format erzeugen. Weitere Informationen finden Sie bei [wikipedia.org](http://de.wikipedia.org/wiki/Portable_Document_Format).


### PDF-Reader {#appendix_glossary_pdf_reader}

ist ein Programm um PDF-Dokumente auf einem Computer betrachten oder ausdrucken zu können. Eine Übersicht verschiedener frei verfügbarer PDF-Reader finden Sie bei [pdfreaders.org](http://pdfreaders.org/).


### Projekt {#appendix_glossary_project}

enthält die Datenbank mit den im ImmoTool erfassten Daten (Firmendaten, Immobilien, Adressen, etc.). Mit dem ImmoTool können bei Bedarf mehrere Projekte getrennt voneinander verwaltet werden.


### RSS {#appendix_glossary_rss}

ist ein verbreitetes Format für den Austausch von Nachrichten. Viele Webseiten stellen ihre Nachrichten als sogenannter "RSS-Feed" bereit. Weitere Informationen finden Sie bei [wikipedia.org](http://de.wikipedia.org/wiki/RSS).


### SSL {#appendix_glossary_ssl}

ist eine weit verbreitete Form der Verschlüsselung und wird vom ImmoTool an verschiedenen Stellen unterstützt:

-   Die Kommunikation zwischen ImmoTool & ImmoTool-Server kann bei Bedarf mit Hilfe von SSL verschlüsselt werden.

-   Der Zugriff auf Internet-Adressen kann bei Bedarf über SSL-Verschlüsselung erfolgen - zumindest wenn der jeweilige Webseiten-Betreiber auch einen Zugriff über Adressen mit `https://` gestattet.

-   Der Zugriff auf E-Mailkonten sowie der Versand von E-Mails kann bei Bedarf über SSL-Verschlüsselung erfolgen - zumindest wenn der jeweilige E-Mailanbieter dies unterstützt.

Weitere Informationen finden Sie bei [Wikipedia](http://de.wikipedia.org/wiki/Transport_Layer_Security).


### SSL-Schlüssel {#appendix_glossary_ssl_key}

wird bei einer SSL-Verschlüsselung benötigt, um versendete Daten zu verschlüsseln und empfangene Daten zu entschlüsseln.

Bei SSL handelt es sich um eine [asymmetrische Verschlüsselung](http://de.wikipedia.org/wiki/Asymmetrisches_Kryptosystem). Genau genommen werden dabei zwei Schlüssel erzeugt (privater und öffentlicher Schlüssel), weshalb oft auch von einem “Schlüsselpaar” die Rede ist.


### SSL-Zertifikat {#appendix_glossary_ssl_certificate}

wird bei einer SSL-Verschlüsselung verwendet, um die Authentizität und Integrität der beiden Kommunikationspartner sicherzustellen. Weitere Informationen finden Sie bei [Wikipedia](http://de.wikipedia.org/wiki/Digitales_Zertifikat).


### TAR.GZ-Archiv {#appendix_glossary_targz}

ist ein Format zur Komprimierung von Dateien. Mehrere Dateien werden dabei zu einer platzsparenden TAR.GZ-Datei zusammengefasst. Das Format wird hauptsächlich unter Mac, Linux & Unix verwendet. Weitere Informationen finden Sie bei [wikipedia.org](http://de.wikipedia.org/wiki/Tar).

{{< tip >}}
Windows kann TAR.GZ-Dateien nicht direkt entpacken. Hier sind externe Programme nötig, wie z.B.: [7-Zip](http://www.7-zip.de/), [WinZIP](http://www.winzip.de/) oder [WinRAR](http://www.winrar.de/).
{{< /tip >}}

{{< tip >}}
Nachdem ein TAR-GZ-Archiv heruntergeladen wurden, entpackt Mac OS X dies in der Regel automatisch.

Um eine TAR.GZ-Datei zu entpacken, klicken Sie im `Finder` mit der rechten Maustaste auf die Datei und wählen Sie `Öffnen mit Archivprogramm / BOMArchiveHelper`.

{{< figure src="extract_archive_mac-01.jpg" caption="Hilfsprogramm zum Entpacken einer TAR.GZ-Datei" >}}

Alternativ kann auf externe Programme wie [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html) zurückgegriffen werden.
{{< /tip >}}

{{< tip >}}
Die grafischen Oberflächen (KDE, Gnome, etc.) stellen in der Regel Programme zum Entpacken von TAR.GZ-Dateien bereit. Meist können die Dateien über das Kontextmenü (rechte Maustaste) entpackt werden. Alternativ kann ein TAR.GZ-Archiv (z.B. OpenEstate-ImmoTool-1.0.tar.gz) über die Kommandozeile mit folgendem Befehl entpackt werden:

```bash
tar xfvz OpenEstate-ImmoTool-1.0.tar.gz
```
{{< /tip >}}

{{< info >}}
Ältere Version des TAR-Programmes unterstützen aus historischen Gründen keine Pfadnamen mit mehr als 100 Zeichen. Die im OpenEstate-Projekt bereitgestellten TAR.GZ-Archive können dieses Limit jedoch überschreiten. Neuere Versionen des TAR-Programmes (z.B. [GNU Tar](http://www.gnu.org/software/tar/)) sind nicht von dem Problem betroffen.
{{< /info >}}


### Teilabgleich {#appendix_glossary_transfer_incremental}

ist ein Export-Modus für Immobiliendaten bei dem nur die zwischenzeitlich geänderten Immobilien exportiert werden. Für zwischenzeitlich gelöschte Immobilien wird ein expliziter Auftrag zur Löschung exportiert.

Bei Exporten im Teilabgleich besteht der Vorteil, dass weniger Daten zum Empfänger gesendet werden müssen. In der Regel sind Exporte im Teilabgleich deshalb schneller als beim Vollabgleich.


### Verschlüsselung {#appendix_glossary_encryption}

wird bei der Übertragung von Daten zwischen mehreren Computern verwendet um sicherzustellen,

1.  dass die übertragenen Informationen von einem Außenstehenden nicht mitgelesen oder manipuliert werden können ([Integrität](http://de.wikipedia.org/wiki/Integrit%C3%A4t_%28Informationssicherheit%29)).

2.  dass die richtigen Computer miteinander kommunizieren (Schutz vor [Man-in-the-middle-Angriff](http://de.wikipedia.org/wiki/Man-in-the-middle-Angriff)).

Das ImmoTool unterstützt die weit verbreitete [SSL-Verschlüsselung](#appendix_glossary_ssl).


### Vollabgleich {#appendix_glossary_transfer_full}

ist ein Export-Modus für Immobiliendaten bei dem alle aktuell veröffentlichten Immobilien exportiert werden. Der Empfänger löscht dabei alle Immobiliendaten, die nicht in der Export-Datei vorhanden sind.

Bei Exporten im Vollabgleich besteht der Vorteil, dass bei jedem Exportvorgang alle Daten mit dem Empfänger synchronisiert werden. Das Risiko von Problemen bei der Synchronisation zwischen Absender und Empfänger ist bei Exporten im Vollabgleich geringer, da grundsätzlich alle Daten übermittelt werden.


### Web-Browser {#appendix_glossary_web_browser}

ist ein Programm zur Darstellung von Internetseiten. Auf den meisten Betriebssystemen sollte bereits ein Web-Browser installiert sein. Verbreitete Web-Browser sind [Mozilla Firefox](http://www.mozilla.com/firefox), [Opera](http://www.opera.com/), [Safari](http://www.apple.com/de/safari/), [Google Chrome](http://www.google.com/chrome/) & [Internet Explorer](http://www.microsoft.com/germany/windows/internet-explorer/).


### ZIP-Archiv {#appendix_glossary_zip}

ist ein Format zur Komprimierung von Dateien. Mehrere Dateien werden dabei zu einer platzsparenden ZIP-Datei zusammengefasst. Das Format wird unter Windows-Betriebssystemen verwendet. Weitere Informationen finden Sie bei [wikipedia.org](http://de.wikipedia.org/wiki/ZIP_%28Dateiformat%29).

{{< tip >}}
Neuere Windows-Versionen liefern bereits Funktionen zum Entpacken von ZIP-Dateien mit. Alternativ kann auf Programme wie [7-Zip](http://www.7-zip.de/), [WinZIP](http://www.winzip.de/) oder [WinRAR](http://www.winrar.de/) zurückgegriffen werden.
{{< /tip >}}

{{< tip >}}
Nachdem ein ZIP-Archiv heruntergeladen wurden, entpackt Mac OS X dies in der Regel automatisch.

Um eine ZIP-Datei von Hand zu entpacken, klicken Sie im `Finder` mit der rechten Maustaste auf die ZIP-Datei und wählen Sie `Öffnen mit Archivprogramm / BOMArchiveHelper`.

{{< figure src="extract_archive_mac-01.jpg" caption="Hilfsprogramm zum Entpacken einer ZIP-Datei" >}}

Alternativ kann auf externe Programme wie [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html) zurückgegriffen werden.
{{< /tip >}}

{{< tip >}}
Die grafischen Oberflächen (KDE, Gnome, etc.) stellen in der Regel Programme zum Entpacken von ZIP-Dateien bereit. Meist können die Dateien über das Kontextmenü (rechte Maustaste) entpackt werden. Alternativ kann ein ZIP-Archiv (z.B. OpenEstate-ImmoTool-1.0.zip) über die Kommandozeile mit folgendem Befehl entpackt werden:

```bash
unzip OpenEstate-ImmoTool-1.0.zip
```
{{< /tip >}}
