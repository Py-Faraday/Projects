from rest_framework.viewsets import ModelViewSet
from mainapp.models import Coment
from mainapp.serializers import(
    Post,PostSerializer,ComentSerializer
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class ComentViewSet(ModelViewSet):
    queryset = Coment.objects.all()
    serializer_class = ComentSerializer