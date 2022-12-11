from rest_framework import serializers, exceptions


class RegistrationSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    

    def validate_password(self, value):
        if len(value) < 8:
            raise exceptions.ValidationError('Password is too short')
        elif len(value) > 24:
            raise exceptions.ValidationError('Password is too long')
        return value 