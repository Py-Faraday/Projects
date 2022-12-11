from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class School(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField(default=0)
    address = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teachers', null=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField(default=0)
    clas = models.CharField(max_length=120)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students', null = True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField(default=0)
    clas = models.CharField(max_length=120)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')