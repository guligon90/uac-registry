# DRF imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

# Project imports
from common.exceptions import response_from_exception
from common.views import crud
from client.serializers import ClientSerializer
from client.models import Client
from user.models import User


# Create your views here.
class UserClientAPIViewSet(ViewSet):
    """View set for the client API endpoints associated
    to a user, i.e., excluding the listing and deleting
    endpoints, i.e., /user/{user_id}/client/"""

    permission_classes = [IsAuthenticated, ]

    @classmethod
    def build_context(cls, method):
        return f'{__name__}.{cls.__name__}.{method}'

    @classmethod
    def perform_crud_operation(cls, request, user_id):
        user = crud.get_instance_from_db(user_id, User)
        if user:
            client_id = user.client.id
            return crud.instance_detail(request, client_id, Client, ClientSerializer)

        payload = {'error': f'User with ID {user_id} not found.'}
        return Response(payload, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, user_id):
        """Retrieves the client associated to the user."""
        try:
            return UserClientAPIViewSet.perform_crud_operation(request, user_id)
        except Exception as e:
            return response_from_exception(UserClientAPIViewSet.build_context('retrieve'), e)

    def partial_update(self, request, user_id):
        """Updates the user's client instance."""
        try:
            return UserClientAPIViewSet.perform_crud_operation(request, user_id)
        except Exception as e:
            return response_from_exception(UserClientAPIViewSet.build_context('partial_update'), e)

    def create(self, request, user_id):
        """Creates a client for that user."""
        try:
            return UserClientAPIViewSet.perform_crud_operation(request, user_id)
        except Exception as e:
            return response_from_exception(UserClientAPIViewSet.build_context('create'), e)
