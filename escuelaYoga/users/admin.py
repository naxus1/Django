""" Administrador de Perfil de usuario  """

# Django
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib import admin

# Modelos
from users.models import Profile
from django.contrib.auth.models import User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ """
    list_display = ('user', 'age', 'picture')
    list_display_links = ('user',)
    list_editable = ('picture',)
    search_fields = ('user__username','user__email')
    list_filter = ('created',)

    fieldsets = (
        ('Perfil', {
                'fields': (('user', 'picture', 'age'),),
            }),
        (
            'Metadata', 
            {
                'fields': (('created', 'updated'),),
            }
        )
    )
    readonly_fields = ('created', 'updated')


class ProfileInline(admin.StackedInline):
     model = Profile
     verbose_name_plural = 'Perfil'


class UserAdmin(BaseAdmin):
    """  """
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
    )


admin.site.unregister(User,)
admin.site.register(User, UserAdmin)

