from django.db import models


class Author(models.Model):
	first_name = models.CharField(max_length=255, verbose_name="Имя", default='')
	last_name = models.CharField(max_length=255, verbose_name="Фамилия", default='')
	patro_name = models.CharField(max_length=255, verbose_name="Отчество", default='')

	def __str__(self):
		return self.last_name + " " + self.first_name + " " + self.patro_name


class Genre(models.Model):
	title = models.CharField(max_length=255, verbose_name="Жанр", default='', unique=True)

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=255, verbose_name="Категория", default='', unique=True)

	def __str__(self):
		return self.title


class Publisher(models.Model):
	title = models.CharField(max_length=255, verbose_name="Издательство", default='', unique=True)

	def __str__(self):
		return self.title


class Book(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название", default='')
	date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации')
	author = models.ManyToManyField(Author)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
	genre = models.ManyToManyField(Genre)
	publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, default=1)

	def __str__(self):
		return self.title


class Chapter(models.Model):
	number = models.CharField(max_length=25, verbose_name="Номер", default='')
	title = models.CharField(max_length=255, verbose_name="Название", default='')
	text = models.TextField()
	book = models.ForeignKey(Book, on_delete=models.CASCADE)

	class Meta:
		unique_together = (('book', 'number'),)

	def __str__(self):
		return self.title
