# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth import get_user_model
# from rest_framework.authtoken.models import Token
# from maings.models import *


# User = get_user_model()


# class Post(models.Model):
#     title = models.CharField(max_length=127, verbose_name='Название')
#     description = models.TextField(verbose_name='Описание')
#     created_at = models.DateField(auto_now=True)
#     user = models.CharField(max_length=120, default='')
#     raiting = models.PositiveIntegerField(default=0)