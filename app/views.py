from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# In-memory list of tasks
task_list = []

# View for listing tasks
def view_tasks(request):
    return HttpResponse('<br>'.join(task_list) if task_list else "No tasks available.")

# View for adding a task
@csrf_exempt
def add_task(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            task_list.append(task)
            return HttpResponse("Task added!")
        return HttpResponse("No task description provided.")
    return HttpResponse("Only POST requests are allowed.")

# View for deleting a task
@csrf_exempt
def delete_task(request, index):
    try:
        task_list.pop(index)
        return HttpResponse("Task deleted!")
    except IndexError:
        return HttpResponse("Task not found.")

from django.http import HttpResponse

# Define your view functions here
def view_tasks(request):
    return HttpResponse("Here are the tasks.")

def add_task(request):
    return HttpResponse("Task added!")

def delete_task(request, task_id):
    return HttpResponse(f"Task {task_id} deleted.")
