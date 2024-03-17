from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    content = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Home page of the site', 'content': content})


def about(request):
    return render(request,'about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Wrong shape'
    form = TaskForm()
    context = {
        'form': form,
        'error':error
    }
    return render(request,'create.html', context)


def update(request, id):
    error = ''
    task = Task.objects.get(id = id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Wrong shape'

    context = {
        'form': form,
        'error':error
    }
    return render(request,'update.html', context)


def delete(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('home')
