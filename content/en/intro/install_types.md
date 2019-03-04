---

title: Installation types for ImmoTool
linktitle: Types of installation
description: How OpenEstate-ImmoTool can be run…
weight: 40

menu:
  main:
    parent: intro
    identifier: intro-install-types

---

## How ImmoTool can be installed… {#intro_install_types}

You may use ImmoTool in two different ways. Before installing the application you should decide for one of these usage scenarios.

{{< tip >}}
If you want to make yourself familiar with the application, it is recommended to start with a **single-user installation**. Later you may switch to multi-user installation (see ["Convert single-user into multi-user installation"]({{< relref "../admin/migration.md#admin_migration_project_local" >}})).
{{< /tip >}}


### Installing on a single workplace {#intro_install_types_local}

Using the application on a single workplace (so called **single-user installation**) is the most straightforward installation method. In this case only the ImmoTool has to be installed. The ImmoTool-Server is **not** required for this type of installation.

On the first startup of the application a database is created automatically on the local hard drive, that gathers all processed data.


#### Advantages of single-user installations {#intro_install_types_local_pros}

-   This is the most straightforward installation method. Only ImmoTool has to be installed.
-   The database is created automatically on the first startup and the application is usable without any further setup.


#### Disadvantages of single-user installations {#intro_install_types_local_cons}

-   Multiple users can not work on the same database at the same time.
-   It is not possible to set permissions for different users. The user always has full access to the database and the application features.  


#### Steps for single-user installations {#intro_install_types_local_steps}

The following steps are required in order to start with a single-user installation:

1.  [Download ImmoTool.]({{< relref "download.md#intro_download" >}})
2.  [Install ImmoTool.]({{< relref "install_client.md#intro_install_client_setup" >}})
3.  [Start ImmoTool.]({{< relref "install_client.md#intro_install_client_startup" >}})
4.  [Create a local project on first application startup.]({{< relref "install_client.md#intro_install_client_project" >}}) 


### Installing on a multiple workplaces {#intro_install_types_network}

If multiple employees should be able to work on the same database from their workplace, a so called **multi-user installation** is required. In this case the shared database has to be provided by an external application (ImmoTool-Server).

The following image illustrates the setup schematically:

{{< figure src="install_types_network.png" caption="client-server model" >}}

The ImmoTool-Server is placed in the center of the image. The employees workplaces are arranged in a circle around the ImmoTool-Server.


#### Advantages of multi-user installations {#intro_install_types_network_pros}

-   Any number of employees may work at same time on the same database.
-   Each employee has its own credentials for database access.
-   Each employee may have its own permissions within the database (e.g. accessing certain data or using certain features).
-   ImmoTool-Server may be installed in a data center. In this case employees may access the database from different locations. Alternatively the ImmoTool-Server might be made available through a [Virtual Private Network](https://en.wikipedia.org/wiki/Virtual_private_network).


#### Disadvantages of multi-user installations {#intro_install_types_network_cons}

-   The installation procedure is more complicated because the ImmoTool-Server needs to be installed separately. Basic knowledge of networks and server administrations are helpful.
-   Software updates are a bit more complicated because all workplaces should use the same ImmoTool version.


#### Steps for multi-user installations {#intro_install_types_network_steps}

A multi-user installation requires multiple steps, that need to be done on multiple computers / workplaces.

The ImmoTool-Server needs to be installed at first on **one** computer in the company network:

1.  [Download ImmoTool & ImmoTool-Server.]({{< relref "download.md#intro_download" >}})
2.  [Install ImmoTool to the server computer.]({{< relref "install_client.md#intro_install_client_setup" >}})
3.  [Install ImmoTool-Server to the server computer.]({{< relref "install_server.md#intro_install_server_setup" >}})
4.  [Start ImmoTool-Server.]({{< relref "install_server.md#intro_install_server_server_startup" >}})
5.  [Start AdminTool (provided with the ImmoTool installation) and create a database on the ImmoTool-Server.]({{< relref "install_server.md#intro_install_server_prepare" >}})
6.  [Start ImmoTool and create a remote project.]({{< relref "install_server.md#intro_install_server_immotool" >}})

{{< info >}}
The ImmoTool installation on the server computer may be removed after the initial setup was finished successfully. But in case of problems it might be helpful in the future to have an ImmoTool / AdminTool on the same system as the ImmoTool-Server.
{{< /info >}}

After the basic setup of ImmoTool-Server was completed you may consider setting up further features (e.g. [encryption]({{< relref "../admin/server/setup.md#admin_server_setup_ssl" >}}), [automatic backups]({{< relref "../admin/backup.md#admin_backup_network" >}}) or [installing a service]({{< relref "../admin/server/service.md#admin_server_service" >}})).

In the next step you have to install ImmoTool on **each workplace**:

1.  [Download ImmoTool.]({{< relref "download.md#intro_download" >}})
2.  [Install ImmoTool.]({{< relref "install_client.md#intro_install_client_setup" >}})
3.  [Start ImmoTool.]({{< relref "install_client.md#intro_install_client_startup" >}})
4.  [Create a remote project on first application startup.]({{< relref "install_server.md#intro_install_server_immotool" >}})
