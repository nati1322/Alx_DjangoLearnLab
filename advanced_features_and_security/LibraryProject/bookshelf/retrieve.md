book = Book.objects.get(title="1984")  # Get the book by title
print(book.title)  # Output: 1984
print(book.author)  # Output: George Orwell
print(book.publication_year)  # Output: 1949

# Retrieve all books
all_books = Book.objects.all()
for b in all_books:
...     print(b.title)