from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        new_task = Task(
            task=request.POST['task'],
        )
        new_task.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks': tasks})

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')
