from rest_framework import viewsets, mixins, generics, permissions
from maings.models import *
from maings.serializers import (
    SchoolSerializer,TeacherSerializer, StudentSerializer, 
)

class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def perfore_create(self, serializer):
        return serializer.save(user=self.request.user)


class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer