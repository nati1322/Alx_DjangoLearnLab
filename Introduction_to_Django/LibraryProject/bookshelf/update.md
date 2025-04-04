book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"  # Change the title
book.save()  # Save the changes to the database
print(book.title)  # Output: Nineteen Eighty-Four