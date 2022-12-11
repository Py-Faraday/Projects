from django.urls import path
from maings.views import RegistrationView

urlpatterns = [
    path('registration/',RegistrationView.as_view()),
]