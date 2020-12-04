# Django imports
from rest_framework import serializers

# Project imports
from address.serializers import AddressSerializer
from user.serializers import UserSerializer
from .models import UserAddress


class UserAddressSerializer(serializers.ModelSerializer):
    address_id = serializers.PrimaryKeyRelatedField(write_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True)

    address = AddressSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserAddress
        fields = (
            'id',
            'is_main_address',
            'address',
            'user',
        )
