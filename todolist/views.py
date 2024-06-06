from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .form import TaskForm
from .models import Task

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods
from django.contrib import messages

# Create your views here.


@login_required
def create_task(request):
    return render(request, 'partials/create-task.html', {'form': TaskForm})


@login_required
def add_task(request):
    try:
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        return redirect('tasks')
    except ValueError:
        return render(request, 'tasks.html', {
            'form': TaskForm,
            'error': 'Complete todos los campos'
        })


class TasksList(LoginRequiredMixin, ListView):
    template_name = 'tasks.html'
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


@require_http_methods(['DELETE'])
def delete_task(request, pk):
    Task.objects.get(pk=pk).delete()

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'partials/tasks-list.html', {'tasks': tasks})


def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = True
    task.save()

    tasks = Task.objects.filter(user=request.user)
    return render(request, 'partials/tasks-list.html', {'tasks': tasks})


require_http_methods(['GET'])


@login_required
def all_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'partials/tasks-list.html', {
        'tasks': tasks
    })


require_http_methods(['GET'])


@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, status=True)
    return render(request, 'partials/tasks-list.html', {
        'tasks': tasks
    })


require_http_methods(['GET'])


@login_required
def pending_tasks(request):
    tasks = Task.objects.filter(user=request.user, status=False)
    return render(request, 'partials/tasks-list.html', {
        'tasks': tasks
    })
