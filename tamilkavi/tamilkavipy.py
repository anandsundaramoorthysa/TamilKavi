import io
import json
import os
import sys
import unicodedata
from pathlib import Path
from argparse import ArgumentParser, RawTextHelpFormatter

# importlib.resources.files() only exists from Python 3.9. On 3.7 and 3.8 the
# same API comes from the importlib_resources backport, which setup.py installs
# for those versions -- so use whichever one this interpreter has.
try:
    from importlib.resources import files as resource_files
except ImportError:  # Python 3.7 / 3.8
    from importlib_resources import files as resource_files

try:
    from tamilkavi import __version__
except ImportError:  # running the module directly from a source checkout
    __version__ = "unknown"

try:
    from tamilkavi.transliterate import romanise
except ImportError:
    from transliterate import romanise

# Tamil script is what the CLI prints by default. -e romanises it instead,
# because no terminal can shape Tamil, and --read opens it in a browser.
ROMANISE_OUTPUT = False


def in_selected_script(text):
    """Return text in whichever script was asked for: Tamil, or -e romanised."""
    if not ROMANISE_OUTPUT or not text:
        return text
    return romanise(text)


# Tamil vowel signs, the pulli, and the au length mark. These attach to the
# preceding letter instead of standing on their own.
_TAMIL_COMBINING = set(range(0x0BBE, 0x0BCE)) | {0x0B82, 0x0BD7}


def enable_utf8_output():
    """Make Tamil survive the trip to the terminal.

    Windows consoles start on a legacy code page (437 by default) which cannot
    encode Tamil at all, so the text is lost before anything is drawn. Switching
    the console to UTF-8 and reconfiguring the streams is what makes it appear.
    """
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        except Exception:
            pass
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def tamil_letters(text):
    """Split text into letters as a reader sees them, not Unicode code points.

    'பிறப்பிலும்' is 11 code points but 6 letters. Counting code points is what
    makes Tamil overflow every column it is put in.
    """
    letters = []
    for ch in str(text):
        if letters and (ord(ch) in _TAMIL_COMBINING or unicodedata.combining(ch)):
            letters[-1] += ch
        else:
            letters.append(ch)
    return letters


def letter_len(text):
    """Length of text measured in letters rather than code points."""
    return len(tamil_letters(text))


def wrap_lines(text, width=66):
    """Word-wrap on spaces, measuring width in letters. Never splits a letter."""
    words = str(text).split()
    if not words:
        return [""]
    lines, current = [], words[0]
    for word in words[1:]:
        if letter_len(current) + 1 + letter_len(word) > width:
            lines.append(current)
            current = word
        else:
            current += " " + word
    lines.append(current)
    return lines


def wrap_text(text, width=50):
    """Wraps text to a specified width for display, counting Tamil letters."""
    if not isinstance(text, str):
        return text
    return '\n'.join(wrap_lines(text, width))

