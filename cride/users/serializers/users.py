
#django
from django.contrib.auth import authenticate
#Django rest framework
from rest_framework import serializers
from cride.users.models import Users


class UserModelSerializer(serializers.ModelSerializer):
    """Model serializer"""
    class Meta:
        model = Users
        field = ('username', 'first_name', 'last_name', 'email', 'phone_number')


class UserLoginSerializer(serializers.Serializer):
    """
        User login serializer
        handle thhe login request
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """check credentials"""

        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user__email=self.context['user'])
        return self.context['user'], token.key
