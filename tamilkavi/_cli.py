import sys
from argparse import ArgumentParser
from pprint import pprint

from ._library_api import (
    get_author_by_name,
    get_book_by_title,
    get_kavithais_by_title,
    get_kavithais_by_category, 
    get_all_author_names,
    get_all_book_titles,
    get_all_titles,
    get_all_categories,
    get_all_kavithais, 
    get_kavithai_by_index
)
from ._models import Author, Book, Kavithai 

def main():
    parser = ArgumentParser(description="Access and filter Tamil Kavithai data.",
                            epilog="Examples:\n"
                                   "  tamilkavi -a anand\n"
                                   "  tamilkavi -b 'இன்பமில்லா-இதயத்திலிருந்து'\n"
                                   "  tamilkavi -t 'Mother-Love'\n"
                                   "  tamilkavi -a anand -b 'இன்பமில்லா-இதயத்திலிருந்து'\n"
                                   "  tamilkavi -a anand -b 'இன்பமில்லா-இதயத்திலிருந்து' -t 'Mother-Love'\n"
                                   "  tamilkavi --list authors\n"
                                   "  tamilkavi --list books\n"
                                   "  tamilkavi --list titles\n"
                                   "  tamilkavi --list categories\n"
                                   "  tamilkavi --show all\n"
                                   "  tamilkavi --show index 5\n" 
                                   )

    list_group = parser.add_mutually_exclusive_group()
    list_group.add_argument("--list", dest="list_what", choices=['authors', 'books', 'titles', 'categories'],
                            help="List all authors, books, titles, or categories.")

    show_group = parser.add_mutually_exclusive_group()
    show_group.add_argument("--show", dest="show_what", choices=['all', 'index'],
                            help="Show all kavithais or a specific kavithai by index.")
    parser.add_argument("--index", dest="show_index", type=int, help="Index of the kavithai to show (used with --show index).")


    parser.add_argument("-a", '--author', dest="author", default=None, type=str,
                        help="Filter by author name.")
    parser.add_argument("-b", '--book', dest="book", default=None, type=str,
                        help="Filter by book title.")
    parser.add_argument("-t", '--title', dest="title", default=None, type=str,
                        help="Filter by kavithai title.")
    parser.add_argument("-c", '--category', dest="category", default=None, type=str,
                        help="Filter by book category.")


    args = parser.parse_args()

    if args.list_what == 'authors':
        authors = get_all_author_names()
        print("Available Authors:")
        for name in authors:
            print(f"- {name}")
        sys.exit(0)
    elif args.list_what == 'books':
        books = get_all_book_titles()
        print("Available Book Titles:")
        for title in books:
            print(f"- {title}")
        sys.exit(0)
    elif args.list_what == 'titles':
        titles = get_all_titles()
        print("Available Kavithai Titles:")
        for title in titles:
            print(f"- {title}")
        sys.exit(0)
    elif args.list_what == 'categories':
        categories = get_all_categories()
        print("Available Book Categories:")
        for category in categories:
             print(f"- {category}")
        sys.exit(0)


    if args.show_what == 'all':
        kavithais = get_all_kavithais()
        print(f"Showing all {len(kavithais)} Kavithais:")
        for i, kavithai in enumerate(kavithais):
            print(f"\n--- Kavithai {i} ---")
            print(kavithai) 
        sys.exit(0)
    elif args.show_what == 'index':
        if args.show_index is None:
            print("Error: --show index requires --index argument.")
            parser.print_help()
            sys.exit(1)
        try:
            kavithai = get_kavithai_by_index(args.show_index)
            print(f"\n--- Kavithai {args.show_index} ---")
            print(kavithai)
            sys.exit(0)
        except IndexError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
             print(f"An unexpected error occurred: {e}")
             sys.exit(1)

    filtered_kavithais = get_all_kavithais() 

    if args.author is not None:
        author_obj = get_author_by_name(args.author)
        if author_obj is None:
            print(f"Error: Author '{args.author}' not found.")
            sys.exit(1)
        filtered_kavithais = [
            k for k in filtered_kavithais
            if any(k in book.kavithais for book in author_obj.books)
        ]
        if not filtered_kavithais and (args.book is None and args.title is None and args.category is None):
             print(f"Author: {author_obj.name}")
             print(f"Contact: {author_obj.contact}")
             print("Books:")
             if author_obj.books:
                 for book in author_obj.books:
                      print(f"- {book.booktitle} ({book.category})")
             else:
                 print("  No books found for this author.")
             sys.exit(0)


    if args.book is not None:
        filtered_kavithais = [
            k for k in filtered_kavithais
            if any(book.booktitle == args.book and k in book.kavithais for author in get_all_authors() for book in author.books)
           
        ]
        if not filtered_kavithais:
            if get_book_by_title(args.book):
                 print(f"No kavithais found matching the book title '{args.book}' within the specified filters.")
            else:
                 print(f"Error: Book '{args.book}' not found.")
            sys.exit(1)

    if args.category is not None:
         filtered_kavithais = [
            k for k in filtered_kavithais
            if any(book.category == args.category and k in book.kavithais for author in get_all_authors() for book in author.books)
         ]
         if not filtered_kavithais:
             print(f"No kavithais found matching the category '{args.category}' within the specified filters.")
             sys.exit(1)


    if args.title is not None:
        filtered_kavithais = [
            k for k in filtered_kavithais
            if k.title == args.title
        ]
        if not filtered_kavithais:
            print(f"No kavithais found matching the title '{args.title}' within the specified filters.")
            sys.exit(1)


    if filtered_kavithais:
        print(f"Found {len(filtered_kavithais)} matching Kavithai(s):")
        for kavithai in filtered_kavithais:
            print("\n---")
            print(f"Title: {kavithai.title}")
            print(f"Line: {kavithai.line}")
            print(f"Meaning: {kavithai.meaning}")
            book = next((b for author in get_all_authors() for b in author.books if kavithai in b.kavithais), None)
            if book:
                print(f"(From Book: {book.booktitle}, Category: {book.category})")

    elif not (args.list_what or args.show_what):
         parser.print_help()
         print("\nNo filters or commands specified.")
         sys.exit(1)
    else:
         pass 


if __name__ == "__main__":
    main()