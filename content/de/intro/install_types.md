---

title: Art der Installationen von ImmoTool
linktitle: Art der Installation
description: Wie OpenEstate-ImmoTool betrieben werden kann…
weight: 40

menu:
  main:
    parent: intro
    identifier: intro-install-types

---

## Wie ImmoTool betrieben werden kann… {#intro_install_types}

Das ImmoTool kann auf zweierlei Arten betrieben werden. Bevor Sie das Programm in Betrieb nehmen, sollten Sie sich für eines der beiden Szenarien entscheiden.

{{< tip >}}
Es ist allgemein jederzeit möglich von einer Einzelplatz-Installation in eine Mehrplatz-Installation umzusteigen (oder anders herum). 

Wenn Sie sich mit dem Programm vertraut machen möchten, empfehlen wir daher erst mal eine **Einzelplatz-Installation** durchzuführen und später ggf. umzusteigen (siehe ["Einzelplatz- in Mehrplatz-Projekt umwandeln"]({{< relref "../admin/migration.md#admin_migration_project_local" >}})). 
{{< /tip >}}  


### Betrieb an einem einzelnen Arbeitsplatz {#intro_install_types_local}

Die einfachste Form der Nutzung ist die Installation des Programms an einem einzelnen Arbeitsplatz (sogenannte **Einzelplatz-Installation**). In diesem Falle stellt das ImmoTool selbst alle nötigen Funktionen bereit. Der ImmoTool-Server muss in diesem Szenario **nicht** installiert werden.

Beim Programmstart wird automatisch eine Datenbank auf dem Rechner des Anwenders erstellt, in der alle erfassten Daten (Immobilien, Kunden, etc.) gespeichert werden.


#### Vorteile einer Einzelplatz-Installation {#intro_install_types_local_pros}

-   Dies ist die einfachst mögliche Form das ImmoTool in Betrieb zu nehmen, da nur ein einziges Programm installiert und gestartet werden muss.
-   Beim ersten Programmstart wird automatisch die Datenbank auf der Festplatte erzeugt und man kann sofort und ohne weiteren Aufwand mit der Arbeit beginnen.


#### Nachteile einer Einzelplatz-Installation {#intro_install_types_local_cons}

-   Die Datenbank einer Einzelplatz-Installation kann nicht von mehreren Mitarbeitern gleichzeitig geöffnet werden.
-   Es gibt keine Möglichkeiten zur Vergabe von Berechtigungen für verschiedene Mitarbeiter. Bei einer Einzelplatz-Installation hat man grundsätzlich immer alle Berechtigungen.


#### Eine Einzelplatz-Installation durchführen {#intro_install_types_local_steps}

Für eine Einzelplatz-Installation sind folgende Schritte durchzuführen:

1.  [ImmoTool herunterladen.]({{< relref "download.md#intro_download" >}})
2.  [ImmoTool installieren.]({{< relref "install_client.md#intro_install_client_setup" >}})
3.  [ImmoTool starten.]({{< relref "install_client.md#intro_install_client_startup" >}})
4.  [Beim ersten Programmstart ein Einzelplatz-Projekt anlegen.]({{< relref "install_client.md#intro_install_client_project" >}}) 


### Betrieb an mehreren Arbeitsplätzen {#intro_install_types_network}

Wenn mehrere Mitarbeiter von Ihrem Arbeitsplatz aus mit dem ImmoTool auf einen gemeinsamen Datenbestand arbeiten sollen, ist eine sogenannte **Netzwerk-Installation** nötig. Die gemeinsam genutzte Datenbank muss in diesem Falle in ein separates Programm ausgelagert werden (ImmoTool-Server). 

