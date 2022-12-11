from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AboutMe(models.Model):
    user = models.ForeignKey(User, verbose_name="", on_delete=models.CASCADE, related_name='User')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    biography = models.TextField()
    photo = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=None)
    

    