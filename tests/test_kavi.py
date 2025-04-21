# tests/test_kavi.py

import pytest
import sys
import os

# This section is to help pytest find your 'tamilkavi' package
# when run from the project root (where setup.py is).
# In a real project, installing the package in "editable" mode
# (`pip install -e .`) before running tests is the standard practice.
# If you encounter ImportError, try uncommenting the lines below or
# installing in editable mode.
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, project_root)

# Try importing your KaviExtraction class from your package
try:
    from tamilkavi.tamilkavipy import KaviExtraction
except ImportError:
    pytest.fail("Could not import KaviExtraction from your 'tamilkavi' package. "
                "Ensure your package structure is correct (e.g., tamilkavi/tamilkavipy.py) "
                "and that you are running pytest from the project root, or install your package "
                "in editable mode (`pip install -e .`) first.")


# --- Fixture to create an instance of KaviExtraction ---
# This fixture will run once per test module (file).
# It instantiates KaviExtraction, which in turn loads data from your packaged kavisrc.
@pytest.fixture(scope="module")
def kavi_library_with_production_data():
    """Provides a KaviExtraction instance loaded with data from the packaged kavisrc."""
    try:
        # Instantiate your class - this triggers the data loading
        library = KaviExtraction()
        # Check if any data was loaded successfully
        if not library.saved_books:
             pytest.fail("KaviExtraction did not load any data from kavisrc. "
                         "Ensure kavisrc/*.json files are present in your source and included "
                         "in package_data/include_package_data in setup.py, and the package "
                         "is installed correctly.")
        return library
    except SystemExit as e:
        # If sys.exit was called during initialization (e.g., due to no files), fail the test
        pytest.fail(f"KaviExtraction initialization failed and called sys.exit: {e}")
    except Exception as e:
        # Catch any other unexpected errors during setup
        pytest.fail(f"An unexpected error occurred during KaviExtraction initialization: {e}")


# --- Basic Tests for KaviExtraction Filtering Methods ---
# These tests use the fixture to get a loaded library instance.
# You MUST update the placeholder values ("Author Name", "Book Title", etc.)
# with actual names and titles from your JSON files in tamilkavi/kavisrc/
# for these tests to pass correctly.

# Test get_authors method: finding a known author
def test_get_authors_known_author(kavi_library_with_production_data):
    library = kavi_library_with_production_data
    # >>> Replace "Anand Sundaramoorthy SA" with an actual author name from your kavisrc JSONs <<<
    author_name_to_find = "Anand Sundaramoorthy SA"
    authors = library.get_authors(author_name_to_find, library.saved_books)

    assert len(authors) == 1 # Assuming author names are unique at the top level
    assert authors[0].get('author') is not None # Ensure the author key exists
    assert authors[0]['author'].lower() == author_name_to_find.lower() # Check the found name (case-insensitive)

# Test get_authors method: not finding an unknown author
def test_get_authors_unknown_author(kavi_library_with_production_data):
    library = kavi_library_with_production_data
    # Use a name that definitely won't be in your data
    authors = library.get_authors("Non Existent Author 123XYZ", library.saved_books)
    assert len(authors) == 0

# Test get_book method: finding a known book by Tanglish title
def test_get_book_known_tanglish_title(kavi_library_with_production_data):
    library = kavi_library_with_production_data
    # >>> Replace "Kadhal Kavithaigal" with an actual book_title_tanglish from your kavisrc JSONs <<<
    book_title_to_find = "Kadhal Kavithaigal"
    books = library.get_book(book_title_to_find, library.saved_books)

    assert len(books) >= 1 # There might be multiple books with the same title across authors
    assert books[0].get('booktitle_tanglish', '').lower() == book_title_to_find.lower() # Check the found title

# Test get_book method: not finding an unknown book
def test_get_book_unknown_title(kavi_library_with_production_data):
    library = kavi_library_with_production_data
    # Use a title that definitely won't be in your data
    books = library.get_book("Non Existent Book ABC", library.saved_books)
    assert len(books) == 0


# Test get_titles method: finding a known poem title
def test_get_titles_known_title(kavi_library_with_production_data):
    library = kavi_library_with_production_data
    # >>> Replace "Muthal Kadhal" with an actual poem title from your kavisrc JSONs <<<
    poem_title_to_find = "Muthal Kadhal"
    poems = library.get_titles(poem_title_to_find, library.saved_books)

    assert len(poems) >= 1 # There might be multiple poems with the same title
    assert poems[0].get('title', '').lower() == poem_title_to_find.lower() # Check the found title


# Test get_titles method: not finding an unknown poem title
def test_get_titles_unknown_title(kavi_library_with_production_data):
    library = kavi_library_with_production_data
    # Use a title that definitely won't be in your data
    poems = library.get_titles("Non Existent Poem XYZ", library.saved_books)
    assert len(poems) == 0


# You can add more tests here for:
# - test_get_all_books(kavi_library_with_production_data) - Check the count and contents of all books returned
# - test_get_all_unique_titles(kavi_library_with_production_data) - Check the count and contents of unique titles
# - Test filtering combinations (e.g., get_book on data already filtered by author)
# - Test edge cases (e.g., kavisrc directory is empty, JSON file is empty, JSON file is malformed)
# - Test display functions (this is more advanced, requires capturing stdout)