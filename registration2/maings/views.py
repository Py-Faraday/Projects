from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from django.views import generic

class AboutMeView(ListView):
    model = AboutMe
    template_name = 'home.html'

class AboutDetailView(DetailView):
    model = AboutMe
    template_name = 'about_detail.html'
    
    