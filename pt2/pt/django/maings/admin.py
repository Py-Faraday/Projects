from django.contrib import admin

# Register your models here.

from maings.models import (
    Post,Tag,Like
)

admin.site.register(Like)
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title','count_likes'
)    
    
admin.site.register(Post, PostAdmin)