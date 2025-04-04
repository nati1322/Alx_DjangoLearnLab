from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password','email', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validate_data):
            password = validate_data.pop('password', None)
            user = get_user_model().objects.create_user(**validate_data)
            if password is not None:
                user.set_password(password)
            user.save()
            token = Token.objects.create(user=user)
            return user, token
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User is deactivated.')
                return data
            else:
                raise serializers.ValidationError('Unable to login with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')
        
            