from django.urls import path
from .views import viewBook


urlpatterns = [
	path('', viewBook),
]
