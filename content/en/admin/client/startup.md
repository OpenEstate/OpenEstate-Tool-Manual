---

title: Starting ImmoTool
linktitle: Startup
description: How to start OpenEstate-ImmoTool…
weight: 10

menu:
  main:
    parent: admin-client
    identifier: admin-client-startup

---

## Starting ImmoTool {#admin_client_startup}

### Start ImmoTool on Windows {#admin_client_startup_windows}

The Windows installer will automatically create a desktop shortcut for the application. Alternatively you can find a folder called **"OpenEstate-ImmoTool"** in the start menu, that contains the shortcuts of the application. 

Besides this you may start the application by executing the **`ImmoTool.exe`** (or **`ImmoTool.bat`**) file in the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_client_directories_application" >}}).


### Start ImmoTool on macOS {#admin_client_startup_mac}

Open the application bundle called **"OpenEstate-ImmoTool"** with a double click. This will open a Finder window with the applications provided by ImmoTool.

{{< figure src="startup_mac_folder.png" caption="Finder window with ImmoTool applications" >}}

{{< todo >}}
Provide an English screenshot.
{{< /todo >}}

A double click on the **"ImmoTool"** application will start the application.

{{< tip >}}
You may integrate the **"ImmoTool"** application symbol into the Dock for future application starts (see [documentation by Apple](https://support.apple.com/en-us/HT201730)).
{{< /tip >}}

Besides this you may start the application by executing the **`ImmoTool.sh`** file in the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_client_directories_application" >}}).


### Start ImmoTool on Linux {#admin_client_startup_linux}

If ImmoTool was installed with the [**Debian** package]({{< relref "../../intro/install_client.md#intro_install_client_setup_debian" >}}), you will find an entry called **"OpenEstate-ImmoTool"** in your start menu.

If ImmoTool was installed with the [**TAR.GZ** package]({{< relref "../../intro/install_client.md#intro_install_client_setup_linux" >}}), you may have to start the **`StartMenuAdd.sh`** script in the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_client_directories_application" >}}) in order to create the start menu entry for ImmoTool.

Alternatively you may start the application by executing the **`ImmoTool.sh`** script in the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_client_directories_application" >}}).


### Start parameters of ImmoTool {#admin_client_startup_params}

You may customize the application startup via **`ImmoTool.exe`** / **`ImmoTool.bat`** / **`ImmoTool.sh`** with the following parameters:

-   **-help** \
    Shows a summary of available command line arguments.

-   **-noProject** \
    Starts the application without automatically opening a project. Instead the *project wizard* is shown.

-   **-project `<PROJECT>`** \
    Automatically opens the project located in the **`<PROJECT>`** folder on startup.

-   **-projectLogin `<USER>`** \
    If the project specified by the **`-project`** parameter is a multi-user project, the program will automatically login as user **`<USER>`**.

-   **-projectPass `<PASSWORD>`** \
    If the project specified by the **`-project`** parameter is a multi-user project, the program will automatically login with the password **`<PASSWORD>`**.

{{< todo >}}
Add link to the project wizard in the usage section.
{{< /todo >}}
