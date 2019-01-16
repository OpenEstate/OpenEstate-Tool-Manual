# Allgemeines

Die zu bearbeitenden Inhalte des deutschen Handbuchs sind im Ordner `content/de` hinterlegt. Dateien mit der Endung `.md` können in einem Texteditor bearbeitet werden. 

Folgende allgemeine Hinweise sollten bei der Bearbeitung beachtet werden: 

-   **Einen anständigen Editor verwenden:** Insbesondere unter *Windows* sollte möglichst **nicht** der Standard-Editor verwendet werden. Statt dessen wird empfohlen, das kostenlose [*Notepad++*](https://notepad-plus-plus.org/) zu verwenden.

-   **Keine manuellen Zeilenumbrüche:** Längere Absätze sollte nicht von Hand umgebrochen werden. Zur besseren Lesbarkeit bei der Bearbeitung kann statt dessen im verwendeten Editor ein automatischer Zeilenumbruch aktiviert werden.

-   **Unicode verwenden:** Die bearbeiteten Markdown-Dateien sollten mit dem Zeichensatz UTF-8 (Unicode) ohne Byte-Order-Mark (BOM) gespeichert werden. Dies kann im Editor entsprechend eingestellt werden.

-   **Unix-Zeilenumbrüche verwenden:** Die Markdown-Dateien sollten Unix-Zeilenumbrüche (`\n`) verwenden. Dies kann im Editor entsprechend eingestellt werden.

-   **Leerzeichen für Einrückungen verwenden:** Die Markdown-Dateien sollten grundsätzlich keine Tabulatoren (Tabs) enthalten.


# Markdown-Syntax

Die Inhalte sollten in [Markdown-Syntax](http://markdown.de/) verfasst werden. Abweichungen von diesem Standard sowie Besonderheiten werden im Folgenden kurz zusammengefasst.


## Metadaten

Am Anfang einer jeden Markdown-Datei sind diverse Metadaten im YAML-Format enthalten. Diese werden von *Hugo* verwendet um die Webseite zu generieren und die Inhalte an der richtigen Stelle darzustellen. Bei der Bearbeitung bestehender Markdown-Dateien sollten diese Metadaten in der Regel nicht bearbeitet werden müssen.

Weitere Informationen können der [Dokumentation des *Hugo*-Projekts](https://gohugo.io/content-management/front-matter/) entnommen werden.


## Überschriften

Überschriften sollten grundsätzlich mit einer vorangestellten Raute notiert werden. Die alternative Schreibweise

```md
Überschrift 1
=============

Überschrift 2
-------------
```

soll **nicht** verwendet werden. Statt dessen ist

```md
# Überschrift 1

## Überschrift 2
```

zu verwenden.

Darüber hinaus sollte jede Überschrift eine eigene ID definieren, welche **eindeutig innerhalb des gesamten Handbuchs** ist, z.B:

```md
## Überschrift {#my_headline}
```

Bei Übersetzungen in andere Sprachen sollten die gleichen ID's für die gleichen / übersetzten Überschriften verwendet werden.


## Links

Es sollen grundsätzlich **keine** Referenz-Links verwendet werden. Zum Beispiel

```md
Dies ist [ein Beispiel][id] für einen Referenz-Link.

[id]: http://example.com/  "Optionalen Titel hier eintragen"
```

sollte vermieden werden. Statt dessen sollte

```md
Dies ist [ein Beispiel](http://example.com/) für einen Link.
```

verwendet werden.


### Interne Links

Für Links auf andere Seiten des Handbuchs ist folgende Notation zu verwenden:

```md
Dies ist [ein Beispiel]({{< relref "another.md" >}}) für einen internen Link.
```

Wenn sich die verlinkte Datei in einem anderen Ordner befindet, sollten relative Links verwendet werden:

```md
Dies ist [ein Beispiel]({{< relref "../folder/another.md" >}}) für einen internen Link.
```

Um mit dem Link auf eine spezielle Überschrift mit der ID `my_headline` zu verweisen, kann folgende Syntax verwendet werden:

```md
Dies ist [ein Beispiel]({{< relref "another.md#my_headline" >}}) für einen internen Link.
```

Um auf eine Überschrift innerhalb der gleichen Seite zu verweisen, kann folgende Syntax verwendet werden:

```md
Dies ist [ein Beispiel](#my_headline) für einen internen Link.
```


## Bilder

Bilder sollten sich in der Regel im gleichen Ordner wie die Markdown-Datei befinden, welche sie einbindet. In diesem Fall kann ein das Bild durch folgende Syntax eingebunden werden:

```md
{{< figure src="image.jpg" caption="Untertitel des Bildes" >}}
``` 

Sollte ein Bild aus einem anderen Ordner geladen werden müssen, kann eine relative Verlinkung genutzt werden:

```md
{{< figure src="../folder/image.jpg" caption="Untertitel des Bildes" >}}
``` 


## Tabellen

Tabellen können gemäß der [Markdown-Erweiterung von GitHub](https://help.github.com/articles/organizing-information-with-tables/) genutzt werden:

```md
| Erster Titel  | Zweiter Titel |
| ------------- | ------------- |
| Inhalt        | Inhalt        |
| Inhtalt       | Inhalt        |
```

Eine perfekte Anordnung ist nicht zwingend nötig:

```md
| Befehl | Beschreibung |
| --- | --- |
| git status | Stellt bearbeitete Dateien dar |
| git diff | Stellt Unterschiede dar, die nicht übernommen wurden |
```

Text-Formatierungen innerhalb einer Zelle sind möglich:

```md
| Befehl | Beschreibung |
| --- | --- |
| `git status` | Stellt *bearbeitete Dateien* dar |
| `git diff` | Stellt Unterschiede dar, die **nicht übernommen** wurden |
```

Spalten können bei Bedarf linksbündig / mittig / rechtsbündig dargestellt werden:

```md
| linksbündig  | zentriert      | rechtsbündig  |
| :----------- | :------------: | ------------: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```


# Konventionen

Um ein einheitliches Erscheinungsbild des Handbuchs zu gewährleisten, wurden folgende Konventionen vereinbart.


## Anrede

Um einen persönlichen Bezug zum Leser des Handbuchs herzustellen, kann der Leser direkt angesprochen werden. Es soll dabei die Höflichkeitsform (Anrede mit "Sie") verwendet werden.


## Bilder

-   Bilder sollten grundsätzlich im **JPEG-Format** gespeichert werden.

-   Bilder sollten mit einer Qualitätsstufe von **75% bis 95%** gespeichert werden. Wenn die Lesbarkeit nicht negativ beeinträchtigt wird, sollte eine **möglichst geringe Qualitätsstufe** verwendet werden um den Speicherbedarf zu minimieren.

-   Bei Screenshots sollte ein möglichst passender Bildausschnitt gewählt werden, sodass nur dir relevanten (zu dokumentierenden) Elemente sichtbar sind.

-   Bei Screenshots sollten keine Fenster-Dekorationen enthalten sein. 


## Fachbegriffe / Englische Bezeichnungen

Englische Bezeichnungen sollten im deutschen Handbuch möglichst vermieden werden. Wenn englische Fachbegriffe genutzt werden, sollen diese zeitgleich im Glossar dokumentiert werden.

Folgende häufig auftretende englische Begriffe werden als bekannt vorausgesetzt und müssen nicht im Glossar dokumentiert werden: 

-   Button
-   Check-Box
-   Select-Box 
-   Tab