class KaviExtraction:
    def __init__(self):
        self.saved_books = []
        self.get_books_from_json()

    def get_authors(self, name, data):
        """Filters a list of author dicts by author name."""
        found_authors = []
        for author in data:
            if author.get('author') is not None and author.get('author').lower() == name.lower():
                found_authors.append(author)
        return found_authors

    def get_book(self, book_title, data):
        """Filters a list of author/book dicts by book title."""
        found_books = []
        if not data:
             return []

        # Check if data is a list of author dicts or a list of book dicts
        if data and isinstance(data[0], dict):
            if 'books' in data[0]:
                 for author in data:
                     for book in author.get('books', []):
                         if (book.get('booktitle_tanglish', '').lower() == book_title.lower() or
                                 book.get('booktitle', '').lower() == book_title.lower()):
                             found_books.append(book)
            elif 'context' in data[0]: # Assuming data is already a list of book-like dictionaries
                 for book in data:
                     if (book.get('booktitle_tanglish', '').lower() == book_title.lower() or
                             book.get('booktitle', '').lower() == book_title.lower()):
                         found_books.append(book)
            # Added a check for 'line' and 'meaning' which might indicate list of contexts,
            # though get_book expects books or authors. This block was in get_titles,
            # moving it here was likely a copy/paste error, but keeping the structure
            # as provided by the user. Let's remove this part as it doesn't belong in get_book.
            # elif 'line' in data[0] and 'meaning' in data[0]:
            #      # This case seems incorrect for get_book. Reverting to previous logic.
            #      pass
        else:
             # If data is not empty but data[0] is not a dict or doesn't have expected keys
             if data: # Only print warning if data was provided but was unexpected format
                print("Warning: get_book received unexpected data format.")


        return found_books

    def get_titles(self, title, data):
        """Filters data (list of authors, books, or contexts) by poem title."""
        found_poems = []
        if not data:
             return []

        def search_books_for_title(books_list):
            poems = []
            for book in books_list:
                for context in book.get('context', []):
                    if context.get('title', '').lower() == title.lower():
                        poems.append(context)
            return poems

        # Check if data is a list of author dicts, book dicts, or context dicts
        if data and isinstance(data[0], dict):
            if 'books' in data[0]: # Data is a list of author dicts
                 for author in data:
                     found_poems.extend(search_books_for_title(author.get('books', [])))
            elif 'context' in data[0]: # Data is a list of book dicts (or book-like dicts with context)
                 found_poems = search_books_for_title(data)
            elif 'line' in data[0] and 'meaning' in data[0]: # Data is a list of context dicts
                 for context in data:
                     if context.get('title', '').lower() == title.lower():
                          found_poems.append(context)
        else:
             # If data is not empty but data[0] is not a dict or doesn't have expected keys
             if data: # Only print warning if data was provided but was unexpected format
                 print("Warning: get_titles received unexpected data format.")


        return found_poems

    def get_all_books(self, data):
        """Extracts all books from a list of author dicts."""
        all_books_list = []
        if data and isinstance(data, list) and data and isinstance(data[0], dict) and 'books' in data[0]:
             for author in data:
                 all_books_list.extend(author.get('books', []))

        return all_books_list

    def get_all_unique_titles(self, data):
        """Collects all unique poem titles from a list of author dicts or book dicts."""
        unique_titles = set()
        if data and isinstance(data, list) and data and isinstance(data[0], dict):
            def collect_titles_from_books(books_list):
                titles = set()
                for book in books_list:
                    for context in book.get('context', []):
                        title = context.get('title')
                        if title:
                             titles.add(title)
                return titles

            if 'books' in data[0]: # Data is a list of author dicts
                 for author in data:
                     unique_titles.update(collect_titles_from_books(author.get('books', [])))
            elif 'context' in data[0]: # Data is a list of book dicts (or book-like dicts with context)
                 unique_titles.update(collect_titles_from_books(data))
            elif 'line' in data[0] and 'meaning' in data[0]: # Data is a list of context dicts
                 for context in data:
                     title = context.get('title')
                     if title:
                         unique_titles.add(title)

        return sorted(list(unique_titles))

    def get_books_from_json(self):
        """Loads book data from JSON files included in the package data."""
        self.saved_books = [] # Clear the list before loading

        # Use importlib.resources to access files within the installed package
        # 'tamilkavi' is the name of your package as defined in setup.py
        # 'kavisrc' is the subdirectory within your package containing data
        try:
            # A Traversable for the 'kavisrc' directory inside the installed
            # package. Works the same on every OS -- no filesystem paths built
            # by hand, so it also survives being run from a zipped install.
            data_dir = resource_files('tamilkavi') / 'kavisrc'
        except FileNotFoundError:
            print("⚠️  Package data directory 'kavisrc' not found.")
            sys.exit("Exiting: Cannot find data files within the package. Ensure kavisrc folder is included in package_data.")
        except Exception as e:
            print(f"⚠️  An unexpected error occurred while accessing package data directory: {e}")
            sys.exit("Exiting: Error accessing package data.")

        json_files = list(data_dir.glob('*.json'))

        if not json_files:
            if data_dir.is_dir():
                print(f"⚠️  No JSON files found in '{data_dir}'. Is the folder empty?")
            else:
                print(f"⚠️  Package data directory '{data_dir}' could not be accessed or found.")
            sys.exit("Exiting: Cannot find any data files.")


        loaded_count = 0
        for file_path in json_files:
            try:
                with file_path.open("r", encoding="utf-8") as file:
                    data = json.load(file)
                    if isinstance(data, dict) and 'author' in data:
                         self.saved_books.append(data)
                         loaded_count += 1
                    else:
                         print(f"⚠️  Skipping {file_path.name}: Does not contain top-level 'author' key or is not a dictionary.")

            except json.JSONDecodeError as e:
                 print(f"⚠️  Error decoding JSON from {file_path.name}: {e}")
            except Exception as e:
                 print(f"⚠️  An unexpected error occurred while reading {file_path.name}: {e}")

        if not self.saved_books:
            print("⚠️  No valid author data loaded from JSON files.")
            sys.exit("Exiting: No data loaded.")


