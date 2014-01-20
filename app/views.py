# Create your views here.

from app.models import Book, Author
from app.serializers import BookSerializer, AuthorSerializer
from rest_framework import generics

class BookList(generics.ListCreateAPIView):
    model = Book
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Book
    serializer_class = BookSerializer
    
class AuthorList(generics.ListCreateAPIView):
    model = Author
    serializer_class = AuthorSerializer
    filter_fields = ['author_name']
    
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Author
    serializer_class = AuthorSerializer