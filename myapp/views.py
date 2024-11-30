

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .form import TaskForm, TaskFilterForm
from django.contrib import messages

# List all tasks
def task_list(request):
    tasks = Task.objects.all()

    # Filtering tasks
    if request.method == "GET" and ('priority' in request.GET or 'status' in request.GET):
        filter_form = TaskFilterForm(request.GET)
        if filter_form.is_valid():
            priority = filter_form.cleaned_data.get('priority')
            status = filter_form.cleaned_data.get('status')
            if priority:
                tasks = tasks.filter(priority=priority)
            if status:
                tasks = tasks.filter(status=status)
    else:
        filter_form = TaskFilterForm()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'filter_form': filter_form})

# Add a new task
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Edit an existing task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('task_list')

