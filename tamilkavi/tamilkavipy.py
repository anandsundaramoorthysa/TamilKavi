import json
import sys
from glob import glob
from argparse import ArgumentParser
from pprint import pprint
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
        if name == 'all':
            return data
        found_authors = []
        for author in data:
            if author.get('author') == name:
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
            if isinstance(data[0], dict) and 'books' in data[0]:
                for author in data:
                    for book in author.get('books', []):
                        for context in book.get('context', []):
                            if context.get('title') == title:
                                found_poems.append(context)
            # Assuming list of books if the first item has 'context' key
            elif isinstance(data[0], dict) and 'context' in data[0]:
                 for book in data:
                    for context in book.get('context', []):
                        if context.get('title') == title:
                            found_poems.append(context)
            # Assuming list of poem contexts if the first item has 'line' and 'meaning' keys
            elif isinstance(data[0], dict) and 'line' in data[0] and 'meaning' in data[0]:
                 for context in data:
                    if context.get('title') == title:
                        found_poems.append(context)

        return found_poems # Return a list of poem context dicts, empty if not found


    def get_books_from_json(self):
        """Loads book data from JSON files in kavisrc/ directory."""
        json_files = glob('kavisrc/*.json')
        if not json_files:
            print("⚠️  No JSON files found in 'kavisrc/' directory.")
            # Decide whether to exit or proceed with no data. Exiting is safer.
            sys.exit("Exiting: Cannot find any data files.")


        for file_path in json_files:
            try:
                with open(file_path, "r+", encoding="utf-8") as file:
                    self.saved_books.append(json.load(file))
            except json.JSONDecodeError as e:
                print(f"⚠️  Error decoding JSON from {file_path}: {e}")
                # Continue loading other files
            except FileNotFoundError:
                print(f"⚠️  Error: File not found at {file_path}")
                # This case is unlikely given glob found the file, but good practice.
                pass
            except Exception as e:
                print(f"⚠️  An unexpected error occurred while reading {file_path}: {e}")
                # Continue loading other files
        
        if not self.saved_books:
             print("⚠️  No valid data loaded from JSON files.")
             sys.exit("Exiting: No data loaded.")


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
def display_kavithais_in_table(kavithais): # Removed category parameter
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
parser = ArgumentParser(description="Tamil Kavi CLI", epilog="வணக்கம் ~ Kavithaigal CLI Tool")
parser.add_argument("-a", '--authors', dest="author_name", default=None, type=str, help="Filter by author name")
parser.add_argument("-t", '--title', dest="poem_title", default=None, type=str, help="Filter by poem title")
parser.add_argument("-b", '--book', dest="book_title", default=None, type=str, help="Filter by book title")
parser.add_argument("-s", '--show', dest="show", default=None, type=str, help="(Optional) future feature - currently ignored") # Updated help text
args = parser.parse_args()

library = KaviExtraction()
current_data = library.saved_books # Start with all loaded data

# Store which filter was applied last to guide display logic
last_filter = None

# Apply filters sequentially
if args.author_name is not None:
    current_data = library.get_authors(args.author_name, current_data)
    if not current_data:
        print(f"⚠️ Sorry, author '{args.author_name}' not found in the package.")
        print(f"⚠️  Manuchu '{args.author_name}' endra ezhuthalar intha package-la kidayadhu.")
        sys.exit()
    last_filter = 'author'

if args.book_title is not None:
    # get_book expects a list of author dicts, which is the current_data structure if -a was used,
    # or the initial list of all authors if -a was not used.
    current_data = library.get_book(args.book_title, current_data)
    if not current_data:
         # Assuming get_book returns empty list if not found
        print(f"⚠️ Sorry, book '{args.book_title}' not found.")
        print(f"⚠️  Manuchu '{args.book_title}' endra puthagham kidayadhu.")
        sys.exit()
    last_filter = 'book'


if args.poem_title is not None:
    # get_titles can handle lists of author dicts or book dicts
    current_data = library.get_titles(args.poem_title, current_data)
    if not current_data:
        # Assuming get_titles returns empty list if not found
        print(f"⚠️ Sorry, poem title '{args.poem_title}' not found.")
        print(f"⚠️  Manuchu '{args.poem_title}' endra kavithai thalaippu kidayadhu.")
        sys.exit()
    last_filter = 'poem'


# Now, determine what to display based on the `last_filter` and the resulting `current_data`

if not current_data:
    # This case should ideally not be reached if "not found" messages are printed after filters
    print("⚠️  No results found based on the provided filters.")

elif last_filter == 'poem':
    # Try to find the author name if an author filter was applied previously
    author_name_to_display = 'Unknown Author'
    if args.author_name:
        author_lookup = library.get_authors(args.author_name, library.saved_books)
        if author_lookup:
            author_name_to_display = author_lookup[0].get('author', 'Unknown Author')
        print(f"✅ Author / Ezhuthalar: {author_name_to_display}") # Added print for author

    if args.poem_title:
         print(f"✅ Filtered by Title: {args.poem_title}")

    # When displaying poems filtered only by title, category information might be varied
    # or not easily accessible for each poem. Display just poems with title.
    display_kavithais_in_table(current_data)
    
# Displaying books (specific book filter applied resulted in book list)
elif last_filter == 'book':
     if current_data: # Should contain at least one book if we reached here
        book_data = current_data[0] # Assuming one relevant book after filtering

        # Try to find the author name if an author filter was applied previously
        author_name_to_display = 'Unknown Author'
        # Re-filtering original data by author name if present is a straightforward way.
        if args.author_name:
            author_lookup = library.get_authors(args.author_name, library.saved_books)
            if author_lookup:
                author_name_to_display = author_lookup[0].get('author', 'Unknown Author')

        # Display Author, Book Titles, and Category before the poem table as requested
        if args.author_name: # Only display author if author filter was used
             print(f"✅ Author / Ezhuthalar: {author_name_to_display}")

        print(f"✅ Book Title (Tanglish): {book_data.get('booktitle_tanglish', 'N/A')}")
        print(f"✅ Book Title (Tamil): {book_data.get('booktitle', 'N/A')}")
        print(f"📚 Category: {book_data.get('category', 'N/A')}") # Display Category here

        print("📜 Poems / Kavithaigal:")
        # Call the display function, which now includes the Title column
        display_kavithais_in_table(book_data.get('context', []))

     else:
         print("⚠️  No book data to display.") # Should be caught by filter check


# Displaying authors and their books (least specific filter applied or no filter)
elif last_filter == 'author': # Specific author requested
    if current_data: # Should contain at least one author if we reached here
        author_data = current_data[0] # Assuming one author after filter
        print(f"✅ Author / Ezhuthalar: {author_data.get('author', 'Unknown')}")
        print(f"📧 Contact: {author_data.get('contact', 'N/A')}") # Include contact for author view
        all_books = author_data.get("books", [])
        if all_books:
            print("📚 Books / Puthagangal:")
            display_books_in_table(all_books)
        else:
            print("⚠️  No books found for this author.")
    else:
         print("⚠️  No author data to display.") # Should be caught by filter check

# No filters applied - list all authors as a default view
else:
    print("Available Authors:")
    if current_data: # current_data is the list of all authors here
        for author_data in current_data:
             print(f"- {author_data.get('author', 'Unknown')}")
        print("\nUse -a <author_name> to see books by an author.")
    else:
        print("No authors available.") # Should be caught by initial loading checks