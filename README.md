![PyPI version](https://img.shields.io/pypi/v/tamilkavi)
![License](https://img.shields.io/github/license/anandsundaramoorthysa/tamilkavi)
![Python Version](https://img.shields.io/static/v1?label=Python&message=3.7%2B&color=blue)
[![Build Status](https://github.com/anandsundaramoorthysa/tamilkavi/actions/workflows/ci.yml/badge.svg)](https://github.com/anandsundaramoorthysa/tamilkavi/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/anandsundaramoorthysa/tamilkavi/branch/main/graph/badge.svg)](https://codecov.io/gh/anandsundaramoorthysa/tamilkavi)
![PyPI Downloads](https://img.shields.io/pypi/dm/tamilkavi)
# tamilkavi

A command-line interface for exploring Tamil Kavithaigal (Tamil Poetry).

## Table of Contents

- [About Project](#about-project)
- [Installation & Run the Project](#installation--run-the-project)
- [Reading Tamil in a terminal](#reading-tamil-in-a-terminal)
- [Features](#features)
- [Contribution](#contribution)
- [License](#license)
- [Contact Me](#contact-me)
- [Acknowledge](#acknowledge)

## About Project

Tamil Kavi is a simple and intuitive command-line tool designed to provide easy access to a curated collection of Tamil poetry. It empowers users to navigate through poems by listing authors, books, and titles, and by applying filters to find specific content. The poetry data is included as JSON files within the package, making the tool self-contained after installation.

This project serves as a command-line companion and is proudly associated with the website [tamilkavi.anandsundaramoorthy.com](https://tamilkavi.anandsundaramoorthy.com), which offers additional details about it.

## Installation & Run the Project

You can install `tamilkavi` directly from the Python Package Index (PyPI) using pip, the standard Python package installer:

```bash
pip install tamilkavi
````

This installs `tamilkavi` and everything it needs. On Python 3.9+ the package has
**no third-party dependencies at all** -- only the standard library -- so there is
nothing that can fail to build. On Python 3.7 and 3.8, pip additionally installs the
small `importlib_resources` backport automatically.

It works on **Windows, macOS and Linux**.

Once the installation is complete, you can run the `tamilkavi` command from any terminal window.

Here is the usage information and examples:

```text
Tamil Kavi CLI - Command Line tool for exploring Tamil Kavithaigal.

options:
  -h, --help            show this help message and exit
  --version             Show the installed tamilkavi version and exit
  -r, --read            Open the result in your browser, where Tamil renders correctly
                        (no terminal can shape Tamil script properly)
  -e, --english         Print the poem in Tanglish (romanised Tamil) instead of
                        Tamil script. Readable in every terminal, on every OS
  -a [AUTHOR_NAME], --authors [AUTHOR_NAME]
                        Filter by author name (use -a to list all authors)
  -b [BOOK_TITLE], --book [BOOK_TITLE]
                        Filter by book title (use -b to list all books)
  -t [POEM_TITLE], --title [POEM_TITLE]
                        Filter by poem title (use -t to list all unique titles)

Examples:

# List all authors
tamilkavi -a

# List all books from all authors
tamilkavi -b

# List all unique poem titles from all books
tamilkavi -t

# Show books by a specific author
tamilkavi -a "Author Name"

# Show poems from a specific book (by any author, if -a not used)
tamilkavi -b "Book Title"

# Show poems with a specific title (from any book/author, if -a/-b not used)
tamilkavi -t "Poem Title"

# Show poems from a specific book by a specific author
tamilkavi -a "Author Name" -b "Book Title"

# Show poems with a specific title by a specific author
tamilkavi -a "Author Name" -t "Poem Title"

# Show poems with a specific title from a specific book
tamilkavi -b "Book Title" -t "Poem Title"

# Show poems with a specific title from a specific book by a specific author
tamilkavi -a "Author Name" -b "Book Title" -t "Poem Title"

# Get detailed help
tamilkavi -h

# Show the installed version
tamilkavi --version

# Read a poem properly, in your browser
tamilkavi -t "Poem Title" --read

# Show a poem in Tanglish, readable in any terminal
tamilkavi -t "Poem Title" -e
```

## Reading Tamil in a terminal

A terminal draws one cell per Unicode code point, but a Tamil letter is usually
several code points that have to be composed into a single shape. No terminal on
any operating system does this correctly -- not Windows Terminal, not macOS
Terminal or iTerm2, not GNOME Terminal. Tamil will always come out with its vowel
signs detached and its clusters overlapping.

That is not something this package can fix, so it gives you two ways around it:

| Command | What you get | Works on |
| --- | --- | --- |
| `tamilkavi -t "..."` | Tamil script | every OS, but the shaping will look broken |
| `tamilkavi -t "..." -e` | Tanglish (romanised) | every terminal, every OS, perfectly |
| `tamilkavi -t "..." --read` | Real Tamil, in your browser | every OS, perfectly |

`--read` opens the poem in your default browser, which shapes Tamil properly. It
prints nothing else to the terminal. If nothing matched your filter it says so and
opens no browser, rather than showing you an empty page.

`-e` and `--read` combine: ask for romanised output and you get it in the browser
too, not just the terminal.

The romanisation in `-e` follows Tamil's own sound rules rather than swapping
letters one by one, so `நதி` becomes *nadhi* but `அதிபதி` becomes *adhibadhi*, and
`பொங்கல்` becomes *pongal*.

## Features

  * **Comprehensive Listing:** Easily list all authors, books, and unique poem titles in the collection.
  * **Flexible Filtering:** Filter the poetry collection by author name, book title (supporting both Tamil and Tanglish titles), or poem title.
  * **Combined Search:** Apply multiple filters simultaneously (e.g., find poems with a specific title within a particular book by a certain author).
  * **Readable Output:** Poems print as blocks that keep the line breaks the poet wrote, instead of being squeezed into table cells.
  * **Tanglish Mode:** `-e` romanises the poem so it is readable in any terminal on any operating system.
  * **Browser Reading:** `--read` opens the poem in your browser, the only place Tamil script renders correctly.
  * **Self-Contained Data:** Includes poetry data within the package for offline access after installation.
  * **Command-Line Interface:** Provides a simple and powerful way to interact with the poetry collection directly from the terminal.

## Contribution

### How to Contribute

We welcome contributions from everyone who wants to help preserve and promote Tamil literature. There are two main ways to contribute poems to our collection:

### Contributing New Features

We are always looking for ways to improve our platform and welcome contributions of new features. If you have an idea for a new feature or improvement, we'd love to hear about it\!

**Guidelines for Feature Contributions:**

  * **Discuss your idea:** Before you start coding, please open an [issue](https://www.google.com/search?q=https://github.com/anandsundaramoorthysa/tamilkavi/issues) on our GitHub repository to discuss your proposed feature. This helps ensure it aligns with the project's goals and avoids duplicate work.
  * **Understand the codebase:** Take some time to familiarize yourself with the existing codebase, its structure, and coding conventions.
  * **Follow coding standards:** Please adhere to the coding style and best practices used throughout the project, including the [PEP-8 format](https://www.python.org/dev/peps/pep-0008/) for Python code. This includes proper formatting, naming conventions, and commenting.
  * **Write tests:** Ensure your feature contribution includes appropriate unit and integration tests to verify its functionality and prevent regressions.
  * **Submit a pull request:** Once you've developed your feature and written tests, submit a pull request with a clear title and description of your changes. Reference the issue you discussed earlier in the PR description.

Our team will review your pull request and provide feedback. We appreciate your effort in helping us improve this project\!

[View Open Issues](https://www.google.com/search?q=https://github.com/anandsundaramoorthysa/tamilkavi/issues)

### Contributing via GitHub

If you're familiar with GitHub, this is our preferred method as it maintains proper versioning and attribution of contributions. You will be directly adding data to the project's source files.

**Step-by-Step Process:**

1.  **Fork the repository:** Start by forking our [GitHub repository](https://github.com/anandsundaramoorthysa/tamilkavi) to your own account.
2.  **Navigate to the data directory:** In your forked repository, navigate to the `tamilkavi/kavisrc/` directory.
3.  **Find or create the author's file:** Look for a JSON file named after the author (e.g., `jothi.json`). If the author doesn't exist, create a new JSON file using their name in lowercase.
4.  **Add/Update the JSON data:** Add or update the poem data within the author's JSON file, following the specified structure for `author`, `contact`, and the `books` array. Ensure the structure for each `book` and `context` entry is correct.
5.  **Commit your changes:** Commit the changes to your forked repository with a clear and concise commit message.
6.  **Submit a pull request (PR):** Create a pull request from your forked repository's branch to the main `TamilKavi` repository's `main` branch. Provide a clear title and description of the poems you've added or updated.

**Sample JSON Structure**

```json
{
  "author": "jothi",
  "contact": "sanand03072005@gamil.com",
  "books":[
      {
          "booktitle": "இன்பமில்லா-இதயத்திலிருந்து",
          "booktitle_tanglish": "inbamilla-ithayathilirundhu",
          "description": "சாதிக்க தூதிக்கும் ஒரு சாதாரண மாணவன்",
          "category": "Feelings",
          "context":[
              {
                  "title": "God-Murugan-Song",
                  "line": "பிறப்பிலும் முருகனை, இறப்பிலும் இறைவனை, அனைத்திலும் அவனை கொண்டு இனிதே தொடங்குவோம்!.",
                  "meaning": "எனது பிறப்பிலும் முருகனை, எனது இறப்பிலும் அவனை, எனது வாழ்வின் ஒவ்வொரு கட்டத்திலும் அவனை நினைத்து இனிதே தொடங்குவோம்!."
              }
              // Add more poem contexts here
          ]
      }
      // Add more books here
  ]
}
```

⚠️ **Important:** Please ensure the JSON structure is valid and follows the format precisely. Invalid JSON will cause errors.

[Visit our GitHub Repository](https://github.com/anandsundaramoorthysa/tamilkavi)

### Contributing via Submission Form

Not comfortable with GitHub? No problem\! You can use our submission form to contribute poems.

**What You'll Need:**

  * ✍️ Author Original Name
  * 📘 Author Book Name
  * 📧 Contact Email
  * 📑 Book Title (Tamil)
  * 📑 Book Title (Tanglish)
  * 📝 Book Description
  * 🏷️ Poem Category
  * 📂 Upload your poetry document (under 100 MB, plain text or .docx preferred)

**Sample Document Format**

```text
Title: God-Murugan-Song
Kavithai: பிறப்பிலும் முருகனை, இறப்பிலும் இறைவனை, அனைத்திலும் அவனை கொண்டு இனிதே தொடங்குவோம்!.
Meaning: எனது பிறப்பிலும் முருகனை, எனது இறப்பிலும் அவனை, எனது வாழ்வின் ஒவ்வொரு கட்டத்திலும் அவனை நினைத்து இனிதே தொடங்குவோம்!.

Title: Mother-Love
Kavithai: தாலாட்டில் வளர்ந்தவன், தனிமையில் வளரும் கொடுமைகளை, வார்த்தையில் சொல்ல இயலாது.
Meaning: தாயின் மடியில் நன்காக, அன்பாக வளர்க்கப்பட்ட ஒரு குழந்தை, பிறகு தனிமையில் வளர நேரிடும் போது எதிர்கொள்ளும் வேதனைகள் மற்றும் துன்பங்களை வார்த்தைகளால் விவரிக்க முடியாது. அந்த அனுபவம் மிகுந்த மன வேதனையைக் கொடுக்கும்.
```

⚠️ **Important:** Please **do not submit kavithaigal written by other authors** unless you have explicit permission. We will not accept or include plagiarized content.

📦 Once we review and approve your submission, it will be added to our **Python Package**, listed on the **Website – Preview Poems Page**, and published in our **Hugging Face Dataset**.

Our team will review submissions and add them to the repository, with full attribution to the contributor.

[![Go to Submission Form Badge](https://img.shields.io/badge/-Go%20to%20Submission%20Form-blue?style=for-the-badge)](https://forms.gle/Qdi9U1btYQSTjDoG6)

## License

This project is released under the MIT License. You are free to use, modify, and distribute the code under the terms of this license. See the [LICENSE](LICENSE) file in the repository for the full text.

## Contact Us

If you have any questions, feedback, or suggestions, feel free to reach out to the authors:

* **ANAND SUNDARAMOORTHY SA**: [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Question%20about%20Tamil%20Kavi%20CLI%20Tool&body=Dear%20Authors%2C%0A%0AI%20have%20a%20question%20regarding%20the%20Tamil%20Kavi%20python%20package%2E%0A%0A%5BYour%20Question%20Here%5D%0A%0AThank%20you%21%0A%5BYour%20Name%5D)
* **Boopalan S**: [content.boopalan@gmail.com](mailto:content.boopalan@gmail.com?subject=Question%20about%20Tamil%20Kavi%20CLI%20Tool&body=Dear%20Authors%2C%0A%0AI%20have%20a%20question%20regarding%20the%20Tamil%20Kavi%20python%20package%2E%0A%0A%5BYour%20Question%20Here%5D%0A%0AThank%20you%21%0A%5BYour%20Name%5D)

## Acknowledge

We want to express our gratitude to:

  * The open-source community, and the authors of `importlib.resources` and its `importlib_resources` backport -- the only libraries this package now relies on.
  * **Praveen Kumar Purushothaman** ([@praveenscience](https://github.com/praveenscience)) – *Early Hosting Supporter*
    🙏 Thanks to him for providing the subdomain **tamilkavi.jigg.win**, which the website ran on in its early days.
  * **[Selvakumar Duraipandian](https://www.linkedin.com/in/selvakumarduraipandian/)** – *Sponsor (Domain Supporter)*
    🙏 Thanks to him for sponsoring the **tamilkavi.com** domain for a year, which the website ran on
    before moving to [tamilkavi.anandsundaramoorthy.com](https://tamilkavi.anandsundaramoorthy.com).
  * The association with the [TamilKavi Python Package](https://github.com/anandsundaramoorthysa/tamilkavi).
