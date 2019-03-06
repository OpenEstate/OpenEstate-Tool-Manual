---

title: Backup & restore databases
linktitle: Backups
description: How to backup & restore a database of OpenEstate-ImmoTool…
weight: 40

menu:
  main:
    parent: admin
    identifier: admin-backup

---

## Backup & restore databases {#admin_backup}

For everyday usage it is **highly recommended** to find and implement a strategy for regular backups. This chapter describes different approaches about how to backup the databases of ImmoTool and ImmoTool-Server.

Please consider, that you have to follow different approaches for [single-user installations]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) and [multi-user installations]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) (see ["How ImmoTool can be installed…"]({{< relref "../intro/install_types.md#intro_install_types" >}})).

{{< warning >}}
Do not simply rely on the backup features of your operating system. Practice has shown, that for example restore points on Windows led to corrupt databases.
{{< /warning >}}

{{< info >}}
In order to avoid a possible data loss, you should implement a backup strategy as soon as ImmoTool is used productively.
{{< /info >}}

{{< tip >}}
It is recommended to test the procedure of backup and restore beforehand. Take notes of the required steps. In case of a system failure you can rely on your notes and previously made experiences, which finally reduces a possible downtime.
{{< /tip >}}

{{< tip >}}
In order to ensure the best possible failure safety you should save the database backups to an external location. For example use an external hard drive or send the backup files to an external server (e.g. your webspace or cloud provider).
{{< /tip >}}


### Backup single-user installations {#admin_backup_local}

On **single-user installations** the database is managed by the Immotool itself (see ["Installing on a single workplace"]({{< relref "../intro/install_types.md#intro_install_types_local" >}})). Therefore in most cases the backup should be executed from the same system, on which ImmoTool is installed.


#### Copy project folder {#admin_backup_local_copy}

The easiest way of backing up a **single-user installation** is copying the [project directory]({{< relref "client/directories.md#admin_client_directories_project" >}}). Find out where your project directory is located and copy this folder accordingly.

{{< info >}}
By default ImmoTool creates a separate directory for each project in the **`OpenEstate-Files/projects`** subfolder of the user's home directory.
{{< /info >}}

{{< warning >}}
You should only copy the [project directory]({{< relref "client/directories.md#admin_client_directories_project" >}}), if ImmoTool is not running or the project is currently not opened.
{{< /warning >}}


#### Manual backup via ImmoTool {#admin_backup_local_manual}

After the local project was opened in ImmoTool you can click in the main menu at **"Extras → Database → Backup"** in order to create a database backup manually. A dialog window is shown, where you can select the save location of the backup file.


#### Automatic backup via ImmoTool {#admin_backup_local_automatic}

As an alternative to a manual backup you can configure automatic backups for local projects (single-user installations). In this case the application will automatically create backups in certain situations.

After the local project was opened in ImmoTool you can click in the main menu at **"Extras → Settings"** in order to open the settings dialog window. After selecting the form **"Database"** you will see the following view: 

{{< figure src="backup_local_automatic.png" caption="Configure automatic backups" >}}

You can choose a target folder, where automatic backups are saved at. Besides this you may choose, in which case an automatic should be created (e.g. while the project is opened).

The number selected as **"Limit"** determines, how many backups are kept in the selected target directory. For example if more than five backups are stored in the target directory, the oldest backups are automatically removed. The defined limit will not be exceeded.

{{< tip >}}
You might select an external hard drive or a network drive as backup location. This makes sure, that the backups are not lost in case of a hardware failure on your local system.
{{< /tip >}}


#### Restoring a backup {#admin_backup_local_restore}

If the [project directory]({{< relref "client/directories.md#admin_client_directories_project" >}}) was copied (see ["Copy project folder"]({{< relref "backup.md#admin_backup_local_copy" >}})), you can simple copy the folder back to its original location. Afterwards the project can be opened again with ImmoTool. Further steps for restoring the backup are **not** necessary in this case.

Backups created within ImmoTool have been stored as **TAR.GZ** archives (see ["Manual backup via ImmoTool"]({{< relref "backup.md#admin_backup_local_manual" >}}) and ["Automatic backup via ImmoTool"]({{< relref "backup.md#admin_backup_local_automatic" >}})). In order to restore these archives you can follow these steps:

