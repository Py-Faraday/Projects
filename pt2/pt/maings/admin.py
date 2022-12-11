from django.contrib import admin

# Register your models here.

from maings.models import Post,Comment,Categoras,Product


admin.site.register(Product)
admin.site.register(Categoras)
admin.site.register(Comment)
admin.site.register(Post)