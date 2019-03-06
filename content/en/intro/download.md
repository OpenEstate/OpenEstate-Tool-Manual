---

title: Download the applications
linktitle: Download
description: How to download OpenEstate-ImmoTool & OpenEstate-ImmoServer…
weight: 30

menu:
  main:
    parent: intro
    identifier: intro-download

---

## Download the applications {#intro_download}


### Obtain packages from the website {#intro_download_website}

ImmoTool and ImmoTool-Server are available for download at the [OpenEstate website](https://openestate.org/downloads/) in different packages. Older versions of the applications are also available here.

The following packages are provided for both applications: 

-   For Windows there are **EXE** installers available (32bit / 64bit).
-   For macOS there is a **DMG** installation image available.
-   For Debian based Linux distributions (e.g. **Debian**, **Ubuntu** or **Linux Mint**) there are different **Debian packages** available (**DEB** installation file).
-   For other Linux systems there are different **TAR.GZ** files available.


### Obtain packages from the Debian repository {#intro_download_debian}

As an alternative for a direct download from the website we provide a [Debian repository](https://debian.openestate.org/), that may be used for all Debian based Linux distributions (e.g. **Debian**, **Ubuntu** or **Linux Mint**). Using the repository results in a better integration into the package management of the operating system and allows easier installation / updates.

Follow these steps in order to integrate the Debian repository into your operating system:

1.  Import the PGP key via:

    ```bash
    wget -qO - \
      https://debian.openestate.org/conf/debian.gpg.key \ 
      | sudo apt-key add -
    ```

2.  Add the following line to the end of the file **`/etc/apt/sources.list`**:

    ```
    deb https://debian.openestate.org/ openestate main
    ```
    
3.  Update the package index via:

    ```bash
    sudo apt update
    ```
    
4.  Afterwards you can install ImmoTool via:

    ```bash
    sudo apt install openestate-immotool
    ```
    
    Or you can install ImmoTool-Server via: 
    
    ```bash
    sudo apt install openestate-immoserver
    ```

{{< info >}}
In case you receive an error message on step 3, you may also need to install the package **"apt-transport-https"** with the following command: 

```bash
sudo apt install apt-transport-https
```
{{< /info >}}
