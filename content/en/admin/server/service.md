---

title: Setup a service for ImmoTool-Server
linktitle: Setup service
description: How to setup a service OpenEstate-ImmoServer in the operating system…
weight: 40

menu:
  main:
    parent: admin-server
    identifier: admin-server-service

---

## Setup a service for ImmoTool-Server {#admin_server_service}

For the everyday operations it is useful to integrate ImmoTool-Server as a service into the operating system. This allows ImmoTool-Server to start **automatically** in background while the system is booting. The administrator can control the service from the outside (start / stop / restart). 


### Setup service on Windows {#admin_server_service_windows}

In order to install and control the service for ImmoTool-Server on Windows systems the Open Source software [commons-daemon](https://commons.apache.org/daemon/) provided by the [Apache Software Foundation](https://apache.org/) is used. The applications in the **`bin\service`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) are provided by the "commons-daemon" project.


#### Install service on Windows {#admin_server_service_windows_install}

The service for ImmoTool-Server can be registered in the operating system in the following ways:

-   Open the start menu and select the shortcut **"OpenEstate-ImmoServer → Service → Install ImmoServer service"**.

-   Open the **`bin`** subfolder in the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the **`ServiceInstall.bat`** script with a double click.

Because services can only be registered by an administrator the operating system might ask for administrative permissions.

After the service was successfully installed a dialog window will show up, which allows further configuration.

{{< figure src="service_windows_install.png" caption="Manage the service on Windows" >}}

For example you might change the path of the application directories in the **"Java"** tab  (see ["Directories of ImmoTool-Server"]({{< relref "directories.md#admin_server_directories" >}})):

{{< figure src="directories_setup_windows_service.png" caption="Change directories in service management application" >}}

After settings were changed click on the **"Submit"** button. You can close the dialog window afterwards or start the service in the **"General"** tab by clicking the **"Start"** button.

If ImmoTool-Server was started for the first time, the operating system may ask to allow incoming connections for ImmoTool-Server. You should answer this question by clicking the **"Allow access"** button. 

{{< figure src="startup_windows_firewall.png" caption="Grant access in the Windows firewall" >}}


#### Uninstall service on Windows {#admin_server_service_windows_uninstall}

The service for ImmoTool-Server can be removed from the operating system in the following ways:

-   Open the start menu and select the shortcut **"OpenEstate-ImmoServer → Service → Uninstall ImmoServer service"**.

-   Open the **`bin`** subfolder in the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the **`ServiceUninstall.bat`** script with a double click.

A command line window will show up, which removes the service from the operating system. You will see a success or error message in this window after the application was finished.

{{< info >}}
If ImmoTool-Server is regularly uninstalled, a previously registered service is automatically removed.
{{< /info >}}


#### Manage service on Windows {#admin_server_service_windows_manage}

ImmoTool-Server provides an application for management / configuration of the service. You may start the application in one of the following ways:

-   Open the start menu and select the shortcut **"OpenEstate-ImmoServer → Service → Manage ImmoServer service"**.

-   Open the **`bin\service`** subfolder in the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the **`OpenEstate-ImmoServer.exe`** application with a double click.

This application provided by the Apache Software Foundation allows modification of the service. Also the service can be started / stopped from this application.  

Alternatively you might use the service management provided by the Windows operating system.

1.  Press the **"Windows key"** together with the letter **"R"** to open a window for command execution. Alternatively you can open the command prompt.

2.  Enter the command **`services.msc`** and press the **"ENTER"** key.

The service management window provided by the Windows operating system will show up:

{{< figure src="service_windows_manage.png" caption="Windows service management" >}}

You might start / stop the service in this window or edit certain settings with a double click.

{{< todo >}}
Provide an English screenshot.
{{< /todo >}}


#### Start service on Windows {#admin_server_service_windows_start}

After the service was installed (see ["Install service on Windows"]({{< relref "service.md#admin_server_service_windows_install" >}})) you might start the service manually in of these ways:

-   Open the start menu and select the shortcut **"OpenEstate-ImmoServer → Service → Start ImmoServer service"**.

-   Open the **`bin`** subfolder in the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the **`ServiceStart.bat`** script with a double click.

-   Open the provided service management application and click the **"Start"** button (see ["Manage service on Windows"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

-   Open the service dialog of the Windows operating system, select the service **"OpenEstate-ImmoServer"** and click on the top left at **"Start the service"** button (see ["Manage service on Windows"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

{{< todo >}}
Figure out the correct naming in the Windows service dialog.
{{< /todo >}}

{{< info >}}
By default the service will **start automatically** while the Windows system is booting. Therefore in most cases it is not possible to start the service manually. 
{{< /info >}}


#### Stop service on Windows {#admin_server_service_windows_stop}

After the service was installed (see ["Install service on Windows"]({{< relref "service.md#admin_server_service_windows_install" >}})) you might stop the service manually in of these ways:

-   Open the start menu and select the shortcut **"OpenEstate-ImmoServer → Service → Stop ImmoServer service"**.

-   Open the **`bin`** subfolder in the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the **`ServiceStop.bat`** script with a double click.

-   Open the provided service management application and click the **"Stop"** button (see ["Manage service on Windows"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

-   Open the service dialog of the Windows operating system, select the service **"OpenEstate-ImmoServer"** and click on the top left at **"Stop the service"** button (see ["Manage service on Windows"]({{< relref "service.md#admin_server_service_windows_manage" >}})).

{{< todo >}}
Figure out the correct naming in the Windows service dialog.
{{< /todo >}}


### Setup service on macOS {#admin_server_service_mac}

On macOS the service is controlled with the [launchd](https://en.wikipedia.org/wiki/Launchd) application, which is part of the operating system. The service is registered by creating a file called **`org.openestate.tool.server.service.plist`** in the **`/Library/LaunchDaemons`** directory.

{{< info >}}
You might modify the created service file by yourself in order to make individual adjustments (see [tutorial for launchd](http://www.launchd.info/)). But in most cases this should not be necessary.
{{< /info >}}


#### Install service on macOS {#admin_server_service_mac_install}

Open the application bundle **"OpenEstate-ImmoServer"** and start the **"ServiceInstall"** application. A terminal window will show up, which will guide you through the installation of the service.

{{< figure src="service_linux_install_settings.png" caption="Installing the service on macOS" >}}

The application requires administrative permissions. While the application is running you might get asked for an administrator password. 

You can select the following options during the installation of the service:

-   You can enter the user name, that executes ImmoTool-Server.

-   You can enter the group name, that executes ImmoTool-Server.

-   You might enable a timer for daily automatic backups (see ["Automatic backup on macOS"]({{< relref "../backup.md#admin_backup_network_live_mac" >}})). In order to make these backups work properly you also have to configure the manager applications properly (siehe ["Configure manager applications"]({{< relref "setup.md#admin_server_setup_manager" >}})).

If all questions have been answered, the service file **`org.openestate.tool.server.service.plist`** is created in the **`/Library/LaunchDaemons`** directory.

{{< figure src="service_mac_install_summary.png" caption="Summary after the service was installed on macOS" >}}

Beim ersten Start des ImmoTool-Servers werden Sie vom Betriebssystem eventuell gefragt, ob eingehende Verbindungen akzeptiert werden sollen. Diese Frage sollte mit **"Erlauben"** beantwortet werden.

{{< figure src="startup_mac_firewall.png" caption="Grant access in the macOS firewall" >}}


#### Uninstall service on macOS {#admin_server_service_mac_uninstall}

Open the application bundle **"OpenEstate-ImmoServer"** and start the **"ServiceUninstall"** application. A terminal window will show up, which will remove the service from the operating system.

The application requires administrative permissions. While the application is running you might get asked for an administrator password. 


#### Start service on macOS {#admin_server_service_mac_start}

After the service was installed (see ["Install service on macOS"]({{< relref "service.md#admin_server_service_mac_install" >}})) you might start the service manually in of these ways:

-   Open the application bundle **"OpenEstate-ImmoServer"** and start the **"ServiceStart"** application.

-   Open the Terminal and execute the following command:

    ```bash
    sudo launchctl start org.openestate.tool.server.service
    ```

{{< info >}}
By default the service will **start automatically** while the macOS system is booting. Therefore in most cases it is not possible to start the service manually. 
{{< /info >}}


#### Stop service on macOS {#admin_server_service_mac_stop}

After the service was installed (see ["Install service on macOS"]({{< relref "service.md#admin_server_service_mac_install" >}})) you might stop the service manually in of these ways:

-   Open the application bundle **"OpenEstate-ImmoServer"** and start the **"ServiceStop"** application.

-   Open the Terminal and execute the following command:

    ```bash
    sudo launchctl stop org.openestate.tool.server.service
    ```


### Setup service on Linux {#admin_server_service_linux}

On Linux the service is controlled with the [systemd](https://en.wikipedia.org/wiki/Systemd) application, which is part of the operating system. The service is registered by creating a file called **`openestate-immoserver.service`** in the **`/etc/systemd/system`** directory.

{{< warning >}}
Most Linux distributions are using "systemd". To be on the safe side you should check, if you operating system also uses this software, before the service is installed.
{{< /warning >}}

{{< info >}}
You might modify the created service file by yourself in order to make individual adjustments (see [manual of launchd](https://www.freedesktop.org/software/systemd/man/systemd.service.html)). But in most cases this should not be necessary.
{{< /info >}}


#### Install service on Linux {#admin_server_service_linux_install}

If ImmoTool-Server was installed with the [**Debian** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_debian" >}}), the service is already installed. In this case **no further steps are necessary** to install the service.

If ImmoTool-Server was installed with the [**TAR.GZ** package]({{< relref "../../intro/install_server.md#intro_install_server_setup_linux" >}}), open the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the **`ServiceInstall.sh`** script.

{{< figure src="service_linux_install_settings.png" caption="Installing the service on Linux" >}} 

The application requires administrative permissions. While the application is running you might get asked for an administrator password.

You can select the following options during the installation of the service:

-   You can enter the user name, that executes ImmoTool-Server.

-   You can enter the group name, that executes ImmoTool-Server.

-   You might enable a timer for daily automatic backups (see ["Automatic backup on Linux"]({{< relref "../backup.md#admin_backup_network_live_linux" >}})). In order to make these backups work properly you also have to configure the manager applications properly (siehe ["Configure manager applications"]({{< relref "setup.md#admin_server_setup_manager" >}})).

If all questions have been answered, the service file **`openestate-immoserver.service`** is created in the **`/etc/systemd/system`** directory.

{{< figure src="service_linux_install_summary.png" caption="Summary after the service was installed on Linux" >}}


#### Uninstall service on Linux {#admin_server_service_linux_uninstall}

Open the **`bin`** subfolder in the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the **`ServiceUninstall.sh`** script.

The application requires administrative permissions. While the application is running you might get asked for an administrator password.


#### Start service on Linux {#admin_server_service_linux_start}

After the service was installed (see ["Install service on Linux"]({{< relref "service.md#admin_server_service_linux_install" >}})) you might start the service manually in of these ways:

-   Open the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the  **`ServiceStart.sh`** script.

-   Open the console and execute the following command:

    ```bash
    sudo systemctl start openestate-immoserver
    ```

{{< info >}}
Standardmäßig wird der Dienst unter Linux **automatisch gestartet** sobald der Rechner hochgefahren wird. Daher ist es in der Regel nicht nötig den Dienst von Hand zu starten.
{{< /info >}}


#### Stop service on Linux {#admin_server_service_linux_stop}

After the service was installed (see ["Install service on Linux"]({{< relref "service.md#admin_server_service_linux_install" >}})) you might stop the service manually in of these ways:

-   Open the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}) and start the  **`ServiceStop.sh`** script.

-   Open the console and execute the following command:

    ```bash
    sudo systemctl stop openestate-immoserver
    ```
