from django.shortcuts import render, get_object_or_404
from maings.models import Post 


# Create your views here.

def index(request):
    template_name = 'index.html'
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, template_name, context)

def details_post(request, post_id):
    template_name = 'etail_post.html'
    post = get_object_or_404(Post,id=post_id)
    context = {
        'post':post
    }
    return render(request,template_name,context)
    