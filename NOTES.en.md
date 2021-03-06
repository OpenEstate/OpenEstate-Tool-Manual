# General remarks

The `content` folder contains the development files of the manual. Each language is placed in a separate subdirectory - e.g. `content/en` contains the English documentation files. Files with the `.md` suffix can be edited with your preferred text editor.

Please take the following general remarks into consideration: 

-   **Use a decent text editor:** Especially on *Windows* you should **not** use the default editor (*Notepad*). Instead it is recommended to use the free [*Notepad++*](https://notepad-plus-plus.org/).

-   **No manual line breaks:** You should not break longer paragraphs manually. Each paragraph should be placed on a single line. For better readability you might enable automatic line breaks in your text editor.

-   **Use Unicode:** The Markdown files should be saved with UTF-8 (Unicode) charset without Byte-Order-Mark (BOM). Please setup your text editor accordingly.

-   **Use Unix line breaks:** The Markdown files should use Unix line breaks (`\n`). Please setup your text editor accordingly.

-   **Use spaces for indentations:** The Markdown files should not contain of tabulators. Always use spaces for indentations.


# Markdown syntax

The contents are composed in [Markdown-Syntax](https://daringfireball.net/projects/markdown/). There are some deviations and exceptions to the Markdown specification documented below.


## Metadata

Each Markdown file contains some metadata at the beginning in YAML format. These data is used by *Hugo* in order to generate the website and place the content at the right place. In most cases there is no need to edit this metadata.

You can find further information about the metadata in the [documentation of the *Hugo* project](https://gohugo.io/content-management/front-matter/).


## Headlines

Headlines should always be marked with a hash character. The alternative notation should **not** be used:

```md
Headline 1
==========

Headline 2
----------
```

Instead you should use:

```md
# Headline 1

## Headline 2
```

Besides this you should define an ID for each headline, which should be **unique** throughout the whole manual - e.g.:

```md
## Überschrift {#my_headline}
```

The same ID should be used, if the headline is translated into other languages.


## Links

Don't use reference links like:

```md
This is [an example][id] for a reference link.

[id]: http://example.com/  "an optional title"
```

Instead you should always use this notation:

```md
This is [an example](http://example.com/) for a link.
```


### Internal links

Use the following notation for links, that point to other pages of the manual:

```md
This is [an example]({{< relref "another.md" >}}) for an internal link.
```

Use a relative path, if the target page is placed in another folder:

```md
This is [an example]({{< relref "../folder/another.md" >}}) for an internal link.
```

Use the following notation in order to link to a certain headline of another page with the ID `my_headline`:

```md
This is [an example]({{< relref "another.md#my_headline" >}}) for an internal link.
```

Use the following notation in order to point to another headline on the same page:

```md
This is [an example](#my_headline) for an internal link.
```


## Images

Images should be placed in the same folder as the referencing Markdown file. In this case use the following notation to embed an image file:

```md
{{< figure src="image.png" caption="subtitle of the image" >}}
``` 

In the rare case, that the embedded image is already placed in another folder, you can use a relative path: 

```md
{{< figure src="../folder/image.png" caption="subtitle of the image" >}}
``` 


## Tables

You can enter tables according to notation of [GitHub flavored Markdown](https://help.github.com/articles/organizing-information-with-tables/): 

```md
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
```

It is not necessary to align columns exactly:

```md
| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |
```

Within a table you might also use text formatting:

```md
| Command | Description |
| --- | --- |
| `git status` | List all *new or modified* files |
| `git diff` | Show file differences that **haven't been** staged |
```

You might align columns left, centered or right:

```md
| Left-aligned | Center-aligned | Right-aligned |
| :----------- | :------------: | ------------: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```


## Special text blocks (notes, warnings, tips, to-do)

You can mark one or more paragraphs as **"information"** with the following syntax:

```md
{{< info >}}
This section is shown as information message.
{{< /info >}}
```

You can mark one or more paragraphs as **"warning"** with the following syntax:

```md
{{< warning >}}
This section is shown as warning message.
{{< /warning >}}
```

You can mark one or more paragraphs as **"tip"** with the following syntax:

```md
{{< tip >}}
This section is shown as tip message.
{{< /tip >}}
```

You can mark one or more paragraphs as **"to-do"** with the following syntax:

```md
{{< todo >}}
This section is shown as to-do message.
{{< /todo >}}
```

You can use any Markdown code within those special text sections (e.g. links, images).


# Conventions

In order to have a consistent appearance, we've declared some further conventions.


## Form of address

The reader can be approached directly with "you". In case you're translating into other languages then English, use the polite form of the language.


## Images

-   In most cases images should always be provided in **PNG format**.

    -   Always use **maximal compression** (level 9).
    
    -   Don't save a preview, EXIF data, XMP data und IPTC data into the PNG file. 
    
    -   In case the image contains transparency, always include a white background.

-   In case a PNG image consumes relatively much disk space despite of the above conditions, you might also use the **JPEG format**.

    -   Images in JPEG format should be saved with a quality level of **90%**.
    
    -   If the JPEG format does not save at least 20% compared to a PNG file, the PNG format should be preferred.

-   Images should be saved with a print resolution of at least 144 pixel per inch (bzw. 144 dpi).

-   Screenshots should be cropped, that only the necessary / documented elements are visible.  

-   If a screenshot is relevant for multiple operating systems, it should not contain the window decoration of the operating system it was taken from. 


## Technical terms

Technical terms used in the documentation should always be documented / described in the glossary.
