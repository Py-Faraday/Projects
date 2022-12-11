from django.urls import path
from maings.views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:post_id>', details_post, name='detail_post')
]