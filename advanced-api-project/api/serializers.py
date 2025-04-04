from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    # The BookSerializer serializes all fields of the Book model and includes custom validation for publication_year.
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        # Ensure the publication year is not in the future.
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    # The AuthorSerializer serializes the name field and includes a nested BookSerializer to serialize related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']