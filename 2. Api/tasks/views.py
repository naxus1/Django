from django.shortcuts import render 
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from tasks.models import User, UserTask
from tasks.serializers import UserSerializer, TaskSerializer

# Create your views here.
class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 

@csrf_exempt 
def user_list(request): 
    if request.method == 'GET': 
        users = User.objects.all() 
        user_serializer = UserSerializer(users, many=True) 
        return JSONResponse(user_serializer.data) 
 
    elif request.method == 'POST': 
        user_data = JSONParser().parse(request) 
        user_serializer = UserSerializer(data=user_data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JSONResponse(user_serializer.data, \
                status=status.HTTP_201_CREATED) 
        return JSONResponse(user_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST) 

@csrf_exempt 
def user_detail(request, pk): 
    try: 
        user = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        user_serializer = UserSerializer(user) 
        return JSONResponse(user_serializer.data) 
 
    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        user_serializer = UserSerializer(user, data=user_data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JSONResponse(user_serializer.data) 
        return JSONResponse(user_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        user.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt 
def task_list(request): 
    if request.method == 'GET': 
        task = UserTask.objects.all()
        task_list = TaskSerializer(task, many=True) 
        return JSONResponse(task_list.data)

    elif request.method == 'POST': 
        task_data = JSONParser().parse(request) 
        task_serializer = TaskSerializer(data=task_data) 
        if task_serializer.is_valid(): 
            task_serializer.save() 
            return JSONResponse(task_serializer.data, \
                status=status.HTTP_201_CREATED) 
        return JSONResponse(task_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt 
def task_view(request, pk): 
    try: 
        task = UserTask.objects.get(pk=pk) 
    except UserTask.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        task_serializer = TaskSerializer(task) 
        return JSONResponse(task_serializer.data) 
 
    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        task_serializer = TaskSerializer(task, data=user_data) 
        if task_serializer.is_valid(): 
            task_serializer.save() 
            return JSONResponse(task_serializer.data) 
        return JSONResponse(task_serializer.errors, \
            status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        task.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt 
def task_user(request, pk):
    try: 
        user = User.objects.get(pk=pk)
    except User.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    user_task = UserTask.objects.filter(user_id=user)
 
    if request.method == 'GET': 
        task_serializer = TaskSerializer(user_task, many=True) 
        return JSONResponse(task_serializer.data)
