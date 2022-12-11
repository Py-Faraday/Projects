from django import forms 
from maings.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 
            'description'
        )