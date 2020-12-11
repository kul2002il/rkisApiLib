from rest_framework import serializers
from .models import Author, Genre, Category, Publisher, Chapter, Book


class SerAuthor(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'


class SerAuthor(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = '__all__'


class SerAuthor(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class SerAuthor(serializers.ModelSerializer):
	class Meta:
		model = Publisher
		fields = '__all__'


class SerAuthor(serializers.ModelSerializer):
	class Meta:
		model = Chapter
		fields = '__all__'


class SerBook(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'
