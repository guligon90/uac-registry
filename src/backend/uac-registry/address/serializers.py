# Django imports
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Address


class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'id',
            'public_place',
            'name',
            'number',
            'additional_info',
            'district',
            'city',
            'state',
            'postal_code',
            'is_main_address',
        )