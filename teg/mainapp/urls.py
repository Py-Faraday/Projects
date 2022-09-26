from rest_framework.routers import DefaultRouter as DR

from mainapp.views import(
    PostViewSet,ComentViewSet
)

router = DR()

router.register('posts',PostViewSet,basename = 'posts')

router.register('comments',ComentViewSet,basename = 'comments')

urlpatterns = []

urlpatterns += router.urls