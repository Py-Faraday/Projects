from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=127, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateField(auto_now=True)
    
    @property
    def get_all_comments(self):
        return self.comments.all()
    
    
    @property
    def count_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()