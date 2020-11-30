from django.contrib import admin

from .models import Author, Book, Publisher, Genre, Category

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Category)
