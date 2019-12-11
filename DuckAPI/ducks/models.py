from django.db import models

# Create your models here.


class Duck(models.Model):
    duckname = models.CharField(max_length=255)
    ducklastname = models.CharField(max_length=255)
    duckmail = models.EmailField(max_length=255)
    duckage = models.IntegerField()


    def __str__(self):
        return self.duckname
