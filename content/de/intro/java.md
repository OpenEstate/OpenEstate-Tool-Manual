---

title: Installation von Java 
linktitle: Java installieren
description: Installation von Java für OpenEstate-ImmoTool & OpenEstate-ImmoServer…
weight: 70

menu:
  main:
    parent: intro
    identifier: intro-java

---

## Java installieren {#intro_java}

ImmoTool und ImmoTool-Server wurden in der Programmiersprache Java entwickelt. Um die Software nutzen zu können, muss eine Java-Laufzeitumgebung (kurz JRE) vorhanden sein.

{{< info >}}
Die Installationspakete von ImmoTool und ImmoTool-Server enthalten bereits die benötigte Java-Laufzeitumgebung. Im Normalfall muss daher Java **nicht** zusätzlich auf dem Rechner installiert werden.
{{< /info >}}

Es gibt nur wenige Gründe, eine andere als die in den Installationspaketen bereitgestellte Java-Version zu verwenden. Derzeit ist dieser Schritt eigentlich nur nötig, wenn man die Software unter einem Linux-System auf einer anderen Architektur als x86-64 (bzw. amd64) nutzen will. Für diese seltenen Fälle werden die nötigen Schritte zur Verwendung einer eigenen Java-Version im Folgenden kurz dokumentiert. 

{{< warning >}}
Beachten Sie bitte, dass OpenEstate nur eingeschränkte Hilfestellungen geben kann, wenn ein eigenes / externes Java verwendet wird. Wir bemühen uns zwar nach bestem Wissen und Gewissen eine bestmögliche Kompatibilität herzustellen, können aber nicht ausschließen, dass vereinzelt Fehler oder Probleme auftreten.
{{< /warning >}}

Standardmäßig wird beim Programmstart im Programmverzeichnis nach einem Ordner namens **`jre`** gesucht. In diesem Ordner sollte die Java-Laufzeitumgebung enthalten sein.


### Java von Drittanbieter verwenden {#intro_java_extern}

Java bzw. OpenJDK kann von verschiedenen Drittanbietern bezogen werden (z.B. [AdoptOpenJDK](https://adoptopenjdk.net/), [Azul Systems](https://www.azul.com/downloads/zulu/), [BellSoft](https://www.bell-sw.com/), [JetBrains](https://bintray.com/jetbrains/intellij-jdk), [Red Hat](https://github.com/ojdkbuild/ojdkbuild), [SAP](https://sap.github.io/SapMachine/) oder [Oracle](https://www.java.com/)). Die Vorgehensweise zur Verwendung dieser Java-Versionen ist wie folgt: 

-   Löschen Sie den Ordner **`jre`** aus dem Programmverzeichnis von ImmoTool / ImmoTool-Server.
-   Entpacken Sie das vom Drittanbieter Ihrer Wahl heruntergeladene Archiv.
-   Kopieren Sie den entpackten Ordner unter dem Namen **`jre`** ins Programmverzeichnis. 


### Java aus Linux-Paketsystem verwenden {#intro_java_linux}

Die meisten Linux-Distributionen stellen ebenfalls Java bzw. OpenJDK über ihr Paketsystem zur Verfügung. Die Vorgehensweise zur Verwendung dieser Java-Versionen ist wie folgt:

-   Löschen Sie den Ordner **`jre`** aus dem Programmverzeichnis von ImmoTool / ImmoTool-Server.
-   Installieren Sie das OpenJDK-JRE Paket von Ihrer Linux-Distribution - z.B. via:

    ```bash
    sudo apt install openjdk-11-jre
    ```   
