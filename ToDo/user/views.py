from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.permissions import AllowAny

@api_view(['POST'])
def login_user(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    else:
        message = {'detail': 'invalid username or password!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        data = request.data
        user = User.objects.create(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            username = data.get('email'),
            email = data.get('email'),
            password = make_password(data.get('password')) 
        )
        
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Can not register user! try again'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)