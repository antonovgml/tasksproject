from django.shortcuts import render

from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-date_created')
    context = {'tasks': tasks}

    return render(request, 'tasksapp/index.html', context)