from rest_framework import serializers
import re

from .models import Author, Genre, Category, Publisher, Chapter, Book


class SerAuthor(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'


class SerGenre(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = '__all__'


class SerCategory(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class SerPublisher(serializers.ModelSerializer):
	class Meta:
		model = Publisher
		fields = '__all__'


class SerChapterNotText(serializers.ModelSerializer):
	class Meta:
		model = Chapter
		fields = 'number', 'title'

	def validate_number(self, value):
		if re.match('[0-9.]+', value) is None:
			raise serializers.ValidationError("Chapter number is not format.")
		return value


class SerChapter(SerChapterNotText):
	class Meta:
		model = Chapter
		fields = 'number', 'title', 'text'


class SerChapterPOST(SerChapterNotText):
	class Meta:
		model = Chapter
		fields = 'book', 'number', 'title', 'text'


class SerBook(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'
