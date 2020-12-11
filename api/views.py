from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *


class ListBook(APIView):
	def get(self, request, format=None):
		books = Book.objects.all()
		serializer = SerBook(books, many=True)
		return Response(serializer.data)


class DetailBook(APIView):
	def get_object(self, pk):
		try:
			return Book.objects.get(pk=pk)
		except Book.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		data = self.get_object(pk)
		serializer = SerBook(data)
		return Response(serializer.data)


class ListChapter(APIView):
	def get(self, request, pk, format=None):
		chapters = Chapter.objects.filter(book=pk)
		serializer = SerChapterNotText(chapters, many=True)
		return Response(serializer.data)


class DetailChapter(APIView):
	def get_object(pk):
		try:
			return Chapter.objects.get(pk=pk)
		except Chapter.DoesNotExist:
			raise Http404

	def get(self, request, book, number, format=None):
		data = self.get_object(book=book, number=number)
		serializer = SerChapter(data)
		return Response(serializer.data)
