from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
# from braces.views import CsrfExemptMixin

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):

    #authentication_classes = []

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def filter_queryset(self, queryset):
        queryset = super(TaskViewSet, self).filter_queryset(queryset)
        return queryset.order_by('id')
