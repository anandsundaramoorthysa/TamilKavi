import json
import sys
from glob import glob
# Import RawTextHelpFormatter to preserve formatting in epilog
from argparse import ArgumentParser, RawTextHelpFormatter
from prettytable import PrettyTable
import textwrap

# Function to wrap text to fit the table
def wrap_text(text, width=50):
    """Wraps text to a specified width for display."""
    if not isinstance(text, str):
        return text # Handle non-string input gracefully
    return '\n'.join(textwrap.wrap(text, width))

# KaviExtraction class to load and retrieve data
class KaviExtraction:
    def __init__(self):
        self.saved_books = []
        self.get_books_from_json()

    def get_authors(self, name, data):
        """Filters data by author name. Data is expected to be a list of author dicts."""
        if name == 'all': # This 'all' case is now used internally or if explicitly passed
            return data
        found_authors = []
        for author in data:
            # Check if the 'author' key exists before comparing
            if author.get('author') is not None and author.get('author') == name:
                found_authors.append(author)
        return found_authors # Return list, empty if not found

    def get_book(self, book_title, data):
        """Filters data by book title. Data is expected to be a list of author dicts."""
        found_books = []
        for author in data:
            for book in author.get('books', []):
                # Match against both Tamil and Tanglish titles
                if book.get('booktitle_tanglish') == book_title or book.get('booktitle') == book_title:
                     found_books.append(book)
        return found_books # Return a list of book dicts, empty if not found

    def get_titles(self, title, data):
        """Filters data by poem title. Data can be a list of author dicts or book dicts."""
        found_poems = []
        # Check if data is a list of authors or a list of books or a list of contexts
        if data:
            # Assuming list of authors if the first item has 'books' key
            # Added checks for data[0] being a dict before accessing keys
            if isinstance(data[0], dict) and 'books' in data[0]:
                for author in data:
                    for book in author.get('books', []):
                        for context in book.get('context', []):
                             # Check if the 'title' key exists before comparing
                            if context.get('title') is not None and context.get('title') == title:
                                found_poems.append(context)
            # Assuming list of books if the first item has 'context' key
            elif isinstance(data[0], dict) and 'context' in data[0]:
                 for book in data:
                    for context in book.get('context', []):
                         # Check if the 'title' key exists before comparing
                        if context.get('title') is not None and context.get('title') == title:
                            found_poems.append(context)
            # Assuming list of poem contexts if the first item has 'line' and 'meaning' keys
            elif isinstance(data[0], dict) and 'line' in data[0] and 'meaning' in data[0]:
                 for context in data:
                     # Check if the 'title' key exists before comparing
                    if context.get('title') is not None and context.get('title') == title:
                        found_poems.append(context)

        return found_poems # Return a list of poem context dicts, empty if not found

    def get_all_books(self, data):
        """Extracts all books from a list of author dicts."""
        all_books_list = []
        if data: # Ensure data is not empty
            # Assuming data is a list of author dicts if the first element has a 'books' key
            if isinstance(data[0], dict) and 'books' in data[0]:
                for author in data:
                    all_books_list.extend(author.get('books', []))
            # If data is already a list of books, return it as is (though filtering should handle this)
            # elif isinstance(data[0], dict) and 'context' in data[0]:
            #     return data # Or copy? Returning original might be risky if modified later.
            # Let's assume this is called on author data or the initial saved_books.
        return all_books_list

    def get_all_unique_titles(self, data):
        """Collects all unique poem titles from a list of author dicts or book dicts."""
        unique_titles = set()
        if data:
            # Check if data is a list of authors or a list of books or a list of contexts
            if isinstance(data[0], dict) and 'books' in data[0]: # List of authors
                for author in data:
                    for book in author.get('books', []):
                        for context in book.get('context', []):
                            title = context.get('title')
                            if title: # Add title if it exists and is not empty
                                unique_titles.add(title)
            elif isinstance(data[0], dict) and 'context' in data[0]: # List of books
                 for book in data:
                    for context in book.get('context', []):
                        title = context.get('title')
                        if title:
                           unique_titles.add(title)
            # If data is already a list of contexts, extract titles from there
            elif isinstance(data[0], dict) and 'line' in data[0] and 'meaning' in data[0]:
                 for context in data:
                    title = context.get('title')
                    if title:
                       unique_titles.add(title)

        return sorted(list(unique_titles)) # Return as a sorted list

    def get_books_from_json(self):
        """Loads book data from JSON files in kavisrc/ directory."""
        json_files = glob('kavisrc/*.json')
        if not json_files:
            print("⚠️  No JSON files found in 'kavisrc/' directory.")
            sys.exit("Exiting: Cannot find any data files.")

        loaded_count = 0
        for file_path in json_files:
            try:
                with open(file_path, "r+", encoding="utf-8") as file:
                    data = json.load(file)
                    # Basic check if the loaded data has expected structure (author key)
                    if isinstance(data, dict) and 'author' in data:
                         self.saved_books.append(data)
                         loaded_count += 1
                    else:
                         print(f"⚠️  Skipping {file_path}: Does not contain top-level 'author' key or is not a dictionary.")

            except json.JSONDecodeError as e:
                print(f"⚠️  Error decoding JSON from {file_path}: {e}")
                # Continue loading other files
            except FileNotFoundError:
                 # This case is unlikely given glob found the file, but good practice.
                print(f"⚠️  Error: File not found at {file_path}")
                pass
            except Exception as e:
                print(f"⚠️  An unexpected error occurred while reading {file_path}: {e}")
                # Continue loading other files
        
        if not self.saved_books:
             print("⚠️  No valid author data loaded from JSON files.")
             sys.exit("Exiting: No data loaded.")
        # Optional: print success message
        # print(f"✅ Successfully loaded data for {loaded_count} author(s) from {len(json_files)} file(s).")


