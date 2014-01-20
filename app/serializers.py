from rest_framework import serializers
from app.models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('id', 'author_name')

class BookSerializer(serializers.ModelSerializer):
	authors = AuthorSerializer(required=False)
	class Meta:
		model = Book
		fields = ('id', 'book_name', 'edition', 'authors')





