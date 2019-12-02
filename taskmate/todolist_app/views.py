from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    context = {
        'welcome_text': 'Welcome todolist Page'
    }
    return render(request, 'todolist.html', context)

def about(request):
    context = {
        'welcome_text': 'Welcome About Page'
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'welcome_text': 'Welcome Contact Page'
    }
    return render(request, 'contact.html', context)
