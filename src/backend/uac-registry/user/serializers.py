# Django imports
from rest_framework.serializers import ModelSerializer, ReadOnlyField

# Project imports
from .models import User


class UserSerializer(ModelSerializer):

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
