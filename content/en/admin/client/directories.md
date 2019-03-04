---

title: Directories of ImmoTool
linktitle: Directories
description: Which directories are used by OpenEstate-ImmoTool…
weight: 20

menu:
  main:
    parent: admin-client
    identifier: admin-client-directories

---

## Directories of ImmoTool {#admin_client_directories}

ImmoTool operates on different directories on the hard drive.


### Application directory of ImmoTool {#admin_client_directories_application}

The application directory contains the installed files necessary to run ImmoTool.

-   On Windows systems the path **`C:\Programme\OpenEstate-ImmoTool`** is used by default. But during the installation process the user might select another location.

-   On macOS systems it depends, where the application bundle was copied to during the installation. By default the application bundle should be located at **`/Applications/OpenEstate-ImmoTool.app`**. The application directory itself is located inside the application bundle in the **`Contents/Resources`** subfolder.

-   If the [**Debian** package]({{< relref "../../intro/install_client.md#intro_install_client_setup_debian" >}}) (or Debian repository) was used on Debian, Ubuntu, Linux Mint & Co. for installation, the application is located at **`/opt/OpenEstate-ImmoTool`**.

-   If the [**TAR.GZ** package]({{< relref "../../intro/install_client.md#intro_install_client_setup_linux" >}}) was used on Linux for installation, it depends where the extracted folder was moved to.

The application directory contains a **`bin`** subfolder with several scripts and applications for ImmoTool.

ImmoTool does **not** write any files / data into to the application directory. It only reads from this directory.

{{< tip >}}
It is recommended to make sure, that regular users of the operating system only have read access to the application directory. Administrators might set appropriate permissions to this directory in order to avoid accidental modifications.
{{< /tip >}}


### Data directory of ImmoTool {#admin_client_directories_data}

If a user starts ImmoTool for the first time, the program will automatically create a folder called **`OpenEstate-Files`** in his home directory. This folder contains data and settings for ImmoTool **exclusively** for this user.

This folder is used by ImmoTool to write certain data during its runtime (e.g. protocols or temporary files).


### Project directory of ImmoTool {#admin_client_directories_project}

If a project is created within ImmoTool, the user can choose the location of the project directory for himself. By default the application stores the project directory into the **`projects`** subfolder of the [data directory]({{< relref "directories.md#admin_client_directories_data" >}}).

{{< info >}}
Each project created with ImmoTool is stored in its own / separate directory. This makes it easier to backup / move / replace a project by modifying the project folder.
{{< /info >}}

{{< info >}}
It is theoretically possible, that multiple users share the same project directory (e.g. by using a shared folder). But local projects (resp. [single-user-installations]({{< relref "../../intro/install_types.md#intro_install_types_local" >}})) can never be opened by multiple users at the same time.
{{< /info >}}

{{< warning >}}
You **should not** open a project directory from an unstable location (e.g. network drive or cloud drive). Network failures may corrupt the database. If you want to go this path nevertheless, keep in mind to backup the project as often as possible.
{{< /warning >}}


### Plugin directory of ImmoTool {#admin_client_directories_plugins}

The plugin directory contains the extensions (addons) as ZIP files loaded by ImmoTool. There are two locations, where addons can be stored:

1.  In the [application directory]({{< relref "directories.md#admin_client_directories_application" >}}) there is a **`plugins`** subfolder. The administrator of the operating system may place addons here, that are available for all users of the operating system.

2.  In the [data directory]({{< relref "directories.md#admin_client_directories_data" >}}) of each user there is also a **`plugins`** subfolder. The user may place addons here, that are only available for himself.

While ImmoTool is starting both directories are synchronized. If both folders contain the same addon in different versions, the application will load the newer version. 

{{< warning >}}
On macOS the plugin directory inside the application directory (within the **"OpenEstate-ImmoTool"** application bundle) should not be modified. Otherwise the signature of the application bundle might get invalid and [Gatekeeper](https://support.apple.com/en-us/HT202491) might reject starting up the application. Therefore you should always place addons into the **`plugins`** subfolder of the [data directory]({{< relref "directories.md#admin_client_directories_data" >}}) on macOS.
{{< /warning >}}
