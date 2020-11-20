#How to use serializer from https://www.askpython.com/django/django-listview

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Task
from .serializer import Serializer
from django.http import JsonResponse 
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_task(request: HttpRequest):
    all_tasks = Task.objects.all()#.order_by('-date_joined')
    serializer = Serializer(all_tasks, many =True)
    return JsonResponse(serializer.data, safe =False)


    