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


### Update on Debian, Ubuntu & Co. {#admin_client_update_debian}

If the Debian repository was configured in your operating system (see ["Obtain packages from the Debian repository"]({{< relref "../../intro/download.md#intro_download_debian" >}})), you do **not** have to download the updated version from the OpenEstate website. Instead you can execute the following commands:

```bash
sudo apt update
sudo apt install openestate-immotool
```

If you do **not** use the Debian repository but installed the program from the [**Debian** package]({{< relref "../../intro/install_client.md#intro_install_client_setup_debian" >}}), you can download the **DEB** installation package. Install the downloaded package with a double click or via the following command:

```bash
sudo dpkg -i openestate-immotool_x.y.z_amd64.deb
```

Replace **`x.y.z`** with the version number of the downloaded file.


### Update on Linux {#admin_client_update_linux}

1.  Find out the path, where ImmoTool was installed beforehand.
2.  Download the **TAR.GZ** installation package for your Linux system and extract the file on your computer.
3.  Rename the folder, you have determined in step 1 - e.g. **`OpenEstate-ImmoTool-OLD`**.
4.  Create a new / empty folder with the name, you have determined in step 1 - e.g. **`OpenEstate-ImmoTool`**.
5.  Copy the files, that were extracted in step 2 into the newly created / empty folder.

After you have been able to properly start the application in the updated version you might remove the temporary folder created in step 3.
