from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AboutMe(models.Model):
    user = models.ForeignKey(User, verbose_name="", on_delete=models.CASCADE, related_name='User')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    biography = models.TextField()
    photo = models.ImageField(upload_to='images/photo.jpg', height_field=None, width_field=None, max_length=None)
   

class ProjectsCategory(models.Model):
    title = models.CharField(max_length=150)
    pre_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/ph.jpg')
    
class Project(models.Model):
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE, related_name='User')
    category = models.ForeignKey(ProjectsCategory, verbose_name=(""), on_delete=models.CASCADE)
    project_name = models.CharField(max_length=150)
    pre_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/photo.jpg', height_field=None, width_field=None, max_length=None)
    link = models.FileField(upload_to='images/ph.jpg', max_length=100)
    date_develop = models.DateField(auto_now=False, auto_now_add=False)
    
class ProjectsImage(models.Model):
    project = models.ForeignKey(Project, verbose_name=(""), on_delete=models.CASCADE, related_name='ProjectImage')
    image = models.ImageField(upload_to='images/photo.jpg', height_field=None, width_field=None, max_length=None)
  
    
class Contact(models.Model):
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    logo = models.CharField(max_length=50)
    link = models.FileField(upload_to='images/ph.jpg', max_length=100)
    name = models.CharField(max_length=50)
    
    
class SendGmail(models.Model):
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    message = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)