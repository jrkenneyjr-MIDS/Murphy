"""Documentation"""

from django.shortcuts import redirect, render
from todo_app.forms import TaskForm
from todo_app.models import Task


def task_list(request):
    """_summary_"""
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})


def task_detail(request, pk):
    """_summary_"""
    task = Task.objects.get(id=pk)
    return render(request, "task_detail.html", {"task": task})


def task_create(request):
    """_summary_"""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "task_form.html", {"form": form})


def task_update(request, pk):
    """_summary_"""
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task_form.html", {"form": form})


def task_delete(request, pk):
    """_summary_"""
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("task_list")
