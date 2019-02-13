---

title: ImmoTool herunterladen
linktitle: Herunterladen
description: Wie OpenEstate-ImmoTool heruntergeladen werden kann…
weight: 30

menu:
  main:
    parent: intro
    identifier: intro-download

---

## Programme herunterladen {#intro_download}


### Pakete von der Webseite beziehen {#intro_download_website}

ImmoTool & ImmoTool-Server können auf der OpenEstate-Webseite in verschiedenen Paketen heruntergeladen werden. Ältere Versionen der Programme sind ebenfalls an dieser Stelle verfügbar.

Für beide Programme stehen folgende Pakete im zur Verfügung: 

-   Für Windows 64bit & 32bit stehen separate **EXE**-Installationsdateien zur Verfügung.
-   Für macOS steht eine **DMG**-Installationsdatei zur Verfügung.
-   Für Debian-basierte Linux-Distributionen (z.B. **Debian**, **Ubuntu** oder **Linux Mint**) steht eine **DEB**-Installationsdatei zur Verfügung.
-   Für andere Linux-Distributionen steht eine **TAR.GZ**-Datei zur Verfügung.


### Pakete aus Debian-Repository beziehen {#intro_download_debian}

Anwender von Debian-basierten Linux-Distributionen (z.B. **Debian**, **Ubuntu** oder **Linux Mint**) können alternativ zum direkten Download auch das [bereitgestellte Repository](https://debian.openestate.org/) in ihr Betriebssystem integrieren. Dies erleichtert die Installation und Aktualisierungen können gemeinsam mit den Betriebssystem-Aktualisierungen installiert werden.

Zur Integration des Repositories ins Betriebssystem ist wie folgt vorzugehen:

1.  PGP-Schlüssel importieren via

    ```bash
    wget -qO - \
      https://debian.openestate.org/conf/debian.gpg.key \ 
      | sudo apt-key add -
    ```

2.  Folgende Zeile am Ende der Datei `/etc/apt/sources.list` eintragen:

    ```
    deb [arch=amd64] https://debian.openestate.org/ openestate main
    ```
    
3.  Pakete aktualisieren via:

    ```bash
    sudo apt update
    ```
    
4.  Danach kann das ImmoTool installiert werden mit dem Befehl:

    ```bash
    sudo apt install openestate-immotool
    ```
    
    Bzw. der ImmoTool-Server kann installiert werden mit dem Befehl: 
    
    ```bash
    sudo apt install openestate-immoserver
    ```

---

> **Hinweis:**
>
> Sollte es bei der Paket-Aktualisierung in Schritt 3 zu einer Fehlermeldung kommen, muss ggf. noch das Paket `apt-transport-https` über folgenden Befehl installiert werden:
>
> ```bash
> sudo apt install apt-transport-https
> ```
