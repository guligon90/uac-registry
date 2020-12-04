# Base imports
import jwt

# Django imports
from django.conf import settings
from django.contrib.auth.signals import user_logged_in

# DRF imports
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

# Project imports
from common.exceptions import response_from_exception
from common.views import crud
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def list_users(request):
    return crud.list_instances(request, UserSerializer, User)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def create_user(request):
    return crud.create_instance(request, UserSerializer)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def user_detail(request, pk):
    return crud.instance_detail(request, pk, User, UserSerializer)


@api_view(['POST', ])
@permission_classes([AllowAny, ])
def login(request):
    """Generates a JWT for an user, given valid credentials."""
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
                'error':
                    'Can not authenticate with the given credentials, or the account has been deactivated'
            }
            return Response(payload, status=status.HTTP_403_FORBIDDEN)

    except User.DoesNotExist:
        payload = {'message': 'The user with the given credentials was not found'}
        return Response(payload, status=status.HTTP_404_NOT_FOUND)
    except KeyError:
        payload = {'error': 'Please provide an email and a password'}
        return Response(payload, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_from_exception('user.views.login', e)
