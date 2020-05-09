from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList


# Create your views here.
def todolist(request):
    all_tasks = TaskList.objects.all()
    return render(request, 'todolist_app/todolist.html', {'all_tasks': all_tasks})

def about(request):
    context = {
        "about_text":"Welcome to todo list about"
    }
    return render(request, 'todolist_app/about.html', context)

def contact(request):
    context = {
        "contact_text":"Welcome to todo list contact"
    }
    return render(request, 'todolist_app/contact.html', context)


