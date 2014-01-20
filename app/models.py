# Create your models here.
from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=255)

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
