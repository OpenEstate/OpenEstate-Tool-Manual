---

title: Starting ImmoTool-Server
linktitle: Startup
description: How to start OpenEstate-ImmoServer…
weight: 10

menu:
  main:
    parent: admin-server
    identifier: admin-server-startup

---

## Starting ImmoTool-Server {#admin_server_startup}

The easiest way to start ImmoTool-Server is a manual startup **in foreground**.

If the application was properly configured an all workplaces can successfully connect to the ImmoTool-Server, you should consider installing a service for ImmoTool-Server. This allows the application to start automatically **in background** while the computer is booting (see ["Setup a service for ImmoTool-Server"]({{< relref "service.md#admin_server_service" >}})).


### Start ImmoTool-Server on Windows {#admin_server_startup_windows}

The Windows installer created a folder called **"OpenEstate-ImmoTool"** in the start menu, that contains the shortcuts of the application. Click on the shortcut **"Start ImmoServer manually"** in the start menu in order to start ImmoTool-Server in foreground.

Besides this you may start the application manually by executing the **`Start.exe`** (or **`Start.bat`**) file in the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}).

If ImmoTool-Server was started for the first time, the operating system may ask to allow incoming connections for ImmoTool-Server. You should answer this question by clicking the **"Allow access"** button. 

{{< figure src="startup_windows_firewall.png" caption="Grant access in the Windows firewall" >}}

{{< todo >}}
Provide an English screenshot.
{{< /todo >}}


### Start ImmoTool-Server on macOS {#admin_server_startup_mac}

Open the application bundle called **"OpenEstate-ImmoServer"** with a double click. This will open a Finder window with the applications provided by ImmoTool-Server.

{{< figure src="startup_mac_folder.png" caption="Finder window with ImmoTool-Server applications" >}}

{{< todo >}}
Provide an English screenshot.
{{< /todo >}}

A double click on the **"Start"** application will start ImmoTool-Server manually.

If ImmoTool-Server was started for the first time, the operating system may ask to allow incoming connections for ImmoTool-Server. You should answer this question by clicking the **"Allow"** button. 

{{< figure src="startup_mac_firewall.png" caption="Grant access in the macOS firewall" >}}

{{< todo >}}
Provide an English screenshot.
{{< /todo >}}


### Start ImmoTool-Server on Linux {#admin_server_startup_linux}

If ImmoTool-Server was installed with the [**Debian** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}), there is already a service available and ImmoTool-Server was already started. In this case you do not have to do any further steps.

On all Linux systems you can start ImmoTool-Server manually by executing the **`Start.sh`** script in the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}).
