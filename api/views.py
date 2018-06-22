from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer
from tasksapp.models import Task


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
