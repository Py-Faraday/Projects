from django.db import models
from django.contrib.auth import get_user_model

# User
# Post 
# Comment

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="post", on_delete=models.CASCADE)
    text = models.TextField()