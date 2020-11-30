from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import Book
from .serializers import SerBook


@api_view(['GET'])
def viewBook(request):
	if request.method == 'GET':
		bbs = Book.objects.all()
		serializer = SerBook(bbs, many=True)
		return Response(serializer.data)