POEM_WIDTH = 66

# Whatever the last command displayed, kept so --read can hand it to a browser.
_shown = {"poems": [], "books": []}


_PAGE = """<!doctype html>
<meta charset="utf-8">
<title>%(title)s</title>
<style>
  :root { color-scheme: light dark; }
  body { margin: 0; padding: 3rem 1.5rem; background: #faf8f5; color: #1a1a1a;
         font-family: "Nirmala UI", "Latha", "Noto Sans Tamil", sans-serif; }
  main { max-width: 46rem; margin: 0 auto; }
  h1 { font-size: 1rem; letter-spacing: .12em; text-transform: uppercase;
       color: #8a7f70; font-weight: 600; margin: 0 0 2.5rem; }
  article { margin: 0 0 3.5rem; }
  h2 { font-size: .8rem; letter-spacing: .1em; text-transform: uppercase;
       color: #8a7f70; font-weight: 600; margin: 0 0 1rem; }
  .kavithai { font-size: 1.5rem; line-height: 2.1; white-space: pre-wrap;
              margin: 0 0 1.75rem; }
  .porul { border-left: 2px solid #ddd4c8; padding-left: 1.25rem;
           font-size: 1.05rem; line-height: 1.9; color: #55504a; }
  .porul b { display: block; font-size: .75rem; letter-spacing: .1em;
             text-transform: uppercase; color: #8a7f70; margin-bottom: .5rem; }
  dl { margin: 0 0 2rem; font-size: 1.1rem; line-height: 1.8; }
  dt { font-size: .75rem; letter-spacing: .1em; text-transform: uppercase;
       color: #8a7f70; }
  dd { margin: 0 0 .75rem; }
  @media (prefers-color-scheme: dark) {
    body { background: #16150f; color: #ece7de; }
    h1, h2, dt, .porul b { color: #9b9184; }
    .porul { border-left-color: #3a352c; color: #b8b0a4; }
  }
</style>
<main>
<h1>%(title)s</h1>
%(body)s
</main>
"""


def _esc(text):
    return (str(text or "").replace("&", "&amp;")
                           .replace("<", "&lt;").replace(">", "&gt;"))


