from todolist_app import views
from django.urls import path, include

urlpatterns = [
    path('', views.todolist, name='todolist'),
]
