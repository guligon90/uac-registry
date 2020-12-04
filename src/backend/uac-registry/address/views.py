# DRF imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Project imports
from common.views import crud
from .models import Address
from .serializers import AddressSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def list_addresses(request):
    return crud.list_instances(request, AddressSerializer, Address)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def create_address(request):
    return crud.create_instance(request, AddressSerializer)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def address_detail(request, pk):
    return crud.instance_detail(request, pk, Address, AddressSerializer)
