from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
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


    # DELETE entire Tasks collection
    def delete(self, request, *args, **kwargs):

        # Task.objects.all().delete() # this might be dropped
        # so doing this via iterator
        for x in Task.objects.all().iterator(): x.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
