from django.urls import path
from .views import *


urlpatterns = [
	path('book/', ListBook.as_view()),
	path('book/<int:pk>', DetailBook.as_view()),
	path('book/<int:pk>/chapter', ListChapter.as_view()),
	path('book/<int:book>/chapter/<str:number>', DetailChapter.as_view()),
]
