# Base imports
import jwt

# Django imports
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.signals import user_logged_in, user_logged_out

# DRF imports
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings

# Project imports
from .models import User
from .serializers import UserSerializer
from common.exceptions import response_from_exception


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this URL
    permission_classes = [AllowAny,]

    def post(self, request):
        try:
            user = request.data

            serializer = UserSerializer(data=user)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return response_from_exception('user.views.UserLoginAPIView.post', e)
            

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            # serializer to handle turning our User object into 
            # something that can be JSONified and sent to the client.
            serializer = self.serializer_class(request.user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return response_from_exception('user.views.UserLoginAPIView.post', e)

    def put(self, request, *args, **kwargs):
        try:
            serializer_data = request.data.get('user', {})

            serializer = UserSerializer(
                request.user, data=serializer_data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return response_from_exception('user.views.UserLoginAPIView.post', e)


class UserDeleteAPIView(DestroyAPIView):
    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)

    def destroy(self, request):
        pass


class UserLoginAPIView(APIView):
    # Allow any user (authenticated or not) to access this URL
    permission_classes = [AllowAny,]

    def get_context(self, method_name: str) -> str:
        return f'{__name__}.{__class__.__name__}.{method_name}'

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = User.objects.get(email=email, password=password, is_active=True)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = jwt.encode(payload, settings.SECRET_KEY)
            
                    user_details = {}
                    user_details['name'] = f'{user.first_name} {user.last_name}'
                    user_details['token'] = token
                    user_logged_in.send(sender=user.__class__, request=request, user=user)
            
                    return Response(user_details, status=status.HTTP_200_OK)
                except Exception as e:
                    raise e
            else:
                payload = {
                    'error': 'Can not authenticate with the given credentials, or the account has been deactivated'
                }
                return Response(payload, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            payload = {'error': 'Please provide an email and a password'}
            return Response(payload, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return response_from_exception(self.get_context('post'), e)
