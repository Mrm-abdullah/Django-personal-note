class Rest_ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rest_Api
        fields = ['teacher_name', 'course_name', 'course_durationss','seat']


#  view

from django.shortcuts import render
from .models import Rest_Api
from .serializers import Rest_ApiSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
# function base
"""
@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def Rest_api_detail(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            Rest = Rest_Api.objects.get(id=id)
            serializer = Rest_ApiSerializer(Rest)
            return Response(serializer.data)
        Rest = Rest_Api.objects.all()
        serializer = Rest_ApiSerializer(Rest, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = Rest_ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        id = pk
        Rest = Rest_Api.objects.get(id=id)
        serializer = Rest_ApiSerializer(Rest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        id = pk
        Rest = Rest_Api.objects.get(id=id)
        serializer = Rest_ApiSerializer(Rest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        id = pk
        Rest = Rest_Api.objects.get(id=id)
        Rest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
@api_view(['GET', 'POST'])
def Rest_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""


# class based

"""
class Rest_api_detail(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            Rest = Rest_Api.objects.get(id=id)
            serializer = Rest_ApiSerializer(Rest)
            return Response(serializer.data)
        Rest = Rest_Api.objects.all()
        serializer = Rest_ApiSerializer(Rest, many=True)
        return Response(serializer.data)     
    def post(self, request, format=None):
        serializer = Rest_ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk, format=None):
        id = pk
        Rest = Rest_Api.objects.get(id=id)
        serializer = Rest_ApiSerializer(Rest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, format=None):
        id = pk
        Rest = Rest_Api.objects.get(id=id)
        serializer = Rest_ApiSerializer(Rest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        id = pk
        Rest = Rest_Api.objects.get(id=id)
        Rest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""

"""
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


