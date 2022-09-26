from dataclasses import field
from rest_framework import serializers

from mainapp.models import(
    User, Post, Coment
)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'post', 'rating', )

class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coment
        fields = ('id','user','post','comment','created_at', )