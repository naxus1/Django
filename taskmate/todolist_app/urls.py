from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
