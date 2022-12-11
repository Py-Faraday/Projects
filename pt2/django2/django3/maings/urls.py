from django.urls import path
from maings.views import *

urlpatterns = [
    path('', index, name='index'),
    path('post_detail/<int:post_id>/', post_detail, name='post_detail'),
    path('create_post/', create_post, name='create_post'),
    path('update_post/<int:post_id>/', update_post, name='update_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]