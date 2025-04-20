class Kavithai:
    """Represents a single Kavithai line and its meaning."""
    def __init__(self, title: str, line: str, meaning: str):
        self.title = title
        self.line = line
        self.meaning = meaning

    def __str__(self):
        return f"Title: {self.title}\nLine: {self.line}\nMeaning: {self.meaning}"

    def __repr__(self):
        return f"Kavithai(title='{self.title}', line='{self.line[:30]}...', meaning='{self.meaning[:30]}...')"

class Book:
    """Represents a book containing Kavithai."""
    def __init__(self, booktitle: str, coverimage: str, description: str, category: str, context: list):
        self.booktitle = booktitle
        self.coverimage = coverimage
        self.description = description
        self.category = category
        self.kavithais = [Kavithai(**k) for k in context]

    def __str__(self):
        return f"Book: {self.booktitle} ({self.category})\nDescription: {self.description}\nKavithais: {len(self.kavithais)}"

    def __repr__(self):
        return f"Book(booktitle='{self.booktitle}', category='{self.category}', num_kavithais={len(self.kavithais)})"

    def __len__(self):
        return len(self.kavithais)

    def __getitem__(self, index):
        """Allows accessing kavithais by index within the book."""
        return self.kavithais[index]

    def get_kavithais_by_title(self, title: str):
        """Returns a list of kavithais in this book with a matching title."""
        return [k for k in self.kavithais if k.title == title]

class Author:
    """Represents an author and their books."""
    def __init__(self, author: str, contact: str, books_data: list):
        self.name = author 
        self.contact = contact
        self.books = [Book(**b) for b in books_data]

    def __str__(self):
        return f"Author: {self.name}\nContact: {self.contact}\nBooks: {len(self.books)}"

    def __repr__(self):
        return f"Author(name='{self.name}', num_books={len(self.books)})"

    def get_book_by_title(self, booktitle: str):
        """Returns the first book by this author with the given title, or None."""
        for book in self.books:
            if book.booktitle == booktitle:
                return book
        return None

    def get_kavithais_by_category(self, category: str):
        """Returns a list of all kavithais by this author across all books with the given category."""
        all_matching_kavithais = []
        for book in self.books:
            if book.category == category:
                all_matching_kavithais.extend(book.kavithais)
        return all_matching_kavithais

    def get_kavithais_by_title(self, title: str):
        """Returns a list of all kavithais by this author across all books with the given title."""
        all_matching_kavithais = []
        for book in self.books:
             all_matching_kavithais.extend(book.get_kavithais_by_title(title))
        return all_matching_kavithais

class KavithaiCollection:
    """Holds data from all authors and provides methods for searching."""
    def __init__(self, authors: list[Author]):
        self.authors = authors
        self._all_kavithais = []
        for author in self.authors:
            for book in author.books:
                 self._all_kavithais.extend(book.kavithais)

    def __len__(self):
        return len(self._all_kavithais)

    def __getitem__(self, index):
        """Allows accessing any kavithai by a global index."""
        return self._all_kavithais[index]

    def get_author_by_name(self, name: str):
        """Returns the first Author with the given name, or None."""
        for author in self.authors:
            if author.name == name:
                return author
        return None

    def get_all_kavithais(self) -> list[Kavithai]:
        """Returns a flat list of all kavithais from all authors/books."""
        return self._all_kavithais

    def get_kavithais_by_title(self, title: str) -> list[Kavithai]:
        """Returns a list of all kavithais across all authors/books with the given title."""
        all_matching_kavithais = []
        for author in self.authors:
            all_matching_kavithais.extend(author.get_kavithais_by_title(title))
        return all_matching_kavithais

    def get_kavithais_by_category(self, category: str) -> list[Kavithai]:
         """Returns a list of all kavithais across all authors/books from books with the given category."""
         all_matching_kavithais = []
         for author in self.authors:
             all_matching_kavithais.extend(author.get_kavithais_by_category(category))
         return all_matching_kavithais

    def get_all_titles(self) -> list[str]:
        """Returns a list of all unique kavithai titles across all authors/books."""
        titles = set()
        for kavithai in self._all_kavithais:
            titles.add(kavithai.title)
        return list(titles)

    def get_all_categories(self) -> list[str]:
        """Returns a list of all unique book categories across all authors/books."""
        categories = set()
        for author in self.authors:
             for book in author.books:
                 categories.add(book.category)
        return list(categories)

    def get_all_author_names(self) -> list[str]:
        """Returns a list of all author names."""
        return [author.name for author in self.authors]

    def get_all_book_titles(self) -> list[str]:
         """Returns a list of all book titles across all authors."""
         titles = set()
         for author in self.authors:
              for book in author.books:
                   titles.add(book.booktitle)
         return list(titles)