# Django imports
from django.shortcuts import render

# DRF imports
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Project imports
from .models import Client
from .serializers import ClientSerializer
from common.exceptions import response_from_exception


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def list_clients(request):
    """
    List all clients.
    """
    try:
        if request.method == 'GET':
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_from_exception('client.views.list_clients', e)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_client(request):
    """
    Create a new client.
    """
    try:
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return response_from_exception('client.views.create_client', e)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated,])
def client_detail(request, pk):
    """
    Retrieve, update or delete a client.
    """
    try:
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ClientSerializer(client)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            serializer = ClientSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            client.delete()
            payload = {'message': 'Client removed successfully.'}
            return Response(payload, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_from_exception('client.views.client_detail', e)
