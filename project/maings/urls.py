from .views import *
# from django.urls import path 
from rest_framework.routers import DefaultRouter as DR 
from maings.views import (
    AboutMeView,ProjectsCategoryView,ProjectView,
    ProjectsImageView,ContactView,SendGmailView
)

router = DR()
router.register('aboutme', AboutMeView, basename='about')
router.register('projectscategory', ProjectsCategoryView, basename='projectscategory')
router.register('project', ProjectView, basename='project')
router.register('projectsimage', ProjectsImageView, basename='projectsimage')
router.register('contact', ContactView, basename='contact')
router.register('sendgmail', SendGmailView, basename='sendgmail')


urlpatterns = []

urlpatterns += router.urls


# urlpatterns = [
#     path('registration/', RegistrationView.as_view()),
#     path('login/', AutorisationView.as_view()),
# ]