1.  Close ImmoTool, if it is currently running.
2.  Extract the TAR.GZ archive, that contains the database backup.
3.  Open the [project directory]({{< relref "client/directories.md#admin_client_directories_project" >}}) in your file browser (Explorer / Finder).
4.  Rename the **`data`** subfolder - e.g. to **`data-old`**.
5.  Create a new / empty **`data`** subfolder.
6.  Copy the files extracted from step 2 into the newly created **`data`** folder.
7.  Start ImmoTool and open the project.

If the restored project was successfully opened, you might remove the folder **`data-old`** created in step 4.

{{< tip >}}
If you do not know where the project is located or do not have a project available anymore, you might create a new / empty local project first and afterwards follow the steps above.
{{< /tip >}}


### Backup multi-user installations {#admin_backup_network}

On **multi-user installations** the database is managed by Immotool-Server (see ["Installing on a multiple workplaces"]({{< relref "../intro/install_types.md#intro_install_types_network" >}})). Therefore in most cases the backup should be executed from the same system, on which ImmoTool-Server is installed.


#### Backup an inactive ImmoTool-Server {#admin_backup_network_copy}

If ImmoTool-Server is not running (or was temporarily stopped), you can copy its [data directory]({{< relref "server/directories.md#admin_server_directories_data" >}}). By default this directory contains the files of all managed databases.

{{< warning >}}
It is not recommended to copy the [data directory]({{< relref "server/directories.md#admin_server_directories_data" >}}) while ImmoTool-Server is running. This may lead to a faulty backup, that can not be restored easily.
{{< /warning >}}


#### Backup a running ImmoTool-Server {#admin_backup_network_live}

You can create backups of ImmoTool-Server while the application is running. For this use case the helper application **"ManagerBackup"** is provided.

-   On Windows you can open start menu and select the shortcut **"OpenEstate-ImmoServer → Management → Create database backup"**.
-   On macOS you can open the application bundle **"OpenEstate-ImmoServer"** and start the **"ManagerBackup"** application.
-   Alternatively you can start the **`ManagerBackup.exe`** / **`ManagerBackup.bat`** / **`ManagerBackup.sh`** file in the **`bin`** subfolder of the [application directory]({{< relref "server/directories.md#admin_server_directories_application" >}}).

The **ManagerBackup** application needs to connect with the databases to backup. Therefore the application needs to login with an administrative account for all databases to backup.

Open the **`manager.conf`** file in the [configuration directory]({{< relref "server/directories.md#admin_server_directories_etc" >}}) with a text editor. For each database to backup you need to provide these lines:

```
urlid immotool
url jdbc:hsqldb:hsql://localhost:9001/immotool
username SA
password
```

After the **`password`** value you need to enter the password of the database administrator (**`SA`**) separated by space - e.g. **`password test1234`** (see ["Configure manager applications"]({{< relref "server/setup.md#admin_server_setup_manager" >}})).

By default the **ManagerBackup** application creates a backup for all databases specified in the **`manager.conf`** file. By default the application stores the backup into the **`backups`** subfolder of the [data directory]({{< relref "server/directories.md#admin_server_directories_data" >}}).

{{< info >}}
Before automating the backup process you should test, if the **ManagerBackup** is properly configured and works as expected.
{{< /info >}}


##### Automatic backup on Windows {#admin_backup_network_live_windows}

The Windows operating system provides a dialog window for task scheduling, which can be used for automatic execution of the **ManagerBackup** application at freely chosen times.

