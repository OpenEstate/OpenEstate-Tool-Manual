---

title: Installing ImmoTool
linktitle: Install ImmoTool
description: How to install and setup OpenEstate-ImmoTool on a workplace…
weight: 50

menu:
  main:
    parent: intro
    identifier: intro-install-client

---

## Installing ImmoTool {#intro_install_client}


### Install the application {#intro_install_client_setup}

Download the ImmoTool installation package for your operating system (see ["Download the applications"]({{< relref "download.md#intro_download" >}})).


#### Installation on Windows {#intro_install_client_setup_windows}

On Windows systems you should download the **EXE** installation file. On a 64bit Windows system you should use the corresponding 64bit installer. 

Start the downloaded EXE installer with a double click. Afterwards an installation program shows up, that will guide you through the installation process. 

{{< figure src="install_client_windows.png" caption="Installing ImmoTool on Windows" >}}


#### Installation on macOS {#intro_install_client_setup_mac}

On macOS systems you should download the **DMG** installation file. Start the downloaded file with a double click in order to show the following installation dialog:

{{< figure src="install_client_mac.jpg" caption="Installing ImmoTool on macOS" >}}

Click with your mouse on the application symbol of **"OpenEstate-ImmoTool"** and drag it into the **"Applications"** folder. This will copy the application into your **`Applications`** folder. In future you can find the application in your Finder by opening the **`Applications`** folder.

Alternatively you can drop the application symbol somewhere else - e.g. on your desktop or any other location on your hard drive.


#### Installation on Debian, Ubuntu or similar {#intro_install_client_setup_debian}

For Debian based Linux distributions (e.g. **Debian**, **Ubuntu** or **Linux Mint**) there are different **Debian packages** it is recommended to use the Debian repository (see ["Obtain packages from the Debian repository"]({{< relref "download.md#intro_download_debian" >}})). After the repository was registered in the operating system you may install the **Debian package** with the following commands:

1.  Update the package index via:
    
    ```bash
    sudo apt update
    ```
    
2.  Install ImmoTool:

    ```bash
    sudo apt install openestate-immotool
    ```

In case you do not like or want to use the repository, you may *alternatively* download the **Debian package** (resp. the **DEB** installation file). Install the package with a double click or via the following command: 

```bash
sudo dpkg -i openestate-immotool_x.y.z_amd64.deb
```

(Replace **`x.y.z`** with the version number of the downloaded file.)

{{< info >}}
The Debian package installs the application into the **`/opt/OpenEstate-ImmoTool`** directory.
{{< /info >}}

{{< info >}}
The Debian package automatically adds start menu entries of the application for each user in the operating system.
{{< /info >}}


#### Installation on Linux {#intro_install_client_setup_linux} 

If you do not use a Debian based Linux distribution or do not want to use the repository, you may alternatively download the **TAR.GZ** installation file. Make sure to select the correct installation file for your processor architecture (most commonly used is **x86-64**).

After the file was extracted on your computer you should find a directory called **`OpenEstate-ImmoTool`**. Move this directory to your preferred location on your hard drive (e.g. into the home directory or to **`/opt/OpenEstate-ImmoTool`**). 

{{< tip >}}
You may execute the **`StartMenuAdd.sh`** script within the **`bin`** folder of the application. This will create the start menu entries of the application for the current user. 
{{< /tip >}} 


### Starting ImmoTool {#intro_install_client_startup}


#### Start ImmoTool on Windows {#intro_install_client_startup_windows}

The Windows installer will automatically create a desktop shortcut for the application. Alternatively you can find a folder called **"OpenEstate-ImmoTool"** in the start menu, that contains the shortcuts of the application. 

Besides this you may start the application by executing the **`ImmoTool.exe`** (or **`ImmoTool.bat`**) file in the **`bin`** subfolder of the [application directory]({{< relref "../admin/client/directories.md#admin_client_directories_application" >}}). 


#### Start ImmoTool on macOS {#intro_install_client_startup_mac}

Open the application bundle called **"OpenEstate-ImmoTool"** with a double click. This will open a Finder window with the applications provided by ImmoTool.

{{< figure src="../admin/client/startup_mac_folder.png" caption="Finder window with ImmoTool applications" >}}

{{< todo >}}
Provide an English screenshot.
{{< /todo >}}

A double click on the **"ImmoTool"** application will start the application.

{{< tip >}}
You may integrate the **"ImmoTool"** application symbol into the Dock for future application starts (see [documentation by Apple](https://support.apple.com/en-us/HT201730)).
{{< /tip >}}


#### Start ImmoTool on Linux {#intro_install_client_startup_linux}

If ImmoTool was installed with the [**Debian** package]({{< relref "install_client.md#intro_install_client_setup_debian" >}}), you will find an entry called **"OpenEstate-ImmoTool"** in your start menu.

If ImmoTool was installed with the [**TAR.GZ** package]({{< relref "install_client.md#intro_install_client_setup_linux" >}}), you may have to start the **`StartMenuAdd.sh`** script in the **`bin`** subfolder of the [application directory]({{< relref "../admin/client/directories.md#admin_client_directories_application" >}}) in order to create the start menu entry for ImmoTool.

Alternatively you may start the application by executing the **`ImmoTool.sh`** script in the **`bin`** subfolder of the [application directory]({{< relref "../admin/client/directories.md#admin_client_directories_application" >}}).


### Language selection {#intro_install_client_language}

If ImmoTool is started for the first time and the language of your operating system is not available in the application, you will have to select your preferred language.

{{< figure src="install_client_language.png" caption="Language selection on first application start" >}}

This window provide a selection of languages, that the application was translated into.

{{< info >}}
ImmoTool may be translated into every language. If you like to help us out with a translation (z.B. new language or fixes in current translations), you can find further information on the [OpenEstate website](https://openestate.org/immotool/translations).
{{< /info >}}


### Create local project {#intro_install_client_project}

If ImmoTool is started for the first time, the project wizards shows up. You will have to create a local project, that provides the database for the application.

{{< info >}}
Within ImmoTool a project is a synonym for a database, that contains all gathered data (real estates, customers, attachments, etc.). In most cases you will only need **one project**, that has to be created once on the first application start. On later startups this project is opened automatically.
{{< /info >}}

{{< warning >}}
In case you are planning to install a **multi-user installation** (see ["Installing on a multiple workplaces"]({{< relref "install_types.md#intro_install_types_network" >}})), please follow the advices in chapter ["Installing ImmoTool-Server"]({{< relref "install_server.md#intro_install_server" >}}). In this case it is **not necessary** to create a local project.
{{< /warning >}}

{{< figure src="install_client_project.png" caption="Create local project on first application start" >}}

Enter the following options into the project wizard in order to create a **local project**:

-   **Project title:** \
    Enter any desired name for the project.

-   **Projekt type:** \
    Select the option **"Create new local project."**.

-   You may open the tab **"Company"** and add some more information about your company.

-   You may open the tab **"Addons"** and enable / disable certain extensions in the project.

After the license agreement was accepted you can create the project by clicking on the button **"Create project""**. The newly created project is automatically opened afterwards. 

From now on you can work with the application. We wish you a lot of fun and success!
