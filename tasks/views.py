#How to use serializer from https://www.askpython.com/django/django-listview

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Task
from .serializer import Serializer
from .forms import Form
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_task(request: HttpRequest):
    all_tasks = Task.objects.all()#.order_by('-date_joined')
    serializer = Serializer(all_tasks, many =True)
    return JsonResponse(serializer.data, safe =False)

@csrf_exempt
def post_task(request):
    form = Form(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse(form.data,status =201)
    else:
        form =Form()
        context = {
            'form':form
        }
        return HttpResponse("TRISTEZA")

    