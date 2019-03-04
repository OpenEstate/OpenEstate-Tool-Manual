---

title: Updating ImmoTool-Server
linktitle: Updates
description: How to update OpenEstate-ImmoServer…
weight: 50

menu:
  main:
    parent: admin-server
    identifier: admin-server-update

---

## Updating ImmoTool-Server {#admin_server_update}

ImmoTool-Server is updated much more rarely compared to ImmoTool. In contradiction to ImmoTool the ImmoTool-Server does **not check for updates automatically**. Therefore you should visit the [OpenEstate website](https://openestate.org/) regularly or subscribe to the [RSS feed](https://openestate.org/news/feed/en/rss/) in order to get notifications about updates.

Download the installation package for your operating system and start the installation process (see ["Installing ImmoTool-Server"]({{< relref "../../intro/install_server.md#intro_install_server" >}})). Thereby keep the following notices for your operating system in mind.

{{< warning >}}
Always close the ImmoTool-Server application before starting the update process.
{{< /warning >}}

{{< tip >}}
In order to avoid a data loss in case of an error, it is recommended to backup the [data directory]({{< relref "directories.md#admin_server_directories_data" >}}) before starting the update procedure.
{{< /tip >}}


### Update on Windows {#admin_server_update_windows}

The **EXE** installer automatically detects, where the application was installed beforehand and will update the files accordingly.

{{< warning >}}
If you made custom modifications to the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}), you should backup all files in this directory before installing the update. Afterwards you can copy the modified files back.
{{< /warning >}}


### Update on macOS {#admin_server_update_mac}

Move the application symbol of **"OpenEstate-ImmoServer"** to the same location, where ImmoTool-Server was installed beforehand. The operating system will show the following question:

{{< figure src="update_mac.png" caption="Question about overwriting on macOS" >}}

{{< todo >}}
Provide an English screenshot.
{{< /todo >}}

Answer this question in the dialog window by clicking on **"Replace"**.


### Update on Debian, Ubuntu & Co. {#admin_server_update_debian}

If the Debian repository was configured in your operating system (see ["Obtain packages from the Debian repository"]({{< relref "../../intro/download.md#intro_download_debian" >}})), you do **not** have to download the updated version from the OpenEstate website. Instead you can execute the following commands:

```bash
sudo apt update
sudo apt install openestate-immoserver
```

If you do **not** use the Debian repository but installed the program from the [**Debian** package]({{< relref "../../intro/install_client.md#intro_install_client_setup_debian" >}}), you can download the **DEB** installation package. Install the downloaded package with a double click or via the following command:

```bash
sudo dpkg -i openestate-immoserver_x.y.z_amd64.deb
```

Replace **`x.y.z`** with the version number of the downloaded file.

{{< warning >}}
If you made custom modifications to the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}), you should backup all files in this directory before installing the update. Afterwards you can copy the modified files back.
{{< /warning >}}


### Update on Linux {#admin_server_update_linux}

1.  Find out the path, where ImmoTool-Server was installed beforehand.
2.  Download the **TAR.GZ** installation package for your Linux system and extract the file on your computer. 
3.  Rename the folder, you have determined in step 1 - e.g. **`OpenEstate-ImmoServer-OLD`**.
4.  Create a new / empty folder with the name, you have determined in step 1 - e.g. **`OpenEstate-ImmoServer`**.
5.  Copy the files, that were extracted in step 2 into the newly created / empty folder.

After you have been able to properly start the application in the updated version you might remove the temporary folder created in step 3.

{{< warning >}}
If you made custom modifications to the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}), you should backup all files in this directory before installing the update. Afterwards you can copy the modified files back.
{{< /warning >}}
