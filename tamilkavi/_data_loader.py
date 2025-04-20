import json
import os
from glob import glob
from ._models import KavithaiCollection, Author 

_current_dir = os.path.dirname(__file__)
_kavisrc_path = os.path.join(_current_dir, 'kavisrc') 

_collection_instance = None 

def load_data():
    """Loads data from all JSON files in kavisrc/ and returns a KavithaiCollection instance."""
    global _collection_instance
    if _collection_instance is not None:
        return _collection_instance 

    loaded_authors = []
    for file_path in glob(os.path.join(_kavisrc_path, '*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                author_data = json.load(f)

            if "author" in author_data and "contact" in author_data and "books" in author_data and isinstance(author_data["books"], list):
                loaded_authors.append(Author(
                    author=author_data["author"],
                    contact=author_data["contact"],
                    books_data=author_data["books"] 
                ))
            else:
                 print(f"Warning: Skipping file {os.path.basename(file_path)} - Invalid data structure.")

        except FileNotFoundError:
            print(f"Error: Data file not found at {file_path}")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {file_path}")
        except Exception as e:
            print(f"An unexpected error occurred while loading {file_path}: {e}")

    if loaded_authors:
        _collection_instance = KavithaiCollection(authors=loaded_authors)
        return _collection_instance
    else:
        print("Error: No valid author data loaded.")
        return None

kavithai_collection = load_data()