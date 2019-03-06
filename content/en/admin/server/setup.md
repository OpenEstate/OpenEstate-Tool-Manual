---

title: Configure ImmoTool-Server
linktitle: Configuration
description: How to configure OpenEstate-ImmoServer…
weight: 30

menu:
  main:
    parent: admin-server
    identifier: admin-server-setup

---

## Configure ImmoTool-Server {#admin_server_setup}

The [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}) of ImmoTool-Server contains several files to customize the default behaviour of the application.

{{< info >}}
In most use cases the provided default configuration is sufficient. You should only change the configuration, if it is really necessary.
{{< /info >}}


### Configure databases {#admin_server_setup_databases}

The [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}) of ImmoTool-Server contains a file called **`server.properties`**. With this file the databases provided by ImmoTool-Server can be configured.

By default ImmoTool-Server provides exactly one database with the name **"immotool"**. When necessary you may provide more databases with ImmoTool-Server by editing the **`server.properties`** file. You can find further information about this configuration file in the [HSQLDB documentation](http://hsqldb.org/doc/2.0/guide/listeners-chapt.html#lsc_server_props).

For example to register a second database called **"immotool2"** in ImmoTool-Server, you can follow these steps:

1.  Stop ImmoTool-Server, if it is currently running.

2.  Open the **`server.properties`** file with a text editor and add the following lines to the end of the file:

    ```ini
    # database #1
    server.database.1=file:${openestate.server.varDir}/data/immotool2/db
    server.dbname.1=immotool2
    ```

    This registers a second database called **"immotool2"**. Its data is stored in the [data directory]({{< relref "directories.md#admin_server_directories_data" >}}) in the **`data/immotool2`** subfolder.

3.  Save the modified **`server.properties`** file and restart ImmoTool-Server.

4.  Start AdminTool and create a connection to the newly created database (see ["Prepare ImmoTool-Server"]({{< relref "../../intro/install_server.md#intro_install_server_prepare" >}})). Enter the database name **"immotool2"** in the connection dialog window in order to connect to the newly created database.

5.  After the database was prepared with AdminTool it can be accessed with ImmoTool (see ["Connect to ImmoTool-Server"]({{< relref "../../intro/install_server.md#intro_install_server_immotool" >}})). Enter the database name **"immotool2"** in the project wizard (or login) window in order to connect to the newly created database.

In general ImmoTool-Server can provide an **arbitrary number of databases** in the **`server.properties`** file with freely choosable name. For each database you need to increment the counter - e.g.:

```ini
# database #0
server.database.0=file:${openestate.server.varDir}/data/immotool/db
server.dbname.0=immotool

# database #1
server.database.1=file:${openestate.server.varDir}/data/mydb/db
server.dbname.1=mydb

# database #2
server.database.2=file:${openestate.server.varDir}/data/anotherdb/db
server.dbname.2=anotherdb
```

{{< info >}}
The character string **`${openestate.server.varDir}`** is automatically replaced with the configured path of the [data directory]({{< relref "directories.md#admin_server_directories_data" >}}).
{{< /info >}}


### Configure protocols {#admin_server_setup_logging}

The [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}) of ImmoTool-Server contains a file called **`log4j.properties`**. With this file the logging behaviour of ImmoTool-Server can be configured.

By default the application stores its protocols into the [protocol directory]({{< relref "directories.md#admin_server_directories_log" >}}). In most cases it is not necessary to make any changes to this file. But you can find further information about customization in the [documentation of log4j](https://logging.apache.org/log4j/1.2/manual.html).

{{< info >}}
The character string **`${openestate.server.logDir}`** in the **`log4j.properties`** file is automatically replaced with the configured path of the [protocol directory]({{< relref "directories.md#admin_server_directories_log" >}}).
{{< /info >}}

{{< info >}}
The character string **`${openestate.server.app}`** in the **`log4j.properties`** file is automatically replaced with the name of the executing application. This allows every application to use a separate log file.
{{< /info >}}


### Configure manager applications {#admin_server_setup_manager}

ImmoTool-Server provides some helper applications to cover some administrative tasks (so called "manager applications"). These application are connecting themselves to the databases provided by the ImmoTool-Server in order to do their work (e.g. ["Backup a running ImmoTool-Server"]({{< relref "../backup.md#admin_backup_network_live" >}})).  

The manager applications need to open a connection to the provided database and login with administrative permissions. Therefore it is necessary to tell these application with which credentials to login. The required login credentials have to be placed in the **`manager.conf`** file within the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}).

