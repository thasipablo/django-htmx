from django.shortcuts import render

from .models import Task


# Rendering the home page
def index(request):
  tasks = Task.objects.all().order_by('-id')
  return render(request, 'task/index.html', {'tasks': tasks})

def create_task(request):
  title = request.POST.get('title')
  task =  Task.objects.create(title=title)
  task.save()
  tasks =  Task.objects.all().order_by('-id')
  return render(request, 'task/includes/task-list.html', {'tasks': tasks})

def delete_task(request, pk):
  task = Task.objects.get(pk=pk)
  task.completed = True
  task.save()
  tasks = Task.objects.all().order_by('-id')
  return render(request, 'task/includes/todo-list.html', {'tasks': tasks})

def mark_task(request, pk):
  task = Task.objects.ger(pk=pk)
  task.delete()
  tasks = Task.objects.all().order_by('-id')
  return render(request, 'task/includes/task-list.html', {'tasks': tasks})
