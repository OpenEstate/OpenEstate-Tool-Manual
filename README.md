Users manual for OpenEstate-ImmoTool
====================================

This repository contains the development files for the *OpenEstate-ImmoTool* users manual in English and German language. These files are used in order to generate the manual in different target formats.

-   A **HTML5 website** is generated with [*Hugo*](https://gohugo.io/).
-   A **PDF** / **EPUB** / **ODT** / **DOCX** / **XHTML (single page)** file is generated with [*Pandoc*](https://pandoc.org/).


Documentation
-------------


### How to generate the HTML5 website

In order to generate the HTML5 website you need to download [*Hugo*](https://gohugo.io/) beforehand:

-   *Linux* users may execute the script [`apps/init-hugo.sh`](apps/init-hugo.sh) in order to download *Hugo* automatically. Alternatively you can [download](https://github.com/gohugoio/hugo/releases) *Hugo* manually and place its binary into the `apps/linux/bin` folder.
-   *Windows* users need to [download](https://github.com/gohugoio/hugo/releases) `hugo.exe` manually and place it into the `apps/windows/bin` folder.

Afterwards you can use the following scripts in order to generate the HTML5 website:

-   The `build.sh` / `build.bat` script generates the website into the `public` folder.
-   The `server.sh` / `server.bat` script starts *Hugo* in [server mode](https://gohugo.io/commands/hugo_server/) and allows live preview of modified files in the web browser via
    -   <http://localhost:1313/en/> for the English website
    -   <http://localhost:1314/de/> for the German website


### How to generate other formats

In order to generate other formats you need to install [*Pandoc*](https://pandoc.org/) on your system. Currently this repository only provides a solution for *Linux* systems. Other operating systems might also work with some modifications, but we're currently not planning to support other systems.

Follow the [instructions provided by *Pandoc*](https://pandoc.org/installing.html#linux) for installation. For PDF output [*TeX Live*](http://www.tug.org/texlive/) is also required.

You also need to install [*Python*](https://www.python.org/) and the [*virtualenv*](https://virtualenv.pypa.io/) package on your system. Most *Linux* distributions provide packages for both dependencies. Afterwards you can create a virtual environment for *Python* by executing the `app/init-virtualenv.sh` script.

On *Debian GNU/Linux* you can install the dependencies via:

```
apt install \
  virtualenv \
  pandoc \
  texlive-latex-base \
  texlive-lang-german \
  texlive-lang-english \
  texlive-fonts-recommended \
  texlive-fonts-extra \
  texlive-latex-recommended \
  texlive-latex-extra
```

After all dependencies are installed you can use the following scripts on your *Linux* system in order to generate the manual in other target formats:

-   The `book-english.sh` script generates the manual into the `book/en` folder.
-   The `book-german.sh` script generates the manual into the `book/de` folder.


### How to modify the users manual

The [`content`](content) folder contains development files of the manual in [Markdown format](https://en.wikipedia.org/wiki/Markdown) and provided images.

-   The [`content/en`](content/en) folder contains all development files of the English manual.
-   The [`content/de`](content/de) folder contains all development files of the German manual. 

Open the Markdown files (ending with `.md`) in your preferred text editor and make your changes. Afterwards you can rebuild the manual with the provided scripts (as documented above).


### Notes about the Markdown format, standards & conventions

In order to provide a consistent users manual we've established some standards and conventions. Please read the following documents before you modify the contents and provide a pull request:

-   The [`NOTES.en.md`](NOTES.en.md) file contains information & conventions about the English users manual.
-   The [`NOTES.de.md`](NOTES.de.md) file contains information & conventions about the German users manual.
-   The [`CONTRIBUTING.md`](CONTRIBUTING.md) file contains information about how to provide you modifications to us.


Dependencies
------------

The generated HTML5 website bundles the following dependencies:

-   [*Bootstrap*](https://getbootstrap.com/) v4.3.1 ([MIT](https://github.com/twbs/bootstrap/blob/master/LICENSE))
-   [*jQuery*](https://jquery.com/) v3.3.1 ([MIT](https://jquery.org/license/))
-   [*SmartMenus*](https://www.smartmenus.org/) v1.1.0 ([MIT](https://github.com/vadikom/smartmenus/blob/master/LICENSE-MIT))
-   [*Lunr*](https://lunrjs.com/) v2.3.5 ([MIT](https://github.com/olivernn/lunr.js/blob/master/LICENSE))
-   [*js-url*](https://github.com/websanova/js-url) v2.5.3 ([MIT](https://github.com/websanova/js-url/blob/master/README.md#license))
-   [*jQuery ScrollSpy Plugin*](https://github.com/softwarespot/jquery-scrollspy) rev `801a603` ([MIT](https://github.com/softwarespot/jquery-scrollspy#jquery-scrollspy))
-   [*ScrollToFixed*](http://bigspotteddog.github.io/ScrollToFixed/) v1.0.8 ([MIT](https://github.com/bigspotteddog/ScrollToFixed/blob/master/license.txt))
-   [*Font Awesome Free*](https://fontawesome.com/) v5.7.2 ([Font Awesome Free License](https://github.com/FortAwesome/Font-Awesome/blob/master/LICENSE.txt))

The users manual in ePub format bundles the following dependencies:

-   [*DejaVu Fonts*](https://dejavu-fonts.github.io/) v2.37 ([Public Domain, Bitstream Vera Fonts Copyright & Arev Fonts Copyright](https://dejavu-fonts.github.io/License.html))

The users manual in PDF format is created with:

-   [*Eisvogel* template](https://github.com/Wandmalfarbe/pandoc-latex-template) v1.1 ([BSD](https://github.com/Wandmalfarbe/pandoc-latex-template/blob/master/LICENSE))
-   [*pandoc-latex-tip*](https://github.com/chdemko/pandoc-latex-tip) ([BSD](https://github.com/chdemko/pandoc-latex-tip/blob/master/LICENSE))
-   [*pandoc-latex-admonition*](https://github.com/chdemko/pandoc-latex-admonition) ([BSD](https://github.com/chdemko/pandoc-latex-admonition/blob/master/LICENSE))


License
-------

The development files of the user manual (including images) and the generated user manual is licensed under the terms of the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/deed). Take a look at [`LICENSE.txt`](LICENSE.txt) for the license text.

The provided development scripts (*Bash*, *Batch* & *Python* files) and *JavaScript* files of the generated website are licensed under the terms of [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.html). Take a look at [`LICENSE.scripts.txt`](LICENSE.scripts.txt) for the license text.


Further information
-------------------

-   [*OpenEstate-Tool-Manual* at GitHub](https://github.com/OpenEstate/OpenEstate-Tool-Manual)
-   [Releases of *OpenEstate-Tool-Manual*](https://github.com/OpenEstate/OpenEstate-Tool-Manual/releases)
-   [*OpenEstate-Tool-Manual* website in English](https://manual.openestate.org/en/)
-   [*OpenEstate-Tool-Manual* website in German](https://manual.openestate.org/de/)
-   [Download *OpenEstate-Tool-Manual* in other formats](https://manual.openestate.org/download/)
