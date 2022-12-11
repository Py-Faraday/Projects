from maings.models import School, Teacher, Student
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'id', 'name', 'address',
        )


class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Teacher
        fields = (
            'id', 'first_name', 'last_name', 'age', 'clas', 'school', 'user', 'username'
        )
        read_only_fields = (
            'user',
        )


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id', 'first_name', 'last_name', 'age', 'clas', 'school', 'user', 
        )