# Function to display books in table format
def display_books_in_table(books):
    """Displays a list of book dictionaries in a table."""
    table = PrettyTable()
    table.field_names = ["SNO", "Book Title (Tanglish)", "Book Title (Tamil)"]

    if not books:
        print("No books to display.")
        return

    for index, book in enumerate(books, start=1):
        book_title_tanglish = book.get('booktitle_tanglish', 'N/A')
        book_title_tamil = book.get('booktitle', 'N/A')

        table.add_row([index, wrap_text(book_title_tanglish, 40), wrap_text(book_title_tamil, 40)]) # Wrap book titles

    print(table)


# Function to display Kavithais in table format
def display_kavithais_in_table(kavithais):
    """Displays a list of poem context dictionaries in a table."""
    table = PrettyTable()
    # Updated field names to include Kavithai Title
    table.field_names = ["SNO", "Kavithai Title", "Kavithai", "Kavithai Meaning"]

    if not kavithais:
        print("No poems to display.")
        return

    for index, kavithai in enumerate(kavithais, start=1):
        row = [index]
        
        # Get the poem title
        kavithai_title = kavithai.get('title', 'N/A')
        kavithai_text = kavithai.get('line', 'N/A')
        kavithai_meaning = kavithai.get('meaning', 'N/A')

        # Wrap the texts
        kavithai_title_wrapped = wrap_text(kavithai_title, width=30) # Wrap title with a suitable width
        kavithai_text_wrapped = wrap_text(kavithai_text, width=60)
        kavithai_meaning_wrapped = wrap_text(kavithai_meaning, width=60)

        # Add data to the row in the correct order
        row.extend([kavithai_title_wrapped, kavithai_text_wrapped, kavithai_meaning_wrapped])
        table.add_row(row)

    print(table)


# CLI Argument parsing
epilog_text = """
Examples:

# List all authors
python tamilkavipy.py -a

# List all books from all authors
python tamilkavipy.py -b

# List all unique poem titles from all books
python tamilkavipy.py -t

# Show books by a specific author
python tamilkavipy.py -a <author_name>

# Show poems from a specific book (by any author, if -a not used)
python tamilkavipy.py -b <book_title>

# Show poems with a specific title (from any book/author, if -a/-b not used)
python tamilkavipy.py -t <poem_title>

# Show poems from a specific book by a specific author
python tamilkavipy.py -a <author_name> -b <book_title>

# Show poems with a specific title by a specific author
python tamilkavipy.py -a <author_name> -t <poem_title>

# Show poems with a specific title from a specific book
python tamilkavipy.py -b <book_title> -t <poem_title>

# Show poems with a specific title from a specific book by a specific author
python tamilkavipy.py -a <author_name> -b <book_title> -t <poem_title>

# Get detailed help
python tamilkavipy.py -h

"""

