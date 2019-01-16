---

title: Installation von Java
linktitle: Java
description: Installation von Java für OpenEstate-ImmoTool…
weight: 40

menu:
  main:
    parent: intro
    identifier: intro-java

---

## Java installieren {#intro_java_install}

Java wird sowohl für das ImmoTool als auch für den ImmoTool-Server benötigt und muss vorab auf allen verwendeten Rechnern installiert werden.

> **Hinweis**
>
> Die Programme können entweder mit **Oracle Java** oder **OpenJDK** betrieben werden. Wir raten von der Verwendung anderer Java-Laufzeitumgebungen ab.

Abhängig vom verwendeten Betriebssystem sind unterschiedliche Vorgehensweisen nötig um Java zu installieren.


### Java unter Windows installieren {#intro_java_install_windows}

Von der Webseite [java.com](http://java.com/de/download/manual.jsp) können Sie Oracle Java kostenlos für Ihr **Windows**-Betriebssystem herunterladen. Es ist empfohlen, das Paket **Windows Offline** herunterzuladen. Starten Sie die heruntergeladene EXE-Datei mit einem Doppelklick um die Installation zu beginnen.

> **Hinweis**
>
> Unter [java.com](http://java.com/de/download/help/windows_offline_download.xml) wird die Installation von Oracle Java unter Windows etwas ausführlicher beschrieben.


### Java unter Mac OS X installieren {#intro_java_install_mac}

Von der Webseite [java.com](http://java.com/de/download/manual.jsp) können Sie Oracle Java kostenlos für Ihr **Mac**-Betriebssystem herunterladen. Nachdem die Datei heruntergeladen wurde, öffnet sich in den meisten Fällen automatisch ein Fenster mit dem Inhalt der DMG-Datei. Andernfalls können Sie per Doppelklick die DMG-Datei als Laufwerk einbinden und aus dem Finder heraus die Installation starten.

> **Hinweis**
>
> Unter [java.com](http://java.com/de/download/help/mac_install.xml) wird die Installation von Oracle Java unter Mac OS X etwas ausführlicher beschrieben.


### Java unter Linux installieren {#intro_java_install_linux}

In der Regel stellen die Distributoren eigene Pakete für OpenJDK 7 zur Verfügung. Es ist ratsam diese Pakete zu installieren, da sich Java auf diesem Wege besser in das Betriebssystem integriert, Aktualisierungen können über das Paketsystem installiert werden und keine weiteren Anpassungen an den Pfaden sind nötig.


#### OpenJDK 7 unter Debian, Ubuntu, Linux Mint, etc. {#intro_java_install_linux_debian}

Öffnen Sie die Konsole und führen Sie den folgenden Befehl aus:

```
sudo apt-get install openjdk-7-jre
```


#### OpenJDK 7 unter Fedora, Oracle Linux, Red Hat Enterprise Linux, etc. {#intro_java_install_linux_fedora}

Öffnen Sie die Konsole und führen Sie den folgenden Befehl aus:

```
su -c "yum install java-1.7.0-openjdk"
```

#### OpenJDK 7 unter Arch Linux {#intro_java_install_linux_arch}

Öffnen Sie die Konsole und führen Sie den folgenden Befehl aus:

```
sudo pacman -S jre7-openjdk
```


## Java-Installation testen {#intro_java_test}


### Java per Eingabeaufforderung testen {#intro_java_test_shell}

Öffnen Sie im Betriebssystem die Eingabeaufforderung / die Konsole / das Terminal und führen Sie den folgenden Befehl aus:

```
java -version
```

Nach Ausführung des Befehls sollte die Version der Java-Installation wie folgt dargestellt werden:

{{< figure src="java_check_terminal-01.jpg" caption="Ausgabe der Java-Version" >}}


### Java per Systemsteuerung testen {#intro_java_test_controlpanel}

Nachdem Java auf Ihrem **Windows**-Betriebssystem installiert wurde, finden Sie in der Systemsteuerung dieses zusätzliche Symbol:

{{< figure src="java_check_windows-01.jpg" caption="Java-Symbol in der Systemsteuerung" >}}


Bei Doppelklick auf das Java-Symbol in der Systemsteuerung öffnet sich ein Fenster mit diversen Informationen zur aktuellen Java-Installation:

{{< figure src="java_check_windows-02.jpg" caption="Informationen zur Java-Installation" >}}

Klicken Sie in diesem Fenster auf `Anwendungsinfo...` um ausführlichere Informationen zur aktuell installierten Java-Version dargestellt zu bekommen. Daraufhin öffnet sich das folgende Fenster, aus dem Sie die Version des aktuell installierten Java entnehmen können:

{{< figure src="java_check_windows-03.jpg" caption="Version der Java-Installation" >}}
