from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from datetime import date, datetime


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    today = date.today()
    date_today = today.strftime("%B %d, %Y")

    now = datetime.now()
    time_now = now.strftime("%H:%M")

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,

        'date_today': date_today,
        'time_now': time_now,
    }
    return render(request, 'todo/tasks.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'todo/update_task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {
        'task': task
    }
    return render(request, 'todo/delete_task.html', context)
