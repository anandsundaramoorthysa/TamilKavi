from glob import glob
from argparse import ArgumentParser
from pprint import pprint
import json
import sys
import os 

class KaviExtraction:
    def __init__(self):
        self.saved_authors_data = []
        self.kavisrc_path = os.path.join(os.path.dirname(__file__), 'kavisrc') 
        self.get_authors_data_from_json()

    def get_authors_data_from_json(self):
        for file_path in glob(os.path.join(self.kavisrc_path, '*.json')):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    author_data = json.load(file)
                    if "author" in author_data and "books" in author_data:
                         self.saved_authors_data.append(author_data)
                    else:
                         print(f"Warning: Skipping file {os.path.basename(file_path)} - Missing 'author' or 'books' key.")
            except FileNotFoundError:
                 print(f"Error: File not found {file_path}")
            except json.JSONDecodeError:
                 print(f"Error: Could not decode JSON from {file_path}")
            except Exception as e:
                 print(f"An unexpected error occurred while loading {file_path}: {e}")


    def find_authors_data(self, author_name):
        """Find author data by name."""
        if author_name == 'all':
            return self.saved_authors_data 
        else:
            found_authors = [
                author_data for author_data in self.saved_authors_data
                if author_data.get('author') == author_name
            ]
            return found_authors 

    def find_books_data(self, book_title, authors_data_list):
        """Find book data by title within a list of authors' data."""
        if not authors_data_list:
            return [] 

        found_books = []
        for author_data in authors_data_list:
            for book_data in author_data.get('books', []):
                if book_data.get('booktitle') == book_title:
                    found_books.append(book_data)
        return found_books 

    def find_kavithais_data(self, kavithai_title, books_data_list):
        """Find kavithai context data by title within a list of books' data."""
        if not books_data_list:
            return []

        found_kavithais = []
        for book_data in books_data_list:
            for context_data in book_data.get('context', []):
                if context_data.get('title') == kavithai_title:
                    found_kavithais.append(context_data)
        return found_kavithais 

if __name__ == "__main__":
    parser = ArgumentParser(description="Access and filter Tamil Kavithai data.", epilog="Example: python kavi.py -a anand -b 'இன்பமில்லா-இதயத்திலிருந்து' -t 'Mother-Love'")

    parser.add_argument("-a", '--author', dest="author", default=None, type=str, help="Filter by author name ('all' for all authors).")
    parser.add_argument("-b", '--book', dest="book", default=None, type=str, help="Filter by book title.")
    parser.add_argument("-t", '--title', dest="title", default=None, type=str, help="Filter by kavithai title.")
   
    args = parser.parse_args()

    liberary = KaviExtraction() 

    results = liberary.saved_authors_data

    if args.author is not None:
        results = liberary.find_authors_data(args.author)
        if not results:
            print(f"No data found for author: {args.author}")
            sys.exit(1) 

    if args.book is not None:
         all_books_from_filtered_authors = []
         for author_data in results:
             all_books_from_filtered_authors.extend(author_data.get('books', []))

         results = liberary.find_books_data(args.book, all_books_from_filtered_authors)
         if not results:
             if args.author is not None and results: 
                 print(f"Book '{args.book}' not found for the specified author(s).")
             else: 
                 print(f"No data found for book: {args.book}")
             sys.exit(1)


    if args.title is not None:
        results = liberary.find_kavithais_data(args.title, results)
        if not results:
            if args.book is not None and results: 
                print(f"Kavithai with title '{args.title}' not found in book '{args.book}'.")
            elif args.author is not None and results:
                 print(f"Kavithai with title '{args.title}' not found for the specified author(s).")
            else:
                 print(f"No data found for title: {args.title}")
            sys.exit(1)

    if args.author is not None and args.book is None and args.title is None:
        for author_data in results:
             print(f"Author: {author_data.get('author')}")
             print(f"Contact: {author_data.get('contact')}")
             print("Books:")
             for i, book_data in enumerate(author_data.get('books', [])):
                 print(f"  {i}: {book_data.get('booktitle')}")

    elif args.book is not None and args.title is None:
         for book_data in results:
             print(f"Book Title: {book_data.get('booktitle')}")
             print(f"Category: {book_data.get('category')}")
             print(f"Description: {book_data.get('description')}")
             print("Kavithai Titles:")
             for i, context_data in enumerate(book_data.get('context', [])):
                  print(f"  {i}: {context_data.get('title')}")

    elif args.title is not None:
         for kavithai_data in results:
              pprint(kavithai_data)

    else:
        parser.print_help()
        print("\nNo filters applied. Please specify -a, -b, or -t.")