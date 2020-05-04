from django.db import models

"""
 It was created models User and User Task
"""

# Model User
class User(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

# Model UserTask
class UserTask(models.Model):
    description = models.CharField(max_length=100)
    state = models.BooleanField(default=False)
    user_id = models.ForeignKey("User", related_name='user_task', verbose_name=("User"), on_delete=models.CASCADE)


    def __str__(self):
        return self.description

