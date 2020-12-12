from django.urls import path
from .views import *


urlpatterns = [
	path('author/', ListAuthor.as_view()),
	path('genre/', ListGenre.as_view()),
	path('category/', ListCategory.as_view()),
	path('publisher/', ListPublisher.as_view()),
	path('book/', ListBook.as_view()),
	path('book/<int:pk_book>', DetailBook.as_view()),
	path('book/<int:pk_book>/chapter', ListChapter.as_view()),
	path('book/<int:pk_book>/chapter/<str:number>', DetailChapter.as_view()),
]
