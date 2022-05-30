from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title':'Home page of the site', 'tasks':tasks})

def about(request):
    return render(request,'main/about.html')


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
    return render(request,'main/create.html', context)