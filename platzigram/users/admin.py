# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin register"""
    list_display = ('user',
                    'phone_number',
                    'website')
    list_display_links = ('user',)
    list_editable = ('phone_number',)
    search_fields = ('user__email',
                     'user__first_name',
                     'user__last_name',
                     'phone_number')
    list_filter = ('created', 'modified', 'user__is_active')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography',)
            )
        }),
        ('Meta Data', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    """ profile inline admin for users """
    model = Profile
    can_deleted = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin """
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active'

    )


admin.site.unregister(User,)
admin.site.register(User, UserAdmin)
