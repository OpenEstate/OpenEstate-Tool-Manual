---

title: System requirements
linktitle: Requirements
description: About the system requirements of OpenEstate-ImmoTool & OpenEstate-ImmoServer…
weight: 20

menu:
  main:
    parent: intro
    identifier: intro-requirements

---

## System requirements {#intro_requirements}

ImmoTool and ImmoTool-Server may be used on all kinds of operating systems as long as they are fairly up to date and Java / OpenJDK is available for it in the required version. 


### Requirements of ImmoTool {#intro_requirements_client}

-   **Operating system:**
    -   Windows (from version 7 onwards; 32bit / 64bit)
    -   macOS (from version 10.9 onwards)
    -   Linux (x86 aka IA-32 / x86-64 aka amd64)
-   **Processor:**
    2 GHZ (the more the merrier)
-   **RAM:**
    512 MB are used by the application at maximum
-   **Hard drive space:**
    approx. 150 MB after installation; more space is required depending on the amount of data
-   **Java:**
    version 11 (already provided in the installation package)
-   **Internet access:**
    not necessary, but helpful

{{< info >}}
There are no installation packages available for Linux systems on other architectures than **x86** and **x86-64**. But you may still be able to run ImmoTool, if the Linux distribution provides an OpenJDK 11 package for the architecture being used (see ["Using Java from the Linux package system"]({{< relref "java.md#intro_java_linux" >}})).
{{< /info >}} 


### Requirements of ImmoTool-Server {#intro_requirements_server}

-   **Operating system:**
    -   Windows (from version 7 onwards; 32bit / 64bit)
    -   macOS (from version 10.9 onwards)
    -   Linux (x86 aka IA-32 / x86-64 aka amd64)
-   **Prozessor:**
    1 GHZ (the more the merrier)
-   **RAM:**
    512 MB are used by the application at maximum
-   **Hard drive space:**
    approx. 150 MB after installation; more space is required depending on the amount of data
-   **Java:**
    version 8 at least; version 11 is recommended (already provided in the installation package)
-   **Internet access:**
    not necessary

{{< info >}}
There are no installation packages available for Linux systems on other architectures than **x86** and **x86-64**. But you may still be able to run ImmoTool-Server, if the Linux distribution provides an OpenJDK 8 package (or newer) for the architecture being used (see ["Using Java from the Linux package system"]({{< relref "java.md#intro_java_linux" >}})).
{{< /info >}} 
