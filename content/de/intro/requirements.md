---

title: Systemanforderungen
linktitle: Anforderungen
description: Über die Systemanforderungen von OpenEstate-ImmoTool & OpenEstate-ImmoServer…
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
    -   Linux (x86 bzw. IA-32 / x86-64 bzw. amd64)
-   **Prozessor:**
    2 GHZ (je mehr, desto besser)
-   **Arbeitsspeicher:**
    512 MB werden vom Programm maximal belegt
-   **Festplattenspeicher:**
    ca. 150 MB nach Installation; abhängig vom Datenbestand wird weiterer Speicherplatz benötigt
-   **Java:**
    Version 11 (ist im Installationspaket bereits enthalten)
-   **Internetzugang:**
    nicht nötig, aber hilfreich

{{< info >}}
Für Linux auf anderen Architekturen als **x86** oder **x86-64** stehen keine Installationspakete zur Verfügung. Das ImmoTool kann jedoch dennoch darunter betrieben werden, wenn OpenJDK 11 von der Linux-Distribution für diese Architektur bereit gestellt wird (siehe ["Java aus Linux-Paketsystem verwenden"]({{< relref "java.md#intro_java_linux" >}})).
{{< /info >}} 


### Anforderungen von ImmoTool-Server {#intro_requirements_server}

-   **Betriebssystem:**
    -   Windows (ab Version 7; 32bit / 64bit)
    -   macOS (ab Version 10.9)
    -   Linux (x86 bzw. IA-32 / x86-64 bzw. amd64)
-   **Prozessor:**
    1 GHZ (je mehr, desto besser)
-   **Arbeitsspeicher:**
    512 MB werden vom Programm maximal belegt
-   **Festplattenspeicher:**
    ca. 150 MB nach Installation; abhängig vom Datenbestand wird weiterer Speicherplatz benötigt
-   **Java:**
    Version 8 mindestens; Version 11 empfohlen (ist im Installationspaket bereits enthalten)
-   **Internetzugang:**
    nicht benötigt

{{< info >}}
Für Linux auf anderen Architekturen als **x86** oder **x86-64** stehen keine Installationspakete zur Verfügung. Der ImmoTool-Server kann jedoch dennoch darunter betrieben werden, wenn OpenJDK 8 (oder neuer) von der Linux-Distribution für diese Architektur bereit gestellt wird (siehe ["Java aus Linux-Paketsystem verwenden]({{< relref "java.md#intro_java_linux" >}})).
{{< /info >}}