parser = ArgumentParser(
    description="Tamil Kavi CLI - Command Line tool for exploring Tamil Kavithaigal.", # Slightly improved description
    epilog=epilog_text,
    formatter_class=RawTextHelpFormatter # Use RawTextHelpFormatter to preserve formatting in epilog
)
# Modified -a argument: nargs='?' allows 0 or 1 argument.
# const='__list_all__' is the value assigned to args.author_name if -a is used without an argument.
parser.add_argument("-a", '--authors', dest="author_name", nargs='?', const='__list_all__', type=str, help="Filter by author name (use -a to list all authors)")
# Modified -b argument: nargs='?' allows 0 or 1 argument.
# const='__list_all_books__' is the value assigned to args.book_title if -b is used without an argument.
parser.add_argument("-b", '--book', dest="book_title", nargs='?', const='__list_all_books__', type=str, help="Filter by book title (use -b to list all books)")
# Modified -t argument: nargs='?' allows 0 or 1 argument.
# const='__list_all_titles__' is the value assigned to args.poem_title if -t is used without an argument.
parser.add_argument("-t", '--title', dest="poem_title", nargs='?', const='__list_all_titles__', type=str, help="Filter by poem title (use -t to list all unique titles)")
args = parser.parse_args()

library = KaviExtraction()
current_data = library.saved_books # Start with all loaded data

# Store which filter was applied last to guide display logic
last_filter = None

# Apply filters sequentially

# Handle the special case for -a used without an argument first
if args.author_name == '__list_all__':
    # If -a was used alone, we intend to list all authors.
    # We set last_filter to 'author_list' to trigger the author listing display block later.
    # current_data is already all loaded authors, so no filtering needed here.
    last_filter = 'author_list' # Use a distinct value for listing all authors

elif args.author_name is not None: # This means -a was used with a specific author name
    current_data = library.get_authors(args.author_name, current_data)
    if not current_data:
        print(f"⚠️ Sorry, author '{args.author_name}' not found in the package.")
        print(f"⚠️  Manuchu '{args.author_name}' endra ezhuthalar intha package-la kidayadhu.")
        sys.exit()
    last_filter = 'author' # Specific author found

# Apply book filter if specified
if args.book_title is not None:
    if args.book_title == '__list_all_books__':
        # Case: -b was used without an argument - list all books across all authors
        # current_data is currently the result of any previous author filter (or all authors)
        current_data = library.get_all_books(current_data) # Get all books from the current data
        last_filter = 'book_list' # Use a distinct last_filter value for listing all books
        # No 'not found' error here, as we're listing what's available
    else:
        # Case: -b was used with a specific book name - filter by book
        # current_data is the result of any previous author filter (or all authors)
        current_data = library.get_book(args.book_title, current_data)
        if not current_data:
             print(f"⚠️ Sorry, book '{args.book_title}' not found.")
             print(f"⚠️  Manuchu '{args.book_title}' endra puthagham kidayadhu.")
             sys.exit()
        last_filter = 'book' # Specific book found


# Apply poem title filter if specified
if args.poem_title is not None:
    if args.poem_title == '__list_all_titles__':
        # Case: -t was used without an argument - list all unique titles
        # current_data is currently the result of any previous author/book filter (or all authors)
        all_titles = library.get_all_unique_titles(current_data) # Get all unique titles from the current data
        current_data = all_titles # Store the list of titles in current_data
        last_filter = 'title_list' # Use a distinct last_filter value for listing all titles
        # No 'not found' error here, as we're listing what's available
    else:
        # Case: -t was used with a specific poem title - filter by title
        # current_data is the result of any previous author/book filter (or all authors/books)
        current_data = library.get_titles(args.poem_title, current_data)
        if not current_data:
            print(f"⚠️ Sorry, poem title '{args.poem_title}' not found.")
            print(f"⚠️  Manuchu '{args.poem_title}' endra kavithai thalaippu kidayadhu.")
            sys.exit()
        last_filter = 'poem' # Specific poem title found


# Now, determine what to display based on the `last_filter`, `args` and the resulting `current_data`
# Order the display logic from most specific filter result to least specific / default.

