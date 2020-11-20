#from https://www.django-rest-framework.org/tutorial/quickstart/

from rest_framework import serializers
from .models import Task

class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'pub_date', 'description']