Schematisch wird dies in folgender Grafik dargestellt (Quelle [Wikipedia](http://de.wikipedia.org/wiki/Client-Server-Modell)):

{{< figure src="install_types_network.png" caption="Client-/Server-Modell" >}}

Der ImmoTool-Server befindet sich im Zentrum des Bildes. Die einzelnen Arbeitsplätze der Mitarbeiter, welche auf den ImmoTool-Server zugreifen, sind im Kreis angeordnet.


#### Vorteile einer Netzwerk-Installation {#intro_install_types_network_pros}

-   Beliebig viele Mitarbeiter können zeitgleich auf einem gemeinsamen Datenbestand arbeiten.
-   Jeder Mitarbeiter erhält seinen eigenen Zugang zur Datenbank (eigener Benutzer-Name und eigenes Passwort), mit denen dieser sich bei jedem Programmstart authentifiziert.
-   Für jeden Mitarbeiter können Zugriffsrechte vergeben werden - sodass z.B. nur bestimmte Funktionen des Programms verwendet werden können.
-   Der ImmoTool-Server kann auch auf einem im Rechenzentrum angemieteten Server betrieben werden - sodass auch Mitarbeiter an verschiedenen Standorten auf den gemeinsamen Datenbestand zugreifen können. Alternativ ist auch ein Zugriff von außen per [Virtual Private Network](http://de.wikipedia.org/wiki/Virtual_Private_Network) realisierbar.


#### Nachteile einer Netzwerk-Installation {#intro_install_types_network_cons}

-   Die Installation ist komplizierter, da hier vorab der ImmoTool-Server eingerichtet werden muss. Grundkenntnisse in der Administration von Netzwerken sind hier in jedem Falle hilfreich.
-   Aktualisierungen sind komplizierter, da möglichst immer die gleiche ImmoTool-Version auf den Arbeitsplätzen aller Mitarbeiter verwendet werden sollte.


#### Eine Netzwerk-Installation durchführen {#intro_install_types_network_steps}

Für eine Netzwerk-Installation sind mehrere Schritte nötig, die auf den verschiedenen Rechnern / Arbeitsplätzen durchzuführen sind.

Zu erst muss der ImmoTool-Server auf **einem** Rechner im Firmennetzwerk installiert werden:

1.  [ImmoTool & ImmoTool-Server herunterladen.]({{< relref "download.md#intro_download" >}})
2.  [ImmoTool auf dem Server-Rechner installieren.]({{< relref "install_client.md#intro_install_client_setup" >}})
3.  [ImmoTool-Server auf dem Server-Rechner installieren.]({{< relref "install_server.md#intro_install_server_setup" >}})
4.  [ImmoTool-Server starten.]({{< relref "install_server.md#intro_install_server_server_startup" >}})
5.  [Das aus dem ImmoTool-Paket installierte AdminTool starten um die Datenbank einzurichten.]({{< relref "install_server.md#intro_install_server_prepare" >}})
6.  [ImmoTool starten und ein Mehrplatz-Projekt mit den Zugangsdaten des ImmoTool-Servers anlegen.]({{< relref "install_server.md#intro_install_server_immotool" >}})

{{< info >}}
Das auf dem Server-Rechner installierte ImmoTool kann nach erfolgreicher Einrichtung bei Bedarf wieder entfernt werden. Es kann jedoch hilfreich sein, für administrative Zwecke direkt auf dem Server-Rechner immer das ImmoTool und AdminTool vorliegen zu haben. 
{{< /info >}}

Die grundlegende Einrichtung des ImmoTool-Servers ist damit abgeschlossen. Weitere Funktionen (z.B. [Verschlüsselung]({{< relref "../admin/server/setup.md#admin_server_setup_ssl" >}}), [automatische Datensicherung]({{< relref "../admin/backup.md#admin_backup_network" >}}) oder [Einrichtung als Dienst]({{< relref "../admin/server/service.md#admin_server_service" >}})) können darüber hinaus noch konfiguriert werden.

Im nächsten Schritt muss auf **jedem Arbeitsplatz** das ImmoTool installiert werden:

1.  [ImmoTool herunterladen.]({{< relref "download.md#intro_download" >}})
2.  [ImmoTool installieren.]({{< relref "install_client.md#intro_install_client" >}})
3.  [ImmoTool starten.]({{< relref "install_client.md#intro_install_client_startup" >}})
4.  [Beim ersten Programmstart ein Mehrplatz-Projekt mit den Zugangsdaten des ImmoTool-Servers anlegen.]({{< relref "install_server.md#intro_install_server_immotool" >}})
