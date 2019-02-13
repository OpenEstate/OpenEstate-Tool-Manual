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

ImmoTool und ImmoTool-Server wurden in der Programmiersprache Java entwickelt. Um die Software nutzen zu können, muss eine Java-Laufzeitumgebung (kurz JRE) vorhanden sein.

{{< warning >}}
Die Installationspakete von ImmoTool und ImmoTool-Server enthalten bereits die benötigte Java-Laufzeitumgebung. Im Normalfall muss daher Java **nicht** zusätzlich auf dem Rechner installiert werden.
{{< /warning >}}


### Java unter Windows installieren {#intro_java_install_windows}

In den Installationspaketen für Windows ist Java bereits enthalten. Es ist daher in der Regel **nicht** nötig, die Java-Laufzeitumgebung (JRE) manuell zu installieren. 

Sollten Sie dennoch Java manuell installieren wollen, so können Sie das JRE-Paket von [AdoptOpenJDK](https://adoptopenjdk.net/) beziehen und [dieser Anleitung](https://adoptopenjdk.net/installation.html?variant=openjdk11&jvmVariant=hotspot) folgen.


### Java unter macOS installieren {#intro_java_install_mac}

Im Installationspaket für macOS ist Java bereits enthalten. Es ist daher in der Regel **nicht** nötig, die Java-Laufzeitumgebung (JRE) manuell zu installieren.

Sollten Sie dennoch Java manuell installieren wollen, so können Sie das JRE-Paket von [AdoptOpenJDK](https://adoptopenjdk.net/) beziehen und [dieser Anleitung](https://adoptopenjdk.net/installation.html?variant=openjdk11&jvmVariant=hotspot) folgen.


### Java unter Linux installieren {#intro_java_install_linux}

In den Installationspaketen für Linux (x86-64 bzw. amd64) ist Java bereits enthalten. Es ist daher in der Regel **nicht** nötig, die Java-Laufzeitumgebung (JRE) manuell zu installieren. 

Sollten Sie eine andere Architektur als x86-64 (bzw. amd64) nutzen oder aus anderen Gründen ein eigenes Java nutzen wollen, so können Sie entweder

-   das Paket von OpenJDK 11 aus dem Paketsystem Ihrer Linux-Distribution heraus installieren oder
-   das JRE-Paket von [AdoptOpenJDK](https://adoptopenjdk.net/) beziehen und [dieser Anleitung](https://adoptopenjdk.net/installation.html?variant=openjdk11&jvmVariant=hotspot) folgen.


## Eigenes Java verwenden {#intro_java_custom}

Standardmäßig wird beim Programmstart im Programmverzeichnis nach einem Ordner namens `jre` gesucht. In diesem Ordner sollte die Java-Laufzeitumgebung enthalten sein.


### Java von AdoptOpenJDK verwenden {#intro_java_custom_extern}

-   Löschen Sie den Ordner `jre` aus dem Programmverzeichnis von ImmoTool / ImmoTool-Server.
-   Entpacken Sie das von [AdoptOpenJDK](https://adoptopenjdk.net/) heruntergeladene Archiv.
-   Kopieren Sie den entpackten Ordner unter dem Namen `jre` ins Programmverzeichnis. 


### Java aus Linux-Paketsystem verwenden {#intro_java_custom_linux}

-   Löschen Sie den Ordner `jre` aus dem Programmverzeichnis von ImmoTool / ImmoTool-Server.
-   Installieren Sie das OpenJDK 11 Paket von Ihrer Distribution im Betriebssystem - z.B. via:

    ```bash
    sudo apt install openjdk-11-jre
    ```   
