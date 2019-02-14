---

title: Installation von Java 
linktitle: Java installieren
description: Installation von Java für OpenEstate-ImmoTool…
weight: 70

menu:
  main:
    parent: intro
    identifier: intro-java

---

## Java installieren {#intro_java_install}

ImmoTool und ImmoTool-Server wurden in der Programmiersprache Java entwickelt. Um die Software nutzen zu können, muss eine Java-Laufzeitumgebung (kurz JRE) vorhanden sein.

{{< info >}}
Die Installationspakete von ImmoTool und ImmoTool-Server enthalten bereits die benötigte Java-Laufzeitumgebung. Im Normalfall muss daher Java **nicht** zusätzlich auf dem Rechner installiert werden.
{{< /info >}}


### Java unter Windows installieren {#intro_java_install_windows}

In den Installationspaketen für Windows ist Java bereits enthalten. Es ist daher in der Regel **nicht** nötig, die Java-Laufzeitumgebung (JRE) manuell zu installieren. 

Sollten Sie dennoch Java manuell installieren wollen, so können Sie das **JRE**-Paket von einem Drittanbieter beziehen und den Hinweisen im Abschnitt ["Eigenes Java verwenden"]({{< relref "java.md#intro_java_custom" >}}) folgen.


### Java unter macOS installieren {#intro_java_install_mac}

Im Installationspaket für macOS ist Java bereits enthalten. Es ist daher in der Regel **nicht** nötig, die Java-Laufzeitumgebung (JRE) manuell zu installieren.

Sollten Sie dennoch Java manuell installieren wollen, so können Sie das **JRE**-Paket von einem Drittanbieter beziehen und den Hinweisen im Abschnitt ["Eigenes Java verwenden"]({{< relref "java.md#intro_java_custom" >}}) folgen.


### Java unter Linux installieren {#intro_java_install_linux}

In den Installationspaketen für Linux (x86-64 bzw. amd64) ist Java bereits enthalten. Es ist daher in der Regel **nicht** nötig, die Java-Laufzeitumgebung (JRE) manuell zu installieren. 

Sollten Sie eine andere Architektur als x86-64 (bzw. amd64) nutzen oder aus anderen Gründen ein eigenes Java nutzen wollen, so können Sie entweder

-   das Paket von OpenJDK 11 aus dem Paketsystem Ihrer Linux-Distribution heraus installieren oder
-   das **JRE**-Paket von einem Drittanbieter beziehen und den Hinweisen im Abschnitt ["Eigenes Java verwenden"]({{< relref "java.md#intro_java_custom" >}}) folgen.


## Eigenes Java verwenden {#intro_java_custom}

Standardmäßig wird beim Programmstart im Programmverzeichnis nach einem Ordner namens `jre` gesucht. In diesem Ordner sollte die Java-Laufzeitumgebung enthalten sein.

{{< warning >}}
Beachten Sie bitte, dass OpenEstate nur eingeschränkte Hilfestellungen geben kann, wenn ein eigenes / externes Java verwendet wird. Wir bemühen uns zwar nach bestem Wissen und Gewissen eine bestmögliche Kompatibilität herzustellen, können aber nicht ausschließen, dass vereinzelt Fehler oder Probleme auftreten.
{{< /warning >}}


### Java von Drittanbieter verwenden {#intro_java_custom_extern}

Java 11 bzw. OpenJDK 11 kann von verschiedenen Drittanbietern bezogen werden (z.B. [AdoptOpenJDK](https://adoptopenjdk.net/), [Azul Systems](https://www.azul.com/downloads/zulu/) oder [Oracle](https://www.java.com/)). Die Vorgehensweise zur Verwendung dieser Java-Versionen ist wie folgt: 

-   Löschen Sie den Ordner `jre` aus dem Programmverzeichnis von ImmoTool / ImmoTool-Server.
-   Entpacken Sie das vom Drittanbieter Ihrer Wahl heruntergeladene Archiv.
-   Kopieren Sie den entpackten Ordner unter dem Namen `jre` ins Programmverzeichnis. 


### Java aus Linux-Paketsystem verwenden {#intro_java_custom_linux}

Die meisten Linux-Distributionen stellen ebenfalls Java 11 bzw. OpenJDK 11 über ihr Paketsystem zur Verfügung. Die Vorgehensweise zur Verwendung dieser Java-Versionen ist wie folgt:

-   Löschen Sie den Ordner `jre` aus dem Programmverzeichnis von ImmoTool / ImmoTool-Server.
-   Installieren Sie das OpenJDK 11 Paket von Ihrer Distribution im Betriebssystem - z.B. via:

    ```bash
    sudo apt install openjdk-11-jre
    ```   
