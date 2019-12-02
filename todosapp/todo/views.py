from django.shortcuts import render, redirect
from .models import List
from .form import listform
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method=='POST':
        form=listform(request.POST or None)

        if form.is_valid():
            form.save()
            all_tasks=List.objects.all()
            messages.success(request,('Task has added to list'))

            return render(request,'home.html' , {'all_tasks': all_tasks })
    else:
        all_tasks=List.objects.all()
        return render(request, 'home.html' , {'all_tasks': all_tasks})
    return HttpResponse(messages)

def delete(request,list_id):
    task=List.objects.get(pk=list_id)
    task.delete()
    messages.success(request,('Task has been deleted'))
    return redirect('home')

def completed(request,list_id):
    task=List.objects.get(pk=list_id)
    task.completed=True
    task.save()
    return redirect('home')

def uncompleted(request,list_id):
    task=List.objects.get(pk=list_id)
    task.completed=False
    task.save()
    return redirect('home')

def edit (request,list_id):
    if request.method=="POST":
        task=List.objects.get(pk=list_id)
        form=listform(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,('Task has been edited'))
            return redirect('home')
    else:
        task=List.objects.get(pk=list_id)
        return render(request,'edit.html',{'task':task})
    return HttpResponse(messages)
