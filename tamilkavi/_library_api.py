from ._data_loader import kavithai_collection
from ._models import Kavithai, Book, Author, KavithaiCollection

if kavithai_collection is None:
    _data_loaded = False
    _collection = None 
else:
    _data_loaded = True
    _collection = kavithai_collection

def _check_data_loaded():
    if not _data_loaded:
        raise RuntimeError("TamilKavi data not loaded. Check for errors during package import.")

def get_kavithai_by_index(index: int) -> Kavithai:
    """Get a Kavithai by its global index."""
    _check_data_loaded()
    try:
        return _collection[index]
    except IndexError:
        raise IndexError(f"Kavithai index {index} is out of range. Total kavithais: {len(_collection)}")


def get_kavithais_by_title(title: str) -> list[Kavithai]:
    """Get Kavithai(s) by title across all authors/books."""
    _check_data_loaded()
    return _collection.get_kavithais_by_title(title)


def get_kavithais_by_category(category: str) -> list[Kavithai]:
    """Get Kavithai(s) from books with the given category across all authors."""
    _check_data_loaded()
    return _collection.get_kavithais_by_category(category)


def get_author_by_name(name: str) -> Author | None:
    """Get an Author object by their name."""
    _check_data_loaded()
    return _collection.get_author_by_name(name)

def get_book_by_title(booktitle: str) -> Book | None:
     """Get the first Book object found with the given title across all authors."""
     _check_data_loaded()
     for author in _collection.authors:
         book = author.get_book_by_title(booktitle)
         if book:
             return book 
     return None

def get_all_authors() -> list[Author]:
    """Get a list of all Author objects."""
    _check_data_loaded()
    return _collection.authors

def get_all_kavithais() -> list[Kavithai]:
     """Get a flat list of all Kavithai objects."""
     _check_data_loaded()
     return _collection.get_all_kavithais()

def get_all_titles() -> list[str]:
     """Get a list of all unique Kavithai titles."""
     _check_data_loaded()
     return _collection.get_all_titles()

def get_all_categories() -> list[str]:
     """Get a list of all unique book categories."""
     _check_data_loaded()
     return _collection.get_all_categories()

def get_all_author_names() -> list[str]:
    """Get a list of all author names."""
    _check_data_loaded()
    return _collection.get_all_author_names()

def get_all_book_titles() -> list[str]:
    """Get a list of all book titles."""
    _check_data_loaded()
    return _collection.get_all_book_titles()