def render_page(poems, books, title="TamilKavi"):
    """Build a standalone HTML page for whatever was just displayed."""
    parts = []
    for book in books:
        parts.append(
            "<article><h2>%s</h2><dl>"
            "<dt>Booktitle</dt><dd>%s</dd>"
            "<dt>Category</dt><dd>%s</dd>"
            "<dt>Description</dt><dd>%s</dd></dl></article>" % (
                _esc(book.get('booktitle_tanglish')),
                _esc(in_selected_script(book.get('booktitle'))),
                _esc(in_selected_script(book.get('category'))),
                _esc(in_selected_script(book.get('description')))))

    for poem in poems:
        # -e applies here too. The browser is where Tamil script renders properly,
        # but if romanised output was asked for, the flag should still be honoured
        # rather than silently ignored.
        meaning = in_selected_script(poem.get('meaning'))
        label = "Porul" if ROMANISE_OUTPUT else "பொருள்"
        porul = ("<div class='porul'><b>%s</b>%s</div>" % (label, _esc(meaning))) if meaning else ""
        parts.append("<article><h2>%s</h2><div class='kavithai'>%s</div>%s</article>" % (
            _esc(poem.get('title')), _esc(in_selected_script(poem.get('line'))), porul))

    if not parts:
        parts.append("<p>Nothing to show.</p>")
    return _PAGE % {"title": _esc(title), "body": "\n".join(parts)}


