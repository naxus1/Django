from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages


# Create and show task
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New task added"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        return render(request, 'todolist_app/todolist.html', {'all_tasks': all_tasks})

# delete task
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

# edit task
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
    else:
        task_object = TaskList.objects.get(pk=task_id)
        return render(request, 'todolist_app/edit.html', {"task_obj":task_object})


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


