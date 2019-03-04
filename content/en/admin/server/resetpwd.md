---

title: Reset the password of database users
linktitle: Reset password
description: How to reset the password of a database user in OpenEstate-ImmoServer…
weight: 60

menu:
  main:
    parent: admin-server
    identifier: admin-server-resetpwd

---

## Reset the password of a database user {#admin_server_resetpwd}

This chapter describes different approaches how to reset the password of a database user. 


### Reset the password via AdminTool {#admin_server_resetpwd_admintool}

If the password of a database user got lost, the administrator can login to [AdminTool]({{< relref "../tool.md#admin_tool" >}}) and assign a new password for the user in the user management (see ["Manage user accounts"]({{< relref "../tool.md#admin_tool_users" >}})).

{{< info >}}
As long as a password of at least one database user with administrative permissions is known this procedure can be used to reset the password of all users (even of other administrators).
{{< /info >}}


### Reset the password without administrator access {#admin_server_resetpwd_script}

If the password of the database administrator is not known anymore, you can follow these steps in order to reset the password:

1.  Stop ImmoTool-Server, if it is currently running.

2.  Open the **`db.script`** file from the database directory in a text editor. By default the database directory is placed in the **`data/immotool`** subfolder of the [data directory]({{< relref "directories.md#admin_server_directories_data" >}}).

    {{< warning >}}Create a backup of the **`db.script`** file before making any changes. Possible mistakes might lead to a defective database.{{< /warning >}}

3.  Search in the **`db.script`** file for a line starting with:
    ```
    CREATE USER SA PASSWORD DIGEST
    ```

    Replace the line with the following line:
    ```
    CREATE USER SA PASSWORD DIGEST '16d7a4fca7442dda3ad93c9a726597e4'
    ```

4.  Save the modified **`db.script`** file and restart ImmoTool-Server.

5.  The password of the database administrator **`SA`** was changed to **`test1234`**. From now on you can use this password to login to the database via AdminTool / ImmoTool.

{{< warning >}}
For security reasons you should connect to the database with [AdminTool]({{< relref "../tool.md#admin_tool" >}}) and enter a new secret password for the **"SA"** user (see ["Manage user accounts"]({{< relref "../tool.md#admin_tool_users" >}})).
{{< /warning >}}