# Displaying poems (last filter was specific poem title)
if last_filter == 'poem':
    # Try to find the author name if an author filter was applied previously (and was a specific name)
    if args.author_name is not None and args.author_name != '__list_all__':
         author_lookup = library.get_authors(args.author_name, library.saved_books)
         if author_lookup:
             author_name_to_display = author_lookup[0].get('author', 'Unknown Author')
             print(f"✅ Author / Ezhuthalar: {author_name_to_display}")

    if args.poem_title and args.poem_title != '__list_all_titles__': # Print title only if specific title was requested
         print(f"✅ Filtered by Title: {args.poem_title}")

    display_kavithais_in_table(current_data)

# Displaying books (last filter was a specific book title)
elif last_filter == 'book':
     if current_data: # Should contain at least one book if we reached here
        book_data = current_data[0] # Assuming one relevant book after filtering by specific title

        # Try to find the author name if an author filter was applied previously (and was a specific name)
        if args.author_name is not None and args.author_name != '__list_all__':
             author_lookup = library.get_authors(args.author_name, library.saved_books)
             if author_lookup:
                 author_name_to_display = author_lookup[0].get('author', 'Unknown Author')
                 print(f"✅ Author / Ezhuthalar: {author_name_to_display}") # Only display author if specific author filter was used

        print(f"✅ Book Title (Tanglish): {book_data.get('booktitle_tanglish', 'N/A')}")
        print(f"✅ Book Title (Tamil): {book_data.get('booktitle', 'N/A')}")
        print(f"📚 Category: {book_data.get('category', 'N/A')}") # Display Category here

        print("📜 Poems / Kavithaigal:")
        display_kavithais_in_table(book_data.get('context', []))

     else:
         print("⚠️  No book data to display.") # Should be caught by filter check

# Displaying list of all unique titles (last filter was -t without argument)
elif last_filter == 'title_list':
    print("📑  Available Poem Titles / Irrukum Kavithai Thalaipugal:")
    if current_data: # current_data is the list of unique titles here
        for i, title in enumerate(current_data, start=1):
            print(f"{i}. {title}")
    else:
        print("No poem titles available.")


# Displaying list of all books (last filter was -b without argument)
elif last_filter == 'book_list':
    print("📚  Available Books / Irrukum Puthagangal:")
    # current_data is already the list of book dicts here
    display_books_in_table(current_data)


# Displaying specific author and their books (last filter was author name)
elif last_filter == 'author': # Specific author requested and found
    if current_data: # Should be a list of one author
        author_data = current_data[0]
        print(f"✅ Author / Ezhuthalar: {author_data.get('author', 'Unknown')}")
        print(f"📧 Contact: {author_data.get('contact', 'N/A')}")
        all_books = author_data.get("books", [])
        if all_books:
            print("📚 Books / Puthagangal:")
            display_books_in_table(all_books)
        else:
            print("⚠️  No books found for this author.")
    else:
        print("⚠️  Author data not found for display.") # Should be caught earlier, but safety check


# Displaying list of all authors (fallback if none of the above matched)
# This happens if:
# - args.author_name is '__list_all__' and no book/title filter was applied subsequently.
# - No args are provided.
elif args.author_name == '__list_all__' or (args.author_name is None and args.book_title is None and args.poem_title is None):
     print("✍️  Available Authors / Irrukum Ezhuthalargal:")
     # current_data is the list of all authors in these cases
     if current_data:
         for author_data in current_data:
              print(f"- {author_data.get('author', 'Unknown')}")
         print("\nUse -a <author_name> to see books by an author.")
         print("Use -a to list all authors.") # Clarify the -a usage
     else:
         print("No authors available.") # Caught by initial loading checks


# Final fallback for any truly unhandled state where current_data is unexpectedly empty
# (cases where filtering failed but weren't caught by specific filter checks)
# or states not covered by the specific display conditions.
elif not current_data:
    # This check is placed later to allow intentional empty results (like listing all authors/books/titles when none exist)
    # to be handled by their specific blocks. If we reach here and current_data is empty, it's an unhandled no-result case.
     print("⚠️  No results found based on the provided filters.")
     # Debug print if needed
     # print("Debug: No results. last_filter:", last_filter, "args:", args)


else:
    # Fallback for any state not covered by the specific display conditions.
    print("⚠️  Unable to determine display format based on filters.")
    # Debug print if needed
    # print("Debug: Unhandled state. last_filter:", last_filter, "args:", args, "current_data type:", type(current_data), "current_data sample:", current_data[:1] if current_data else "[]")