from rest_framework import serializers
from tasksapp.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer): # TODO
    """ map Task model instalce into JSON format """

    class Meta:
        """ map serializer's fields with model fields """
        model = Task

        fields = ('id', 'title', 'details', 'date_created')
        read_only_fields = ('date_created',)

