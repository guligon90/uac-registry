# DRF imports
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Project imports
from common.exceptions import response_from_exception
from .models import Client
from .serializers import ClientSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def list_clients(request):
    """Lists all clients."""
    try:
        if request.method == 'GET':
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_from_exception('client.views.list_clients', e)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_client(request, user_pk=None):
    """Creates a new client."""
    try:
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_from_exception('client.views.create_client', e)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def client_detail(request, pk, user_pk=None):
    """Retrieves, update or delete a client."""
    try:
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ClientSerializer(client)
            return Response(serializer.data)

        if request.method == 'PATCH':
            serializer = ClientSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            client.delete()
            payload = {'message': 'Client removed successfully.'}
            return Response(payload, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_from_exception('client.views.client_detail', e)


class ClientUserAPIViewSet(ViewSet):
    """View set for the client API endpoints associated
    to a user, i.e., excluding the listing and deleting
    endpoints."""

    def create(self, request, user_pk):
        """Creates a client for that user."""
        return create_client(request, user_pk)

    def retrieve(self, request, pk, user_pk):
        """Retrieves the client associated to the user."""
        return client_detail(request, pk, user_pk)

    def partial_update(self, request, pk, user_pk):
        """Updates the user's client instance."""
        return client_detail(request, pk, user_pk)
