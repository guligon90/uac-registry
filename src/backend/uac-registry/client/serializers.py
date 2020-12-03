# Django imports
from rest_framework.serializers import ModelSerializer
from .models import Client


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
        )
