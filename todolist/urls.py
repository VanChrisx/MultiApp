from django.urls import path
from todolist import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('create-task/', views.create_task, name='create-task')
]
