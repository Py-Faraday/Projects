from django.contrib import admin
from maings.models import Student, Teacher, School
                           
admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)