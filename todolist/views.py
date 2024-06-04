from django.shortcuts import render
from .form import TaskForm

# Create your views here.


def tasks(request):
    return render(request, 'tasks.html')


def create_task(request):
    return render(request, 'partials/create-task.html', {'form': TaskForm})
