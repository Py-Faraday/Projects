from django.db import models
from datetime import date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=127, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'Пост: {self.title.capitalize()}'
    
class Comment(models.Model):
    past = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    text = models.TextField(verbose_name='Комментарии') 
    
    def __str__(self):
        return f'Комментарии: {self.text.capitalize()}'
     
class Categoras(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    
    def __str__(self) -> str:
        return f'Категории: {self.name.capitalize()}'

    
class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='Продукт')
    price = models.IntegerField(default=0, verbose_name='Цены')
    categor = models.ForeignKey(Categoras, on_delete=models.CASCADE, verbose_name='Категории')
    
    def __str__(self):
        return f'Продукты: {self.name.capitalize()}'
    