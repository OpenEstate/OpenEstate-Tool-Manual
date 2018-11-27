---

title: Installation im Netzwerk
linktitle: Netzwerk-Installation
description: OpenEstate-ImmoTool im Netzwerk installieren…
weight: 60

menu:
  main:
    parent: intro
    identifier: intro-install-network

---

## *ImmoTool* als Netzwerk-Version installieren {#intro_install_network}


### Was ist eine Netzwerk-Installation? {#intro_install_network_info}

Bei einer Netzwerk-Installation greifen mehrere Mitarbeiter von Ihrem Arbeitsplatz aus auf einen gemeinsamen Datenbestand zu. Die Datenbank muss für dieses Szenario in ein separates Programm "ausgelagert" werden (*ImmoTool-Server*).

Bevor das *ImmoTool* verwendet werden kann, muss daher im ersten Schritt der *ImmoTool-Server* auf **einem** Rechner in Ihrem Netzwerk installiert werden. Die Mitarbeiter greifen dann von ihren Arbeitsplätzen per *ImmoTool* auf den *ImmoTool-Server* zu. Schematisch wird dies in folgender Grafik dargestellt (Quelle [Wikipedia](http://de.wikipedia.org/wiki/Client-Server-Modell)):

{{< figure src="network_model.jpg" caption="Client-/Server-Modell" >}}

Der *ImmoTool-Server* befindet sich im Zentrum des Bildes. Die einzelnen Rechner der Mitarbeiter, welche auf den *ImmoTool-Server* zugreifen, sind im Kreis angeordnet.

> **Hinweis**
>
> Wenn Sie *ImmoTool* auf nur einem einzelnen Rechner betreiben wollen, empfiehlt sich die einfachere [Einzelplatz-Installation](install_local.md#intro_install_local).


### Vorteile einer Netzwerk-Installation {#intro_install_network_pro}

-   Beliebig viele Mitarbeiter können zeitgleich auf einem gemeinsamen Datenbestand arbeiten.
-   Jeder Mitarbeiter erhält seinen eigenen Zugang zur Datenbank (eigener Benutzername und eigenes Passwort), mit denen dieser sich bei jedem Programmstart authentifizieren muss.
-   Für jeden Mitarbeiter können Zugriffsrechte vergeben werden - sodass z.B. nur bestimmte Programmfunktionen verwendet werden können.
-   Der *ImmoTool-Server* kann auch auf einem im Rechenzentrum angemieteten Server betrieben werden - sodass auch Mitarbeiter an verschiedenen Standorten auf den gemeinsamen Datenbestand zugreifen können. Alternativ ist auch ein Zugriff von außen per [Virtual Private Network](http://de.wikipedia.org/wiki/Virtual_Private_Network) realisierbar.


### Nachteile einer Netzwerk-Installation {#intro_install_network_contra}

-   Die Installation ist komplizierter, da hier vorab der ImmoTool-Server eingerichtet werden muss. Grundkenntnisse in der Administration von Netzwerken sind hier in jedem Falle hilfreich.
-   Aktualisierungen sind komplizierter, da möglichst immer die gleiche *ImmoTool*-Version auf den Arbeitsplätzen aller Mitarbeiter verwendet werden sollte.


### Programmpakete installieren

> **TODO**
>
> Inhalte einfügen


### *ImmoTool-Server* starten {#intro_install_network_server_startup}

> **TODO**
>
> Inhalte einfügen

> **Hinweis**
>
> Um mit dem *ImmoTool-Server* über das Netzwerk kommunizieren zu können, muss eventuell eine Zugriffsregel in der Firewall hinterlegt werden. Benötigt wird in der Standardeinstellung eine Freigabe für Verbindungen auf Port-Nr `9001`.


### Datenbank im *ImmoTool-Server* einrichten {#intro_install_network_admintool_init}

> **TODO**
>
> Inhalte einfügen


### *ImmoTool* starten {#intro_install_network_immotool_startup}

> **TODO**
>
> Inhalte einfügen


### *ImmoTool* mit dem *ImmoTool-Server* verbinden {#intro_install_network_immotool_project}

> **TODO**
>
> Inhalte einfügen
