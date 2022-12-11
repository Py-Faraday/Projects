from rest_framework import viewsets
from .models import *
from .serializers import *

class AboutMeView(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer 
    
class ProjectsCategoryView(viewsets.ModelViewSet):
    queryset = ProjectsCategory.objects.all()
    serializer_class = ProjectsCategorySerializer
    
class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer  
    
class ProjectsImageView(viewsets.ModelViewSet):
    queryset = ProjectsImage.objects.all()
    serializer_class = ProjectsImageSerializer 
    
class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer 
    
class SendGmailView(viewsets.ModelViewSet):
    queryset = SendGmail.objects.all()
    serializer_class = SendGmailSerializer 