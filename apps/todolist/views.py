from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


from apps.todolist.models import *
from apps.todolist.serialzers import *
# Create your views here.


class TaskViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin
                  ):
    queryset = TodoList.objects.all()
    serializer_class = TaskSerializer

