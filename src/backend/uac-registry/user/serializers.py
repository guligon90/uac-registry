# Django imports
from rest_framework.serializers import ModelSerializer, ReadOnlyField

# Project imports
from address.serializers import AddressSerializer
from client.serializers import ClientSerializer
from .models import User


class UserSerializer(ModelSerializer):

    addresses = AddressSerializer(required=False, many=True)
    client = ClientSerializer(required=False)
    date_joined = ReadOnlyField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'password',
            'addresses',
            'client',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