Open the [Windows Task Scheduler](https://en.wikipedia.org/wiki/Windows_Task_Scheduler) application: 

1.  Press the **"Windows key"** together with the letter **"R"** to open a window for command execution. Alternatively you can open the command prompt.

2.  Enter the command **`taskschd.msc`** and press the **"ENTER"** key.

Click on the right side in the **"Actions"** section on the **"Create task"** link.

{{< figure src="backup_network_live_windows_task_add.png" caption="Create task for automatic backup" >}}

A new dialog window shows up, which allows the creation of the backup task.

{{< figure src="backup_network_live_windows_task_general.png" caption="General settings for the task" >}}

Open the tab **"General"** and enter a suitable name and description for the task. Besides this you should click on the **"Change User or Group"** button and select the **"Local Service"** user. 

{{< figure src="backup_network_live_windows_task_trigger.png" caption="Zeit der Ausführung wählen" >}}

Open the tab **"Triggers"** in order to configure the execution time of automated backups.

{{< figure src="backup_network_live_windows_task_action.png" caption="Auszuführendes Programm wählen" >}} 

Open the tab **"Actions"** and select the **`ManagerBackup.exe`** application from the **`bin`** subfolder of the [application directory]({{< relref "server/directories.md#admin_server_directories_application" >}}).

You may change further settings in this dialog window. After you have completed the configuration, click on the **"OK"** button in order to register the task in the operating system.

{{< todo >}}
Provide English screenshots.
{{< /todo >}}


##### Automatic backup on macOS {#admin_backup_network_live_mac}

While installing a service for ImmoTool-Server on macOS you can enable daily automatic backups (see ["Setup service on macOS"]({{< relref "server/service.md#admin_server_service_mac" >}})).  

If automated backups were enabled while installing the service, the script creates a file **`org.openestate.tool.server.backup.plist`** in the **`/Library/LaunchDaemons`** directory. This file tells the operating system to automatically execute **ManagerBackup** once in a day.

{{< info >}}
You are not forced to use the provided mechanism for automated backups. You might also create your own cronjob (or agent for launchd), that executes the **ManagerBackup** application.
{{< /info >}}


##### Automatic backup on Linux {#admin_backup_network_live_linux}

If ImmoTool-Server was installed with the [**Debian** package]({{< relref "../intro/install_server.md#intro_install_server_setup_debian" >}}), a timer for daily automated backups is already installed.

Alternatively a timer can be registered, while a service for ImmoTool-Server on Linux is installed (see ["Setup service on Linux"]({{< relref "server/service.md#admin_server_service_linux" >}})).

The files **`openestate-immoserver-backup.timer`** and **`openestate-immoserver-backup.service`** in the **`/etc/systemd`** folder are used to trigger automatic execution of the **ManagerBackup** application.

{{< info >}}
You are not forced to use the provided mechanism for automated backups. You might also create your own cronjob (or timer for systemd), that executes the **ManagerBackup** application.
{{< /info >}}


##### Parameters for ManagerBackup {#admin_backup_network_live_options}

The **ManagerBackup** can be controlled by the following command line parameters:

-   **-help** \
    Shows a summary of available command line arguments.

-   **-conf `<file>`** \
    You may specify a custom path to the **`manager.conf`** configuration file.
    
-   **-id `<urlid>`** \
    Only the database with identifier **`<urlid>`** from the **`manager.conf`** file should be backed up. Otherwise all configured database are backed up.

-   **-dir `<path>`** \
    You may specify the directory at **`<path>`**, where backups are stored.

-   **-limit `<number>`** \
    You may set the maximal number **`<number>`** of backups to keep for each database. Older backups are automatically removed, if the limit is exceeded.
    
-   **-delay `<seconds>`** \
    You may delay the execution of the backup for **`<seconds>`** seconds.
    
-   **-wait** \
    After the backup was successfully executed the applications waits for the user to press the **"ENTER"** key. 
    
-   **-dump** \
    Create a database dump instead of copying the database files.


#### Restoring a server backup {#admin_backup_network_restore}

A database backup is a copy of the database files. You can restore these files quite easily by following these steps: 

1.  Stop ImmoTool-Server, if it is currently running.

2.  If the backup is created as **ZIP** or **TAR.GZ** archive, extract these files accordingly.

3.  Rename the database directory and create a new / empty database directory with the same name.

4.  Copy the database files **`db.data`**, **`db.lobs`**, **`db.properties`** & **`db.script`** into the database directory (see ["Data directory of ImmoTool-Server"]({{< relref "server/directories.md#admin_server_directories_data" >}})).

5.  Start ImmoTool-Server in order to make the restored databases available.

If the restored project was successfully opened, you might remove the renamed database directory created in step 3.
