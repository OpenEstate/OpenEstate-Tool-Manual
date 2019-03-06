---

title: Migrating projects
linktitle: Migration
description: How to migrate projects of OpenEstate-ImmoTool…
weight: 50

menu:
  main:
    parent: admin
    identifier: admin-migration

---


## Convert single-user into multi-user installation {#admin_migration_project_local}

A [single-user installation]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) can be migrated to a [multi-user installation]({{< relref "../intro/install_types.md#intro_install_types_network" >}}). Therefore the database has to be copied to the ImmoTool-Server and slightly modified.

1.  Install ImmoTool-Server, if it is not installed yet (see ["Installing ImmoTool-Server"]({{< relref "../intro/install_server.md#intro_install_server" >}})).

2.  Stop ImmoTool-Server, if it is currently running.

3.  Open the [data directory]({{< relref "server/directories.md#admin_server_directories_data" >}}) of the ImmoTool-Server and create a folder **`data/immotool`**, if it does not already exist. If the directory does already exist, remove all contained files and subfolders.

4.  Open the [directory of the local project]({{< relref "client/directories.md#admin_client_directories_project" >}}). There you should find a **`data`** folder. This directory contains the database files: **`immotool.data`**, **`immotool.lobs`**, **`immotool.properties`** and **`immotool.script`**.

5.  Copy the database files located in step 4 into the directory created in step 3. Rename these files to **`db.data`**, **`db.lobs`**, **`db.properties`** and **`db.script`**.

6.  Start ImmoTool-Server and connect to the copied database with [AdminTool]({{< relref "tool.md#admin_tool" >}}). Use the username **"SA"** and an **empty password**. On the first connection with [AdminTool]({{< relref "tool.md#admin_tool" >}}) you will be asked to enter a password for the **"SA"** user.

From now on the database is available for ImmoTool and AdminTool as a remote project. To finally access the database with ImmoTool you need to create a remote project (see ["Connect to ImmoTool-Server"]({{< relref "../intro/install_server.md#intro_install_server_immotool" >}})).

If the migration was successfully completed and ImmoTool properly connects to ImmoTool-Server, you might remove the old [directory of the local project]({{< relref "client/directories.md#admin_client_directories_project" >}}).


## Convert multi-user into single-user installation {#admin_migration_project_remote}

A [multi-user installation]({{< relref "../intro/install_types.md#intro_install_types_network" >}}) can be migrated to a [single-user installation]({{< relref "../intro/install_types.md#intro_install_types_local" >}}). Therefore the database has to be copied into a local project and slightly modified.

1.  Start ImmoTool and create a new / empty local project (see ["Create local project"]({{< relref "../intro/install_client.md#intro_install_client_project" >}})). Into this project the database will be transferred in the next steps.

2.  Close ImmoTool after the new / empty local project was created and opened for the first time.

3.  Stop ImmoTool-Server, if it is currently running.

4.  Open the [directory of the local project]({{< relref "client/directories.md#admin_client_directories_project" >}}) created in step 1. The **`data`** subfolder should contain these files: **`immotool.data`**, **`immotool.lobs`**, **`immotool.properties`** and **`immotool.script`**. Remove all files and subfolders from the **`data`** subfolder.

5.  Open the database directory of the ImmoTool-Server. By default you find this directory in the **`data/immotool`** subfolder of the [data directory]({{< relref "server/directories.md#admin_server_directories_data" >}}). You should find these files in this folder: **`db.data`**, **`db.lobs`**, **`db.properties`** and **`db.script`**. Copy these files into the **`data`** subfolder of the previously created project (see step 4). Rename the copied files to **`immotool.data`**, **`immotool.lobs`**, **`immotool.properties`** and **`immotool.script`**.

6.  Edit the **`immotool.script`** file from the **`data`** folder of the local project in a text editor.

    {{< warning >}}Copy a backup of the **`immotool.script`** file before making any changes. A mistake while editing may lead to a faulty database.{{< /warning >}}

7.  Seach in the **`immotool.script`** file for a line starting with:

    ```
    CREATE USER SA PASSWORD DIGEST
    ```

    Replace this line with:

    ```
    CREATE USER SA PASSWORD DIGEST 'd41d8cd98f00b204e9800998ecf8427e'
    ```

8.  Save the modified **`immotool.script`** file.

From now on you can open the local project with ImmoTool. All data from ImmoTool-Server is available in the local project.

In case you don't need ImmoTool-Server anymore, you might uninstall ImmoTool-Server after the migration was successfully finished.


## Migrate an old project from ImmoTool 0.9.x {#admin_migration_legacy}

ImmoTool 0.9.x is already very old. It is not developed any further and can not be supported by OpenEstate anymore. Therefore it is **heavily recommended** to migrate the application to the latest 1.x version. This chapter describes the required steps for migration.

