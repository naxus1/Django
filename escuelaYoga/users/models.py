""" Class User """

# Django
from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    """ Se define la clase usuario """
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    age = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Retorna el nombre de usuario creado """
        return self.user.username

    class META:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil"
        app_label = 'Perfil'