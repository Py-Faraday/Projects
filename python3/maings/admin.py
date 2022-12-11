from django.contrib import admin

from .models import *

admin.site.register(AboutMe)
admin.site.register(ProjectsCategory)
admin.site.register(Project)
admin.site.register(ProjectsImage)
admin.site.register(Contact)
admin.site.register(SendGmail)