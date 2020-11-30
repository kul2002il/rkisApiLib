from rest_framework import serializers
from .models import Author, Publisher, Book, Category, Genre

class SerBook(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'title', 'date', 'author', 'category', 'genre', 'publisher')
