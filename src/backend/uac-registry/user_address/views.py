# DRF imports
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Project imports
from address.serializers import AddressSerializer
from address.models import Address
from user.models import User
from common.exceptions import response_from_exception
from common.views import crud


class UserAddressDetailAPIViewSet(ViewSet):
    """View set for the users' address API,
    e.g., /users/{user_id}/address/{address_id}"""

    permission_classes = [IsAuthenticated, ]

    @classmethod
    def build_context(cls, method):
        return f'{__name__}.{cls.__name__}.{method}'

    @classmethod
    def perform_crud_operation(cls, request, address_id, user_id):
        user = crud.get_instance_from_db(user_id, User)
        if user:
            address = user.addresses.get(id=address_id)
            return crud.instance_detail(request, address.id, Address, AddressSerializer)

        payload = {'error': f'User with ID {user_id} not found.'}
        return Response(payload, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, address_id, user_id):
        """Removes an user's address."""
        try:
            return UserAddressDetailAPIViewSet.perform_crud_operation(request, address_id, user_id)
        except Exception as e:
            return response_from_exception(UserAddressDetailAPIViewSet.build_context('destroy'), e)

    def partial_update(self, request, address_id, user_id):
        """Updates the user's address information."""
        try:
            return UserAddressDetailAPIViewSet.perform_crud_operation(request, address_id, user_id)
        except Exception as e:
            return response_from_exception(UserAddressDetailAPIViewSet.build_context('partial_update'), e)

    def retrieve(self, request, address_id, user_id):
        """Gets information about a user's address."""
        try:
            return UserAddressDetailAPIViewSet.perform_crud_operation(request, address_id, user_id)
        except Exception as e:
            return response_from_exception(UserAddressDetailAPIViewSet.build_context('retrieve'), e)


# Create your views here.
class UserAddressAPIViewSet(ViewSet):
    """View set for the users' addresses API,
    e.g., /users/{user_id}/address/"""

    permission_classes = [IsAuthenticated, ]

    @classmethod
    def build_context(cls, method):
        return f'{__name__}.{cls.__name__}.{method}'

    def create(self, request, user_id):
        """Creates one or more addresses for a user."""
        try:
            user = crud.get_instance_from_db(user_id, User)

            if user:
                serializer = AddressSerializer(data=request.data)

                if serializer.is_valid():
                    address = serializer.save()
                    user.addresses.add(address)
                    user.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            payload = {'error': f'User with ID {user_id} not found.'}
            return Response(payload, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return response_from_exception(UserAddressAPIViewSet.build_context('create'), e)

    def list(self, request, user_id):
        """Lists all the user's addresses."""
        try:
            addresses = Address.objects.filter(user__id=user_id)
            serializer = AddressSerializer(addresses, many=True)

            return Response(serializer.data)
        except Exception as e:
            return response_from_exception(UserAddressAPIViewSet.build_context('list'), e)
