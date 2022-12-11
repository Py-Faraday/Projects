from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=127, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(auto_now=True)
    user = models.CharField(max_length=120, default='')
    raiting = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'Пост {self.title} создал {self.user}'
    