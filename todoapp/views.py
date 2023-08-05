from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    form = TodoForm()

    #logic
    if request.method=="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'todos':todos,'form':form}
    return render(request,'list.html',context)

def update(request,pk): #pk is the primary key and can be named whatever you want
    list= Todo.objects.get(id=pk)
    form= TodoForm(instance=list)

    if request.method == "POST":
        form = TodoForm(request.POST,instance=list)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context={'form':form}
    return render(request,'update.html',context)

def delete(request,pk):
    task= Todo.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    context={'task':task}
    return render(request,'delete.html',context)
