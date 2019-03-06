---

title: Installing Java 
linktitle: Install Java
description: Integration of Java into OpenEstate-ImmoTool & OpenEstate-ImmoServer…
weight: 70

menu:
  main:
    parent: intro
    identifier: intro-java

---

## Installing Java {#intro_java}

ImmoTool and ImmoTool-Server have been written in the Java programming language. In order to use the software a Java runtime environment (so called JRE) is required.

{{< info >}}
The provided installation packages of ImmoTool and ImmoTool-Server already contain the required Java runtime environment. In most cases it is **not necessary** to install Java separately.
{{< /info >}}

There are only a few reasons not to use the Java version provided in the installation packages. It might be required, if a Linux system is used, for which no official installation package is available. For these rare cases the documentation below describes the steps to use a custom Java runtime environment.

{{< warning >}}
Please consider, that OpenEstate can only give limited support for custom / external Java installations. We are trying to maintain compatibility to our best knowledge and belief. But we can not fully rule out possible errors or problems regarding custom Java installations. 
{{< /warning >}}

By default each application contains a folder called **`jre`**, that contains the provided Java runtime environment. This folder may be replaced with a custom Java installation.


### Using Java from a third-party supplier {#intro_java_extern}

Many third-party suppliers are providing Java or OpenJDK packages (e.g. [AdoptOpenJDK](https://adoptopenjdk.net/), [Azul Systems](https://www.azul.com/downloads/zulu/), [BellSoft](https://www.bell-sw.com/), [JetBrains](https://bintray.com/jetbrains/intellij-jdk), [Red Hat](https://github.com/ojdkbuild/ojdkbuild), [SAP](https://sap.github.io/SapMachine/) or [Oracle](https://www.java.com/)). You may use their packages by following these steps:

-   Remove the **`jre`** folder from the application directory of ImmoTool / ImmoTool-Server.
-   Extract the archive, that you have downloaded from the third-party supplier.
-   Rename the extracted folder into **`jre`** and copy it into the application directory of ImmoTool / ImmoTool-Server.


### Using Java from the Linux package system {#intro_java_linux}

Most Linux distributions also provide Java / OpenJDK through their package system. You may use their packages by following these steps:

-   Remove the **`jre`** folder from the application directory of ImmoTool / ImmoTool-Server.
-   Install the OpenJDK package of your Linux distributions - e.g. via:

    ```bash
    sudo apt install openjdk-11-jdk
    ```   

If the **`jre`** folder is not present in the application directory, the application will automatically try to use the installed OpenJDK package on startup.
