---

title: Updating ImmoTool
linktitle: Updates
description: How to update OpenEstate-ImmoTool…
weight: 30

menu:
  main:
    parent: admin-client
    identifier: admin-client-update

---

## Updating ImmoTool {#admin_client_update}

Once per day the application searches for available updates on startup. The following information is shown, in case that updates are available: 

{{< figure src="update_notification.png" caption="Information about available updates" >}}

Click on **"Download installation package."** in order to open the web browser and download the installation package for the currently used operating system.

Click on **"Open download website."** in order to open the [download page](https://openestate.org/downloads/openestate-immotool) for the new application version.   

Download the installation package for your operating system and start the installation process (see ["Installing ImmoTool"]({{< relref "../../intro/install_client.md#intro_install_client" >}})). Thereby keep the following notices for your operating system in mind. 

{{< warning >}}
Always close the ImmoTool application before starting the update process.
{{< /warning >}}

{{< info >}}
If ImmoTool is installed on multiple workplaces (see ["Installing on a multiple workplaces"]({{< relref "../../intro/install_types.md#intro_install_types_network" >}})), you should update the application on **all workplaces**. Different versions of ImmoTool might not work in a multi-user installation.
{{< /info >}}


### Update on Windows {#admin_client_update_windows}

The **EXE** installer automatically detects, where the application was installed beforehand and will update the files accordingly. 


### Update on macOS {#admin_client_update_mac}

Move the application symbol of **"OpenEstate-ImmoTool"** to the same location, where ImmoTool was installed beforehand. The operating system will show the following question: 

{{< figure src="update_mac.png" caption="Question about overwriting on macOS" >}}

{{< todo >}}
Provide an English screenshot.
{{< /todo >}}

Answer this question in the dialog window by clicking on **"Replace"**.


### Update on Debian, Ubuntu or similar {#admin_client_update_debian}

If the Debian repository was configured in your operating system (see ["Obtain packages from the Debian repository"]({{< relref "../../intro/download.md#intro_download_debian" >}})), you do **not** have to download the updated version from the OpenEstate website. Instead you can execute the following commands:

```bash
sudo apt update
sudo apt install openestate-immotool
```

If you do **not** use the Debian repository but installed the program from the [**Debian** package]({{< relref "../../intro/install_client.md#intro_install_client_setup_debian" >}}), you can download the **DEB** installation package. Install the downloaded package with a double click or via the following command:

```bash
sudo dpkg -i openestate-immotool_x.y.z_amd64.deb
```

(Replace **`x.y.z`** with the version number of the downloaded file.)


### Update on Linux {#admin_client_update_linux}

1.  Find out the path, where ImmoTool was installed beforehand.
2.  Download the **TAR.GZ** installation package for your Linux system and extract the file on your computer.
3.  Rename the folder, you have determined in step 1 - e.g. **`OpenEstate-ImmoTool-OLD`**.
4.  Create a new / empty folder with the name, you have determined in step 1 - e.g. **`OpenEstate-ImmoTool`**.
5.  Copy the files, that were extracted in step 2 into the newly created / empty folder.

After you have been able to properly start the application in the updated version you might remove the temporary folder created in step 3.


### Important advices for certain versions {#admin_client_update_advices}

This section contains advices about updates to certain application versions.


#### Update from version 1.0-beta to 1.x {#admin_client_update_advices_beta}

ImmoTool 1.0.0 introduced some major changes, that should be considered during an update from version 1.0-beta.


##### New installation routine for Windows & macOS {#admin_client_update_advices_beta_installer}

A **new installation routine** was implemented for **Windows** and **macOS** systems (EXE and DMG installation packages). The new installation packages are not compatible with the old update procedure. Please make sure, that you **do not overwrite** the previous ImmoTool version while installing the update. Therefore we are recommending the following approach:

-   Find out, in which folder ImmoTool 1.0-beta is currently installed on your hard drive. 

    -   If the application is located on Windows systems at **`C:\Programme\OpenEstate-ImmoTool`**, you should rename this folder - e.g. in **`C:\Programme\OpenEstate-ImmoTool-OLD`**.
    
    -   On macOS systems there should not be a problem with the naming of the folder. But nevertheless you should figure out, where the application is located.
    
-   On Windows you should remove of the application (from the Desktop or start menu). On macOS you might remove the application from the Dock.

-   Start the installation procedure (see ["Installing ImmoTool"]({{< relref "../../intro/install_client.md#intro_install_client" >}})).

-   If the application was successfully installed and started, you can remove the installation folder of ImmoTool 1.0-beta.

Future updates of ImmoTool 1.x do not require these steps and should work flawlessly. 


##### Java can be removed {#admin_client_update_advices_beta_java}

Since version 1.0.0 Java is bundled together with the ImmoTool application. Therefore you can **remove Java from your operating system** as long as you do not need it for other applications.  

-   On Windows you can open the system control panel and open the section for software removal. You should find an entry for **"Oracle Java"**, that can be removed.

-   On macOS you can follow these steps in order to remove **"Oracle Java"**:

    1.  Click on the **"Finder"** icon located in your dock.
    2.  Click on **"Go"** in the Finder menu.
    3.  Click on **"Utilities"**.
    4.  Double-click on the **"Terminal"** icon.
    5.  In the Terminal window copy and paste the commands below:
    
        ```bash
        sudo rm -fr /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin
        sudo rm -fr /Library/PreferencePanes/JavaControlPanel.prefPane
        sudo rm -fr ~/Library/Application\ Support/Oracle/Java
        ```

    (quoted from the [official instructions by Oracle](https://www.java.com/en/download/help/mac_uninstall_java.xml))

-   On Linux you might remove **"OpenJDK"** via the package system of your distribution. Or if **"Oracle Java"** was installed, you might remove its installation folder manually. 


#### Update from version 0.9.x to 1.x {#admin_client_update_advices_0_9}

For a migration from ImmoTool 0.9.x to 1.x the same advices apply as for the [migration from 1.0-beta to 1.x]({{< relref "update.md#admin_client_update_advices_beta" >}}). But in this case the project is not migrated automatically. Therefore you also need to follow the [instructions to migrate an old project into ImmoTool 1.x]({{< relref "../migration.md#admin_migration_legacy" >}}).
