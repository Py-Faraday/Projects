from rest_framework import serializers
# exception
from .models import *

# class RegistrationSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#     email = serializers.CharField()
#     def validate_password(self,value):
#         if len(value) < 8:
#             raise exceptions.ValidationError('пароль меньше 8 символов')
#         elif len(value) > 32:
#             raise exceptions.ValidationError('пароль больше 32 символов')
#         return value


# class AutorisationSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
    
    
class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = (
            'user','first_name','last_name',
            'biography','photo'
        )
        
class ProjectsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsCategory
        fields = (
            'title','pre_description',
            'description','image'
        )
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'user','project_name','pre_description',
            'description','image',
            'link','date_developer'
        )
        
class ProjectsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsImage
        fields = (
            'project','image'
        )

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'user','logo','link','name'
        )
        
class SendGmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendGmail
        fields = (
            'user','first_name','last_name',
            'email','message',
            'phone_number','date'
        )
        