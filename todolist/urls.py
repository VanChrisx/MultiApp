from django.urls import path
from todolist import views

urlpatterns = [
    path('tasks/', views.TasksList.as_view(), name='tasks'),
    path('create-task/', views.create_task, name='create-task'),
    path('add-task/', views.add_task, name='add-task'),
    path('complete-task/<int:pk>/', views.complete_task, name='complete-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
    path('all-tasks/', views.all_tasks, name='all_tasks'),
    path('completed-tasks/', views.completed_tasks, name='completed-tasks'),
    path('pending-tasks/', views.pending_tasks, name='pending-tasks')
]
