from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_task, name='index'),
    path('post', views.post_task, name='post'),
]
