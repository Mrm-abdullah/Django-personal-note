# create serializers.py in app
""" 
from rest_framework import serializers
from .models import Rest_Api

class Rest_ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rest_Api
        fields = ['teacher_name', 'course_name', 'course_durationss','seat']

class Rest_ApiSerializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=50)
    course_name = serializers.CharField(max_length=50)
    course_durationss = serializers.IntegerField()
    seat = serializers.IntegerField()


    def create(self, validated_data):
        return Rest_Api.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
        instance.course_name = validated_data.get('course_name', instance.course_name)
        instance.course_durationss = validated_data.get('course_durationss', instance.course_durationss)
        instance.seat = validated_data.get('seat', instance.seat)
        instance.save()
        return instance
"""


############################## view
""" 
from django.shortcuts import render

# Create your views here.
from .models import Rest_Api
from .serializers import Rest_ApiSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def Rest_Api_view(request):
    # complex data
    ra = Rest_Api.objects.all()
    # pythoon dict
    serializer = Rest_ApiSerializer(ra, many=True)
    # render json
    json_data = JSONRenderer().render(serializer.data)
    # json send to user
    return HttpResponse(json_data, content_type='application/json')

# model instance
def Rest_Api_details(request, pk):
    # complex data
    ra = Rest_Api.objects.get(id=pk)
    # pythoon dict
    serializer = Rest_ApiSerializer(ra)
    # render json
    json_data = JSONRenderer().render(serializer.data)
    # json send to user
    return HttpResponse(json_data, content_type='application/json')



@csrf_exempt
def Rest_Api_list(request):
    # if request.method == 'GET':
        # pass
    #     api = Rest_Api.objects.all()
    #     serializer = Rest_ApiSerializer(api, many=True)
    #     return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Rest_ApiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        id = data.get('id')
        data_id = Rest_Api.objects.get(id=id)
        serializer = Rest_ApiSerializer(data_id, data=data, partial=True) # partial=True sob update korte caile partial deoya lagbe na.
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    # res = {'msg':'successfully update data'}
    #         json_data = JSONRenderer().rander(res)
    #         return HttpResponse(json_data, content_type='application/json')
        
    #     json_data = JSONRenderer().rander(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json')
    
    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        id = data.get('id')
        data_id = Rest_Api.objects.get(id=id)
        data_id.delete()
        res = {'msg':'successfully update data'}
        json_data = JSONRenderer().rander(res)
        return HttpResponse(json_data, content_type='application/json')
# url

from django.urls import path
from  drapi import views
urlpatterns = [
    path('rest/', views.Rest_Api_view, name='rest'),
    path('rest/<int:pk>/', views.Rest_Api_details, name='rests'),
    path('restcreate/', views.Rest_Api_list, name='ral'),
]

"""


# py app
# get
"""
import requests
import json

URL = "http://127.0.0.1:8000/rest/"

response = requests.get(url=URL)
data = response.json()
print(data)
"""

# URL = "http://127.0.0.1:8000/restcreate/"

# create
"""
data = {
    'teacher_name': 'Abdul khalek',
    'course_name': 'english',
    'course_durationss': 3,
    'seat': 20
}

json_data = json.dumps(data)
response = requests.post(url=URL, data = json_data)
data = response.json()
print(data)
"""

# update
"""
data = {
    'id': 6,
    'teacher_name': 'tumiiiii',
    'course_name': 'ami'
}

json_data = json.dumps(data)
r = requests.put(url=URL, data = json_data)
data = r.json()
print(data)
"""

# delete
"""
data = {
    'id': 5,
}

json_data = json.dumps(data)
r = requests.delete(url=URL, data = json_data)
data = r.json()
print(data)
"""



