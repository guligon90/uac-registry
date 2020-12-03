# Django imports
from django.shortcuts import render

# DRF imports
from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


# Project imports
from .models import Address
from .serializers import AddressSerializer
from common.exceptions import response_from_exception


def get_user_main_address(user_pk):
    return Address.objects.filter(users__id=user_pk).first()


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def list_addresses(request, user_pk=None):
    """
    List all addresses.
    """
    try:
        if request.method == 'GET':
            addresses = Address.objects.all()
            serializer = AddressSerializer(addresses, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = AddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_from_exception('address.views.list_address', e)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_address(request, user_pk=None):
    """
    Create a new address.
    """
    try:
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_from_exception('address.views.create_address', e)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated,])
def address_detail(request, pk, user_pk=None):
    """
    Retrieve, update or delete a address.
    """
    try:
        try:
            address = Address.objects.get(pk=pk)
            # If an address is being filtered from the user API
            if user_pk:
                address = Address.objects.filter(id=pk, users__id=user_pk).first()
        except Address.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = AddressSerializer(address)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            serializer = AddressSerializer(address, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            address.delete()
            payload = {'message': 'Address removed successfully.'}
            return Response(payload, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_from_exception('address.views.address_detail', e)


class UserAddressDetailAPIViewSet(ViewSet):
    """View set for the users' address API,
    e.g., /users/{user_pk}/address/{address_pk}"""

    def destroy(self, request, pk, user_pk):
        """Removes an user's address."""
        return address_detail(request, pk, user_pk)
    
    def partial_update(self, request, pk, user_pk):
        """Updates the user's address information."""
        return address_detail(request, address_pk, user_pk)

    def retrieve(self, request, pk, user_pk):
        """Gets information about a user's address."""
        from pprint import pprint
        pprint(request)
        return address_detail(request, pk, user_pk)


class UserAddressAPIViewSet(ViewSet):
    """View set for the users' addresses API,
    e.g., /users/{user_pk}/addresses/"""

    def create(self, request, user_pk):
        """Creates one or more addresses for a user."""
        return create_address(request, user_pk)

    def list(self, request, user_pk):
        """Lists all the user's addresses."""
        return list_addresses(request, user_pk)
