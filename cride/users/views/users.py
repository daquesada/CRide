"""users views"""

#django rest framewor
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
#serializars
from cride.users.serializers import (UserLoginSerializer,UserModelSerializer)


class UserLoginApiView(APIView):
    """user login Api view"""
    def post(sefl, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user,token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