{{< info >}}
You should **not** overwrite old ImmoTool 0.9.x installation. ImmoTool 1.x has to be installed separately. In case of problems during the migration you can continue using the old version until the problem was solved.
{{< /info >}}


### Export project from ImmoTool 0.9.x {#admin_migration_legacy_backup}

In the first step you need to open ImmoTool 0.9.x and create a backup of the project database.

1.  Make sure, that the latest available old version is used (at least **0.9.15** or **1.0-beta10f**). Therefore click in the main menu at **"Extras → Updates"**.

    {{< figure src="migration_update.png" caption="Update the old ImmoTool version" >}}
    
    Alternatively you might download version 0.9.33 (the latest 0.9.x Version) from the [OpenEstate website](https://openestate.org/downloads/openestate-immotool/0.9.33).

2.  Open the project to migrate in the old ImmoTool installation and create a database backup by clicking in the main menu at **"Extras → DB type → Sicherung für Version 1.x"**. (The translation in the application is incorrect here.)

    {{< figure src="migration_export.png" caption="Create a backup for ImmoTool 1.x" >}}
    
    This will create a ZIP archive with the contents of the project database. You will need this ZIP archive in the following steps.

The next steps depend on how you want to use ImmoTool 1.x in the future (as [single-user installation]({{< relref "../intro/install_types.md#intro_install_types_local" >}}) or [multi-user installation]({{< relref "../intro/install_types.md#intro_install_types_network" >}})).


### Migrate into a single-user installation {#admin_migration_legacy_local}

If ImmoTool 1.x should be used as [**single-user installation**]({{< relref "../intro/install_types.md#intro_install_types_local" >}}), install the latest version of ImmoTool 1.x next to your old ImmoTool installation (see ["Installing ImmoTool"]({{< relref "../intro/install_client.md#intro_install_client" >}})).

{{< warning >}}
Do **not** overwrite the old ImmoTool installation! Both versions should be installed **next to each other**.
{{< /warning >}}

If ImmoTool 1.x is started for the first time, the *project wizard* shows up. Create a new project and select the previously created ZIP file.

{{< todo >}}
Add link to the project wizard in the usage section.
{{< /todo >}}

{{< figure src="migration_import_local.png" caption="Datensicherung via Projektassistent importieren" >}}

Select as **"Project type"** the option **"Migrate local project from ImmoTool 0.9.x"**. Below you can find a form, where the  [previously created ZIP file]({{< relref "migration.md#admin_migration_legacy_backup" >}}) can be selected by clicking the **"Select"** button. The application will validate the ZIP file and automatically load the company information.

You might check and fix the company information and addon. Afterwards click on the **"Create project"** button. While the project is created the data from the ZIP file is automatically imported into the database. 

{{< info >}}
After the migration was successfully finished you might remove the old installation of ImmoTool 0.9.x.
{{< /info >}}


### Migrate into a multi-user installation {#admin_migration_legacy_remote}

If ImmoTool 1.x should be used as [**multi-user installation**]({{< relref "../intro/install_types.md#intro_install_types_network" >}}), install the latest version of ImmoTool 1.x next to your old ImmoTool installation (see ["Installing ImmoTool"]({{< relref "../intro/install_client.md#intro_install_client" >}})) and ImmoTool-Server (see ["Installing ImmoTool-Server"]({{< relref "../intro/install_server.md#intro_install_server" >}})).

{{< warning >}}
Do **not** overwrite the old ImmoTool installation! Both versions should be installed **next to each other**.
{{< /warning >}}

After ImmoTool-Server was installed you can import the database backup with [AdminTool]({{< relref "tool.md#admin_tool" >}}) into ImmoTool-Server. The [previously created ZIP file]({{< relref "migration.md#admin_migration_legacy_backup" >}}) can be imported via [AdminTool]({{< relref "tool.md#admin_tool" >}}) in one of these ways:

-   If ImmoTool-Server is connected **for the first time**, you will see a window on which the previously created ZIP file can be selected. 

    {{< figure src="migration_import_remote_new.png" caption="Import ZIP file while creating the database" >}}

-   If the database was already created with [AdminTool]({{< relref "tool.md#admin_tool" >}}), you can import the ZIP file **afterwards** by clicking in the main menu to **"Extras → Migration from ImmoTool 0.9.x"**.

    {{< figure src="migration_import_remote_existing.png" caption="Import ZIP file after the database was created" >}}

After the contents of the ZIP file were imported the database is ready for use. Start ImmoTool 1.x and create a remote project in order to connect to the database (see ["Connect to ImmoTool-Server"]({{< relref "../intro/install_server.md#intro_install_server_immotool" >}})).

{{< info >}}
After the migration was successfully finished you might remove the old installation of ImmoTool 0.9.x.
{{< /info >}}
