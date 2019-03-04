---

title: Directories of ImmoTool-Servers
linktitle: Directories
description: Which directories are used by OpenEstate-ImmoServer…
weight: 20

menu:
  main:
    parent: admin-server
    identifier: admin-server-directories

---

## Directories of ImmoTool-Server {#admin_server_directories}

ImmoTool-Server operates on different directories on the hard drive.


### Application directory of ImmoTool-Server {#admin_server_directories_application}

The application directory contains the installed files necessary to run ImmoTool-Server.

-   On Windows systems the path **`C:\Programme\OpenEstate-ImmoServer`** is used by default. But during the installation process the user might select another location.

-   On macOS systems it depends, where the application bundle was copied to during the installation. By default the application bundle should be located at **`/Applications/OpenEstate-ImmoServer.app`**. The application directory itself is located inside the application bundle in the **`Contents/Resources`** subfolder.

-   If the [**Debian** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) (or Debian repository) was used on Debian, Ubuntu, Linux Mint & Co. for installation, the application directory is located at **`/opt/OpenEstate-ImmoServer`**.

-   If the [**TAR.GZ** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}}) was used on Linux for installation, it depends where the extracted folder was moved to.

The application directory contains a **`bin`** subfolder with several scripts and applications for ImmoTool-Server.

ImmoTool-Server does **not** write any files / data into to the application directory. It only reads from this directory.

{{< tip >}}
It is recommended to make sure, that regular users of the operating system only have read access to the application directory. Administrators might set appropriate permissions to this directory in order to avoid accidental modifications.
{{< /tip >}}


### Data directory of ImmoTool-Server {#admin_server_directories_data}

All data, that is created and written by ImmoTool-Server, is stored in the data directory (e.g. databases, backups, log files).

-   If the [**Debian** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) (or Debian repository) was used on Debian, Ubuntu, Linux Mint & Co. for installation, the data directory is located at **`/var/lib/OpenEstate-ImmoServer`**.

-   For all other types of installation (Windows, macOS, Linux via [**TAR.GZ** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}})) the data directory is located at the subfolder **`OpenEstate-ImmoServer`** of the home directory by the user, who executed the application.


### Protocol directory of ImmoTool-Server {#admin_server_directories_log}

The protocol directory contains log files with messages created during the execution of ImmoTool-Server.

-   If the [**Debian** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) (or Debian repository) was used on Debian, Ubuntu, Linux Mint & Co. for installation, the protocol directory is located at **`/var/log/OpenEstate-ImmoServer`**.

-   For all other types of installation (Windows, macOS, Linux via [**TAR.GZ** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}})) the protocol directory is located in the subfolder **`log`** of the [data directory]({{< relref "directories.md#admin_server_directories_data" >}}).


### Configuration directory of ImmoTool-Server {#admin_server_directories_etc}

ImmoTool-Server uses the configuration directory to load its configurations.

-   On Windows systems the **`etc`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) is used as configuration directory.

-   On macOS systems the application creates an **`etc`** subfolder in the [data directory]({{< relref "directories.md#admin_server_directories_data" >}}) of the executing user on the first startup. The program copies its default configuration files into this folder.

-   If the [**Debian** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}) (or Debian repository) was used on Debian, Ubuntu, Linux Mint & Co. for installation, the configuration directory is located at **`/etc/OpenEstate-ImmoServer`**.

-   If the [**TAR.GZ** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}}) was used for installation on Linux, the **`etc`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) is used as configuration directory.

{{< info >}}
The chapter ["Configure ImmoTool-Server"]({{< relref "setup.md#admin_server_setup" >}}) contains further information about how to configure ImmoTool-Server for your personal needs.
{{< /info >}}


### Configure directories of ImmoTool-Server {#admin_server_directories_setup}

It is possible to change the location of the directories used by Immotool-Server.

{{< info >}}
The user of the operating system, who starts ImmoTool-Server, needs write permission on the protocol and data directory. For the configuration directory only read access is required.
{{< /info >}}


#### Configure directories on Linux & macOS {#admin_server_directories_setup_unix}

On Linux and macOS systems you can create a file at **`/etc/default/OpenEstate-ImmoServer`** with the following contents:

```bash
# path to configuration directory
SERVER_ETC_DIR="/etc/OpenEstate-ImmoServer"

# path to protocol directory
SERVER_LOG_DIR="/var/log/OpenEstate-ImmoServer"

# path to data directory
SERVER_VAR_DIR="/var/lib/OpenEstate-ImmoServer"
```

Enter the desired path of the directories behind the variables and restart ImmoTool-Server afterwards. 


#### Configure directories on Windows {#admin_server_directories_setup_windows}

On Windows it depends, how the individual applications provided by ImmoTool-Server are started. 

-   If **EXE** files are used, you can edit the identically named **`l4j.ini`** with a text editor. Change the following lines in these files:

    ```ini
    # path to configuration directory
    -Dopenestate.server.etcDir=D:\OpenEstate-ImmoServer\etc
    
    # path to protocol directory
    -Dopenestate.server.logDir=D:\OpenEstate-ImmoServer\log
    
    # path to data directory
    -Dopenestate.server.varDir=D:\OpenEstate-ImmoServer
    ```

-   If **BAT** files are used, you can edit these files with a text editor. You can change the following lines:

    ```batch
    :: path to configuration directory
    set "SERVER_ETC_DIR=D:\OpenEstate-ImmoServer\etc"
    
    :: path to protocol directory
    set "SERVER_LOG_DIR=D:\OpenEstate-ImmoServer\log"
    
    :: path to data directory
    set "SERVER_VAR_DIR=D:\OpenEstate-ImmoServer"
    ```
    
-   If a service was installed on Windows, you can edit the path to the directories in the service management application (siehe ["Manage service on Windows"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

    {{< figure src="directories_setup_windows_service.png" caption="Change directories in service management application" >}}
    
    Open the tab **"Java"** in the service management application and update the values in the **"Java Options"** text field according to your requirements:
    
    -   Enter the path of the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}) behind **`-Dopenestate.server.etcDir=`**.
    -   Enter the path of the [protocol directory]({{< relref "directories.md#admin_server_directories_log" >}}) behind **`-Dopenestate.server.logDir=`**.
    -   Enter the path of the [data directory]({{< relref "directories.md#admin_server_directories_data" >}}) behind **`-Dopenestate.server.varDir=`**.

