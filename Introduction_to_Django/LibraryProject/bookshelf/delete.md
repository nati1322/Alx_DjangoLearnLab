from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()  # Delete the book
Book.objects.all() # Check if any books are present.
<QuerySet []> # Empty query set. Book is deleted

# To delete all books (use with extreme caution!)
# Book.objects.all().delete()