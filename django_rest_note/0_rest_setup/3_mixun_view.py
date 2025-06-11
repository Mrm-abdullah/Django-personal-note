from django.shortcuts import render
from .models import Rest_Api
from .serializers import Rest_ApiSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView

# Create your views here.

"""
class Rest_api( ListModelMixin,  CreateModelMixin, GenericAPIView):
    queryset = Rest_Api.objects.all()
    serializer_class = Rest_ApiSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Rest_api_detail( RetrieveModelMixin,  UpdateModelMixin,  DestroyModelMixin, GenericAPIView):
    queryset = Rest_Api.objects.all()
    serializer_class = Rest_ApiSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""

# concrete
"""
from .models import Rest_Api
from .serializers import Rest_ApiSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class Rest_api(ListCreateAPIView):
    queryset = Rest_Api.objects.all()
    serializer_class = Rest_ApiSerializer

class Rest_api_detail(RetrieveUpdateDestroyAPIView):
    queryset = Rest_Api.objects.all()
    serializer_class = Rest_ApiSerializer
"""

# model viewsets
"""
from .models import Rest_Api
from .serializers import Rest_ApiSerializer
from rest_framework import viewsets
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Rest_Api.objects.all()
    serializer_class = Rest_ApiSerializer


# url

from django.contrib import admin
from django.urls import path, include
from  drapi import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', views.BookViewSet, basename='rest')


urlpatterns = [
    path('', include(router.urls)),
]
"""