# DRF imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Project imports
from common.views import crud
from .models import Client
from .serializers import ClientSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def list_clients(request):
    return crud.list_instances(request, ClientSerializer, Client)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_client(request):
    return crud.create_instance(request, ClientSerializer)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def client_detail(request, pk):
    return crud.instance_detail(request, pk, Client, ClientSerializer)
