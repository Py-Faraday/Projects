from django.urls import path 
from maings.views import index

urlpatterns = [
    path('', index, name='index')
]
