from bookshelf.models import Book  # Import the Book model
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Output: 1984 (because of the __str__ method)
book.id # To see the ID of the created book