from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=127)
    is_active: models.BooleanField(default=False)

    def str(self) -> str:
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Posts')
    post = models.TextField()
    rating = models.IntegerField(default=0, verbose_name='рейтинг')

    def __str__(self) -> str:
        return self.user.username


class Coment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='коментарий')
    comment = models.TextField(verbose_name='коментарий') 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата')