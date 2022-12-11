from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    
    def __str__(self):
        return f'Тэги:{self.name}'
    
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    

  
class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    
    @property
    def count_likes(self):
        return self.likes.count()
    
    
    def __str__(self):
        return f'Посты:{self.title}'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
    
    
class Like(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, verbose_name='Пост', related_name='like')
    
    
    def __str__(self):
        return f'Лайк:{self.post.title}'  
    
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки' 