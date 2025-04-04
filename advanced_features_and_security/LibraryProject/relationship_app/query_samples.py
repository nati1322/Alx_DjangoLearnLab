import os
import django
import sys

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
print("DJANGO_SETTINGS_MODULE:", os.environ.get("DJANGO_SETTINGS_MODULE"))
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample Data Creation (for demonstration)
author = Author.objects.create(name="Jane Doe")
book1 = Book.objects.create(title="Python Basics", author=author)
book2 = Book.objects.create(title="Django Unleashed", author=author)
library1 = Library.objects.create(name="Central Library")
library1.books.add(book1, book2)
librarian1 = Librarian.objects.create(name="John Smith", library=library1)

# Queries
# Query all books by a specific author
author_books = Book.objects.filter(author=author)
print("Books by Jane Doe:")
for book in author_books:
    print(book.title)

# List all books in a library
library_books = library1.books.all()
print("\nBooks in Central Library:")
for book in library_books:
    print(book.title)

# Retrieve the librarian for a library
library_librarian = Librarian.objects.get(library=library1)
print(f"\nLibrarian for Central Library: {library_librarian.name}")

# Retrieve a Library by name
library_name = "Central Library"
try:
    library_by_name = Library.objects.get(name=library_name)
    print(f"\nLibrary found by name '{library_name}': {library_by_name}")
except Library.DoesNotExist:
    print(f"\nLibrary with name '{library_name}' not found.")

# Retrieve an Author by name
author_name = "Jane Doe"
try:
    author_by_name = Author.objects.get(name=author_name)
    print(f"\nAuthor found by name '{author_name}': {author_by_name}")
except Author.DoesNotExist:
    print(f"\nAuthor with name '{author_name}' not found.")

# Filter books by author object.
try:
    books_by_author_object = Book.objects.filter(author=author)
    print(f"\nBooks filtered by author object '{author.name}':")
    for book in books_by_author_object:
        print(book.title)
except Author.DoesNotExist:
    print(f"Author Object does not exist.")