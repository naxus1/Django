from django.contrib import admin
from tasks.models import User, UserTask

# Register your models here.
admin.site.register(User)
admin.site.register(UserTask)
