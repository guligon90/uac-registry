# Django imports
from rest_framework.serializers import ModelSerializer, ReadOnlyField

# Project imports
from address.serializers import AddressSerializer
from client.serializers import ClientSerializer
from user_address.models import UserAddress
from .models import User


class UserSerializer(ModelSerializer):
    addresses = AddressSerializer(read_only=True, many=True)
    client = ClientSerializer(read_only=True)
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

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        user_addresses = UserAddress.objects.filter(user__id=instance.id).distinct()

        if user_addresses is not None:
            serialized = AddressSerializer(data=user_addresses, many=True)
            ret.update({
                'addresses': serialized.data if serialized.is_valid() else [],
            })

        return ret
