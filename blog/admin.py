from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified')


# Register your models here.
admin.site.register(Post, PostAdmin)
