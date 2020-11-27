from django.db import models


class Author(models.Model):
	first_name = models.CharField(max_length=255, verbose_name="Имя", default='')
	last_name = models.CharField(max_length=255, verbose_name="Фамилия", default='')
	patro_name = models.CharField(max_length=255, verbose_name="Отчество", default='')

	def __str__(self):
		return self.last_name + " " + self.first_name + " " + self.patro_name


class Genre(models.Model):
	title = models.CharField(max_length=255, verbose_name="Жанр", default='')

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=255, verbose_name="Категория", default='')

	def __str__(self):
		return self.title


class Publisher(models.Model):
	title = models.CharField(max_length=255, verbose_name="Издательство", default='')

	def __str__(self):
		return self.title


class Book(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название", default='')
	date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации')
	author = models.ManyToManyField(Author)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING())
	genre = models.ManyToManyField(Genre)
	publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING())

	def __str__(self):
		return self.title