def open_in_browser(poems, books, title="TamilKavi"):
    """Write the page to a temp file and open it in the default browser.

    A terminal draws one cell per code point, but a Tamil letter is several code
    points that have to be composed into one shape. No terminal does that, so a
    kavithai always comes out broken. A browser shapes text properly, which is
    the only way to actually read the poem on this machine.
    """
    import tempfile
    import webbrowser

    path = os.path.join(tempfile.gettempdir(), "tamilkavi.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(render_page(poems, books, title))
    webbrowser.open(Path(path).as_uri())
    print("🌐 Opened in your browser: %s" % path)


def display_books(books, indent="  "):
    """List books as labelled blocks rather than a table.

    A column has to be padded to a fixed width, and no terminal agrees with us
    about how wide Tamil is: the console draws one cell per code point, while a
    Tamil letter is usually several. Any table therefore tears its own borders
    apart. Putting the label first and the value after it removes the problem,
    because nothing has to fit a column any more.
    """
    _shown["books"].extend(books)

    if not books:
        print("No books to display.")
        return

    for index, book in enumerate(books, start=1):
        print("%s[%d] Book Title (Tanglish): %s" % (
            indent, index, book.get('booktitle_tanglish') or 'N/A'))
        print("%s    Book Title (Tamil):    %s" % (
            indent, in_selected_script(book.get('booktitle')) or 'N/A'))
        print("%s    Category:              %s" % (
            indent, in_selected_script(book.get('category')) or 'N/A'))

        description = book.get('description')
        if description:
            for position, piece in enumerate(wrap_lines(in_selected_script(description), POEM_WIDTH)):
                label = "Description:           " if position == 0 else " " * 23
                print("%s    %s%s" % (indent, label, piece))
        print("")


def display_kavithais(kavithais, indent="  "):
    """Print poems as blocks, preserving the line breaks the poet wrote.

    A table cannot hold a kavithai. PrettyTable re-wraps every cell, which
    flattens the line breaks that give a poem its shape, and its column maths
    counts code points, so Tamil never lines up inside the borders anyway.
    """
    _shown["poems"].extend(kavithais)

    if not kavithais:
        print("No poems to display.")
        return

    for index, kavithai in enumerate(kavithais, start=1):
        title = kavithai.get('title') or 'N/A'
        print("%s[%d] Kavithai Title: %s" % (indent, index, title))
        print("%s    %s" % (indent, "-" * POEM_WIDTH))

        for authored_line in str(in_selected_script(kavithai.get('line')) or 'N/A').split("\n"):
            if not authored_line.strip():
                print("")
                continue
            # Long lines still have to fold, but an authored break is never
            # invented or removed -- folded continuations are indented so you
            # can tell them apart from a real line of the poem.
            for position, piece in enumerate(wrap_lines(authored_line, POEM_WIDTH)):
                print("%s    %s%s" % (indent, "  " if position else "", piece))

        meaning = kavithai.get('meaning')
        if meaning and meaning != 'N/A':
            print("")
            print("%s    Kavithai Meaning:" % indent)
            for piece in wrap_lines(in_selected_script(meaning), POEM_WIDTH):
                print("%s    %s" % (indent, piece))
        print("")

def main():
    enable_utf8_output()

    epilog_text = """
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

    """

    parser = ArgumentParser(
        prog='tamilkavi',
        description="Tamil Kavi CLI - Command Line tool for exploring Tamil Kavithaigal.",
        epilog=epilog_text,
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__,
                        help="Show the installed tamilkavi version and exit")
    parser.add_argument('-r', '--read', action='store_true',
                        help="Open the result in your browser, where Tamil renders correctly\n"
                             "(no terminal can shape Tamil script properly)")
    parser.add_argument('-e', '--english', action='store_true',
                        help="Print the poem in Tanglish (romanised Tamil) instead of\n"
                             "Tamil script. Readable in every terminal, on every OS")
    parser.add_argument("-a", '--authors', dest="author_name", nargs='?', const='__list_all__', type=str, help="Filter by author name (use -a to list all authors)")
    parser.add_argument("-b", '--book', dest="book_title", nargs='?', const='__list_all_books__', type=str, help="Filter by book title (use -b to list all books)")
    parser.add_argument("-t", '--title', dest="poem_title", nargs='?', const='__list_all_titles__', type=str, help="Filter by poem title (use -t to list all unique titles)")
    args = parser.parse_args()

    global ROMANISE_OUTPUT
    ROMANISE_OUTPUT = args.english
    _shown["poems"].clear()
    _shown["books"].clear()

    # Check if *any* of the filter arguments (-a, -b, -t) were provided with *any* value (including the const values)
    is_any_filter_requested = (
        args.author_name is not None or
        args.book_title is not None or
        args.poem_title is not None
    )

    # If none of the filter arguments were requested, this is the default command
    is_default_command = not is_any_filter_requested

    if is_default_command:
        print("🙏 Vannakam Makkalayae !")
        print("Welcome to Tamil Kavi 👋")
        print("A command-line tool for exploring Tamil Kavithaigal.")
        print("\nTo explore the commands. Check,")
        print("👉 tamilkavi -h")
        print("\nAlso Check our website about this project:")
        print("👉 https://tamilkavi.anandsundaramoorthy.com")

        # Terminals draw one cell per code point, but a Tamil letter is often
        # several code points, so no console shapes Tamil perfectly. The classic
        # Windows console is the worst of them -- say so instead of letting the
        # reader think the poems themselves are broken.
        if sys.platform == "win32" and not os.environ.get("WT_SESSION"):
            print("\nNote: the classic Windows console cannot shape Tamil script properly.")
            print("For the best reading experience use Windows Terminal, or the website.")

        sys.exit(0)

    # --read is a browser-only mode: the terminal copy would be the broken one,
    # so the normal output is captured and thrown away rather than shown.
    real_stdout = sys.stdout
    captured = io.StringIO()
    if args.read:
        sys.stdout = captured

    library = KaviExtraction()
    current_data = library.saved_books


    # If author filter is specified (and not just listing all)
    if args.author_name is not None and args.author_name != '__list_all__':
        current_data = library.get_authors(args.author_name, current_data)

    # If book filter is specified (and not just listing all)
    if args.book_title is not None and args.book_title != '__list_all_books__':
        current_data = library.get_book(args.book_title, current_data)

    # If poem title filter is specified (and not just listing all)
    if args.poem_title is not None and args.poem_title != '__list_all_titles__':
         current_data = library.get_titles(args.poem_title, current_data)


    displayed = False

    if args.author_name == '__list_all__':
        print("✍️ Available Authors / Irrukum Ezhuthalargal:") 
        all_authors = library.saved_books
        if all_authors:
             for author_data in all_authors:
                  print(f"- {author_data.get('author', 'Unknown')}")
             print("\nUse -a \"Author Name\" to see books by a specific author.")
        else:
             print("No authors available.")
        displayed = True

    elif args.book_title == '__list_all_books__':
        print("📚 Available Books / Irrukum Puthagangal:")
        all_books = library.get_all_books(library.saved_books)
        display_books(all_books)
        displayed = True

    elif args.poem_title == '__list_all_titles__':
        print("📑 Available Poem Titles / Irrukum Kavithaiyin Thalaipugal:")
        all_titles = library.get_all_unique_titles(library.saved_books)
        if all_titles:
            for i, title in enumerate(all_titles, start=1):
                print(f"{i}. {title}")
        else:
            print("No poem titles available.")
        displayed = True

    is_specific_filter_applied_with_results = (
        is_any_filter_requested and
        not (args.author_name == '__list_all__' or args.book_title == '__list_all_books__' or args.poem_title == '__list_all_titles__') and # It wasn't just a list-all command
        current_data
    )

    if is_specific_filter_applied_with_results:
        if args.poem_title is not None and args.poem_title != '__list_all_titles__':
             print(f"✅ Filtered by Title: {args.poem_title}")
             if args.author_name is not None and args.author_name != '__list_all__':
                 author_lookup = library.get_authors(args.author_name, library.saved_books)
                 if author_lookup:
                      print(f"✅ Author / Ezhuthalar: {author_lookup[0].get('author', 'Unknown Author')}")
             if args.book_title is not None and args.book_title != '__list_all_books__':
                  book_lookup = library.get_book(args.book_title, library.saved_books)
                  if book_lookup:
                       print(f"✅ Book Title (Tanglish): {book_lookup[0].get('booktitle_tanglish', 'N/A')}")

             display_kavithais(current_data)
             displayed = True

        elif args.book_title is not None and args.book_title != '__list_all_books__':
             for book_data in current_data:
                  if args.author_name is not None and args.author_name != '__list_all__':
                      author_lookup = library.get_authors(args.author_name, library.saved_books)
                      if author_lookup:
                           print(f"✅ Author / Ezhuthalar: {author_lookup[0].get('author', 'Unknown Author')}")

                  print(f"✅ Book Title (Tanglish): {book_data.get('booktitle_tanglish', 'N/A')}")
                  print(f"✅ Book Title (Tamil): {book_data.get('booktitle', 'N/A')}")
                  print(f"📚 Category: {book_data.get('category', 'N/A')}")
                  print("📜 Poems / Kavithaigal:")
                  display_kavithais(book_data.get('context', []))
                  if len(current_data) > 1: print("-" * 30)
             displayed = True

        elif args.author_name is not None and args.author_name != '__list_all__':
             author_data = current_data[0]
             print(f"✅ Author / Ezhuthalar: {author_data.get('author', 'Unknown')}")
             print(f"📧 Contact: {author_data.get('contact', 'N/A')}")
             all_books = author_data.get("books", [])
             if all_books:
                 print("📚 Books / Puthagangal:")
                 display_books(all_books)
             else:
                  print("⚠️  No books found for this author.")
             displayed = True

    if is_any_filter_requested and not (args.author_name == '__list_all__' or args.book_title == '__list_all_books__' or args.poem_title == '__list_all_titles__') and not current_data:
         print("⚠️  No results found.") 
         displayed = True


    if not displayed:
         print("⚠️  Unhandled command or display scenario.")
         print("Use -h for help.")

    if args.read:
        sys.stdout = real_stdout
        if not (_shown["poems"] or _shown["books"]):
            # Nothing matched, so there is no page worth opening. Show the
            # message that was captured instead of a blank browser tab.
            sys.stdout.write(captured.getvalue())
            return 1
        heading = args.poem_title or args.book_title or args.author_name or "TamilKavi"
        if heading.startswith("__list_all"):
            heading = "TamilKavi"
        open_in_browser(_shown["poems"], _shown["books"], heading)


if __name__ == "__main__":
    main()
