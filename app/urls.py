from django.urls import path
from . import views  # Import views from the same app

# Define URL patterns for this app
urlpatterns = [
    path('tasks/', views.view_tasks, name='view_tasks'),               # For viewing tasks
    path('tasks/add/', views.add_task, name='add_task'),               # For adding a task
    path('tasks/delete/<int:index>/', views.delete_task, name='delete_task'),  # For deleting a task by index
]

