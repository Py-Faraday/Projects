from rest_framework.routers import DefaultRouter as DR
from django.urls import path
from maings.views import (
    SchoolView, TeacherView, StudentView,StudentRetrieveView
)

router = DR()
router.register('schools', SchoolView, basename='school')
router.register('teachers', TeacherView, basename='teacher')

urlpatterns = [
    path('student_list/',StudentView.as_view(), ),
    path('student_list/<int:pk>',StudentRetrieveView.as_view(),)
]

urlpatterns += router.urls