For each database, that is provided by ImmoTool-Server, you need to add the following lines into the **`manager.conf`** file:

```ini
urlid immotool
url jdbc:hsqldb:hsql://localhost:9001/immotool
username SA
password test1234
```

-   The value after **`urlid`** is a unique name for the database connection. To simplify matters you should use the database name here.

-   The value after **`url`** is the database address used for the connection. 

    -   If the manager applications are executed from the same system as the ImmoTool-Server, you can use the **"localhost"** address. Otherwise you should enter the IP address or hostname. If ImmoTool-Server was configured for SSL encryption, you have to use the hostname specified in the SSL certificate.
    
    -   After the **"localhost"** (separated by a colon) address follows the configured port number. In most cases you can keep the number **"9001"** untouched.
    
    -   After the port number **"9001"** (separated by a forward slash) you have to set the name of the configured database (as it is configured as **`server.dbname`** in the **`server.properties`** file).
    
    -   If the ImmoTool-Server was configured for SSL encryption, you need to replace **`hsql://`** with **`hsqls://`**.

-   The value after **`username`** contains the login name of the database administrator. By default each database has an administrator account called **"SA"**. In most cases you do not need to change this value.

-   The value after **`password`** is the password for the user specified by **`username`**. Enter the password of the administrator here, that was chosen during the server preparation with AdminTool (see ["Prepare ImmoTool-Server"]({{< relref "../../intro/install_server.md#intro_install_server_prepare" >}})).

For the three example databases described in the ["Configure databases"]({{< relref "setup.md#admin_server_setup_databases" >}}) chapter, you would have to put the following lines into the **`manager.conf`** file:

```ini
urlid immotool
url jdbc:hsqldb:hsql://localhost:9001/immotool
username SA
password test1234

urlid mydb
url jdbc:hsqldb:hsql://localhost:9001/mydb
username SA
password test2345

urlid anotherdb
url jdbc:hsqldb:hsql://localhost:9001/anotherdb
username SA
password test3456
```

(Replace the password accordingly.)

You can find furter information about this configuration file in the [HSQLDB documentation](http://hsqldb.org/doc/2.0/util-guide/sqltool-chapt.html#sqltool_auth-sect).

{{< warning >}}
The **`manager.conf`** contains sensitive information. Only the users of the operating system, who are allowed to use the manager applications, should be able to read this file.  
{{< /warning >}}


### Configure SSL encryption {#admin_server_setup_ssl}

If ImmoTool-Server was installed outside of the local network or if connections from the internet are allowed, it is recommended to use encrypted communication between ImmoTool and ImmoTool-Server.

In other cases it also might make sense to use encryption because it improves security and integrity during data transfers. But keep in mind, that encryption will slow down the connection speed a bit and will increase the amount of computation time.

{{< info >}}
ImmoTool-Server does **not** allow to use encrypted and unencrypted at the same time. You need to decide which way you want to go and have to configure **all** ImmoTool installations in your network accordingly (see ["Use SSL encryption in ImmoTool"]({{< relref "setup.md#admin_server_setup_ssl_immotool" >}})).
{{< /info >}}


#### Create SSL certificate {#admin_server_setup_ssl_cert}

In order to provide SSL encryption you need to create a SSL certificate in the first step. The certificate ensures the trustworthiness of ImmoTool-Server towards the client applications.

ImmoTool-Server provides an application for easily creating a SSL certificate.

-   On Windows systems you can select the following start menu entry **"OpenEstate-ImmoServer → Management → Create SSL certificate"** to start the application.

-   On macOS systems you can open the application bundle **"OpenEstate-ImmoServer"** and start the **"SslInit"** application.

-   Alternatively you can open the **`bin`** subfolder of the [application directory]({{< relref "directories.md#admin_server_directories_application" >}}). From there you can start the application via **`SslInit.exe`** / **`SslInit.bat`** / **`SslInit.sh`**.

After the application was started a terminal window will show up with the following output:

{{< figure src="setup_ssl_cert_settings.png" caption="Configure the SSL certificate" >}}

1.  Enter the **IP address** (or hostname), that is used for connection to the ImmoTool-Server. The SSL certificate is created exactly for this address. All applications, that are connecting to ImmoTool-Server, will have to use the provided address. 

2.  In the next step you have to enter a **keystore password**, that is used to protect the certificate from external modification. Note down the chosen password because it is needed afterwards.

After these settings were entered the application will create a **`ssl`** subfolder in the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}). All created files are stored into this folder. The following summary is shown after the program finished its job: 

