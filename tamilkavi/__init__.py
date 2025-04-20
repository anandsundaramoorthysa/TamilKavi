# tamilkavi/__init__.py

# Import core library functions and models
from ._library_api import (
    get_kavithai_by_index,
    get_kavithais_by_title,
    get_kavithais_by_category,
    get_author_by_name,
    get_book_by_title,
    get_all_authors,
    get_all_kavithais,
    get_all_titles,
    get_all_categories,
    get_all_author_names,
    get_all_book_titles
)

# Import models if users want to work with the objects directly
from ._models import Kavithai, Book, Author, KavithaiCollection

# Import the command-line interface entry point (optional, depends on packaging)
# from ._cli import main as cli_main # If you make a dedicated CLI entry point

# Define what is imported with 'from tamilkavi import *'
__all__ = [
    'get_kavithai_by_index',
    'get_kavithais_by_title',
    'get_kavithais_by_category',
    'get_author_by_name',
    'get_book_by_title',
    'get_all_authors',
    'get_all_kavithais',
    'get_all_titles',
    'get_all_categories',
    'get_all_author_names',
    'get_all_book_titles',
    'Kavithai',
    'Book',
    'Author',
    'KavithaiCollection',
    # 'cli_main', # Include if you want the CLI exposed here
]

# Add package metadata
__version__ = "0.1.0"
__author__ = "ANAND SUNDARAMOORTHY SA"
__contact__ = "sanand03072005@gamil.com" 

from ._data_loader import kavithai_collection
if kavithai_collection:
    total_kavithais = len(kavithai_collection)
    total_authors = len(kavithai_collection.authors)
else:
    total_kavithais = 0
    total_authors = 0