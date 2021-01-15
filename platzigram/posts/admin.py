# Django
from django.contrib import admin

#  Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'photo')
    list_display_links = ('user', 'title')
    list_editable = ('photo',)
    search_fields = ('user__email', 'title')