{{< figure src="setup_ssl_cert_summary.png" caption="Summary about the SSL certificate" >}}

{{< warning >}}
The **`ssl`** subfolder in the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}) contains sensitive information. Only the users of the operating system, who are allowed to start ImmoTool-Server, should be able to read this file.  
{{< /warning >}}

{{< info >}}
As an alternative to the application you can create the SSL certificate manually with the following commands:

```bash
keytool -genkey \
  -alias OpenEstate-ImmoServer \
  -keyalg RSA -validity 999 \
  -keystore keystore.jks \
  -storetype JKS

keytool -export \
  -alias OpenEstate-ImmoServer \
  -keystore keystore.jks \
  -rfc -file private.crt
```

The **`keytool`** application is located in the **`bin`** subfolder of the Java runtime environment.

The files created by the **`keytool`** applications have to be placed into the **`ssl`** subfolder of the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}).
{{< /info >}}


#### Enable SSL encryption {#admin_server_setup_ssl_enable}

In the next step SSL encryption has to be enabled in the ImmoTool-Server. Edit the **`server.properties`** file in the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}) with a text editor. The following lines need to be changed:

```
# TLS/SSL (secure) sockets
server.tls=true
system.javax.net.ssl.keyStore=${openestate.server.etcDir}/ssl/keystore.jks
system.javax.net.ssl.keyStorePassword=test1234
```

-   The value after **`server.tls`** has to be set to **`true`** in order to enable SSL encryption.

-   The value after **`system.javax.net.ssl.keyStore`** contains the path to the previously created keystore file (**`keystore.jks`**). In most cases you do **not** need to change this value.

-   The value after **`system.javax.net.ssl.keyStorePassword`** is the keystore password, that was chosen during the creation of the SSL certificate.

Restart ImmoTool-Server in order to make the changes take effect. 

{{< info >}}
The character string **`${openestate.server.etcDir}`** is automatically replaced with the configured path of the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}).
{{< /info >}}


#### Use SSL encryption in ImmoTool {#admin_server_setup_ssl_immotool}

If a new remote project is created in ImmoTool, you need to select the protocol **"hsqls"** in the *project wizard* dialog.

{{< todo >}}
Add link to the project wizard in the usage section.
{{< /todo >}}

{{< figure src="setup_ssl_immotool_project.png" caption="Enable SSL encryption in the project wizard" >}}

If an existing remote project is opened, you might also enable SSL encryption. Click on the **"Modify server connection settings."** checkbox and select the protocol **"hsqls"**. This setting is stored permanently for the project and does not have to be set again.

{{< figure src="setup_ssl_immotool_login.png" caption="Enable SSL encryption during login" >}}


#### Use SSL encryption in AdminTool {#admin_server_setup_ssl_admintool}

If a connection is established with AdminTool, you need to select the protocol **"hsqls"** in the connection dialog.

{{< figure src="setup_ssl_admintool.png" caption="Enable SSL encryption in AdminTool" >}}


#### Use SSL encryption in manager applications {#admin_server_setup_ssl_manager}

The manager application are configured with the **`manager.conf`** file in the [configuration directory]({{< relref "directories.md#admin_server_directories_etc" >}}).

Modify this file with a text editor and update the value behind **`url`** for all configured databases. 

-   Instead of **`hsql://`** you need to use **`hsqls://`**. 
-   Replace **`localhost`** with the hostname, that was chosen while creating the SSL certificate.

The three example databases from the ["Configure manager applications"]({{< relref "setup.md#admin_server_setup_manager" >}}) chapter would have to be changed like this:

```ini
urlid immotool
url jdbc:hsqldb:hsqls://192.168.178.123:9001/immotool
username SA
password test1234

urlid mydb
url jdbc:hsqldb:hsqls://192.168.178.123:9001/mydb
username SA
password test2345

urlid anotherdb
url jdbc:hsqldb:hsqls://192.168.178.123:9001/anotherdb
username SA
password test3456
```
