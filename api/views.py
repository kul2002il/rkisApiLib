from django.shortcuts import render, get_object_or_404
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


class ListAuthor(APIView):
	def get(self, request, format=None):
		data = Author.objects.all()
		serializer = SerAuthor(data, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SerAuthor(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ListGenre(APIView):
	def get(self, request, format=None):
		data = Genre.objects.all()
		serializer = SerGenre(data, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SerGenre(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ListCategory(APIView):
	def get(self, request, format=None):
		data = Category.objects.all()
		serializer = SerCategory(data, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SerCategory(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ListPublisher(APIView):
	def get(self, request, format=None):
		data = Publisher.objects.all()
		serializer = SerPublisher(data, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SerPublisher(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ListBook(APIView):
	def get(self, request, format=None):
		books = Book.objects.all()
		serializer = SerBook(books, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SerBook(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DetailBook(APIView):
	def get(self, request, pk_book, format=None):
		data = get_object_or_404(Book, pk=pk_book)
		serializer = SerBook(data)
		return Response(serializer.data)


class ListChapter(APIView):
	def get(self, request, pk_book, format=None):
		chapters = Chapter.objects.filter(book=pk_book)
		serializer = SerChapterNotText(chapters, many=True)
		return Response(serializer.data)

	def post(self, request, pk_book, format=None):
		get_object_or_404(Book, pk=pk_book)
		request.data['book'] = pk_book
		serializer = SerChapterPOST(data=request.data) # , context={'book': pk_book}, partial=True
		# serializer.initial_data.book = pk_book
		print(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DetailChapter(APIView):
	def get(self, request, pk_book, number, format=None):
		data = get_object_or_404(Chapter, book=pk_book, number=number)
		serializer = SerChapter(data)
		return Response(serializer.data)
