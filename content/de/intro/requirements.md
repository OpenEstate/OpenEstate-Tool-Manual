---

title: Systemanforderungen
linktitle: Anforderungen
description: Die Systemanforderungen von OpenEstate-ImmoTool…
weight: 20

menu:
  main:
    parent: intro
    identifier: intro-requirements

---

## Systemanforderungen {#intro_requirements}

ImmoTool und ImmoTool-Server können auf verschiedensten Systemen betrieben werden solange diese einigermaßen aktuell sind und Java / OpenJDK in der jeweils benötigten Version dafür zur Verfügung steht.


### Anforderungen von ImmoTool {#intro_requirements_client}

-   **Betriebssystem:**
    -   Windows (ab Version 7; 32bit / 64bit)
    -   macOS (ab 10.9)
    -   Linux (x86-64 bzw. amd64)
-   **Prozessor:**
    2 GHZ (je mehr desto besser)
-   **Arbeitsspeicher:**
    512 MB werden vom Programm maximal belegt
-   **Festplattenspeicher:**
    ca. 150 MB nach Installation; abhängig vom Datenbestand wird weiterer Speicherplatz benötigt
-   **Java:**
    Version 11 (ist im Installationspaket bereits enthalten)
-   **Internetzugang:**
    nicht nötig, aber hilfreich

{{< info >}}
Für Linux auf **x86** (auch "i686" oder "i386" genannt) und andere Architekturen stehen keine Installationspakete zur Verfügung. Das Programm kann jedoch dennoch darunter betrieben werden, wenn OpenJDK 11 von der Linux-Distribution für diese Architektur bereit gestellt wird (siehe [Java unter Linux installieren]({{< relref "java.md#intro_java_install_linux" >}})).
{{< /info >}} 


### Anforderungen von ImmoTool-Server {#intro_requirements_server}

-   **Betriebssystem:**
    -   Windows (ab Version 7; 32bit / 64bit)
    -   macOS (ab Version 10.9)
    -   Linux (x86-64 bzw. amd64)
-   **Prozessor:**
    1 GHZ (je mehr desto besser)
-   **Arbeitsspeicher:**
    512 MB werden vom Programm maximal belegt
-   **Festplattenspeicher:**
    ca. 150 MB nach Installation; abhängig vom Datenbestand wird weiterer Speicherplatz benötigt
-   **Java:**
    Version 8 (ist im Installationspaket bereits enthalten)
-   **Internetzugang:**
    nicht benötigt

{{< info >}}
Für Linux auf **x86** (auch "i686" oder "i386" genannt) und andere Architekturen stehen keine Installationspakete zur Verfügung. Das Programm kann jedoch dennoch darunter betrieben werden, wenn OpenJDK 11 von der Linux-Distribution für diese Architektur bereit gestellt wird (siehe [Java unter Linux installieren]({{< relref "java.md#intro_java_install_linux" >}})).
{{< /info >}}
