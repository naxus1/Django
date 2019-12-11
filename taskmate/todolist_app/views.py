from django.shortcuts import render

from todolist_app.models import TaskList

# Create your views here.
def todolist(request):
    all_task = TaskList.objects.all
    return render(request, 'todolist.html', {'all_task': all_task})

def about(request):
    context = {
        'about_text': 'Welcome About Page'
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'contact_text': 'Welcome Contact Page'
    }
    return render(request, 'contact.html', context)
