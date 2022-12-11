from django.urls import path

from .views import AboutMeView,AboutDetailView

urlpatterns = [
    path('', AboutMeView.as_view(), name='home'),
    path('aboutme/<int:pk>/', AboutDetailView.as_view(), name='about_detail'),    
]
