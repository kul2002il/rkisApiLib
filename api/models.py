from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=255, verbose_name="Имя", default='')
	last_name = models.CharField(max_length=255, verbose_name="Фамилия", default='')
	patro_name = models.CharField(max_length=255, verbose_name="Отчество", default='')

	def __str__(self):
		return self.last_name + " " + self.first_name + " " + self.patro_name

class Book(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название", default='')
	datetime = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата публикации')
	author = models.ManyToManyField(Author)

	def __str__(self):
		return self.title