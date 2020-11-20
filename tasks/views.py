#How to use serializer from https://www.askpython.com/django/django-listview

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Task
from .serializer import Serializer
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_task(request: HttpRequest):
    all_tasks = Task.objects.all()#.order_by('-date_joined')
    serializer = Serializer(all_tasks, many =True)
    return JsonResponse(serializer.data, safe =False)

def post_task(request):
    data = JSONParser().parse(request)
    serializer =Serializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status =201)
    else: 
        return HttpResponse("TRISTEZA")
        #return JsonResponse(serializer.errors,status = 400)

    