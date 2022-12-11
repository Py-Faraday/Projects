from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from maings.serializers import (
    RegistrationSerializers,
)

from rest_framework.authtoken.models import Token

User = get_user_model()

class RegistrationView(APIView):

    def post(self, request):
        serializer = RegistrationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        
        if User.objects.filter(username=username).exists():
            return Response({'message': 'User with such username is already exists'})
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # user_set_password(password)
        # user.save()
        
        token = Token.objects.create(user=user)
        return Response({'token':token.key})