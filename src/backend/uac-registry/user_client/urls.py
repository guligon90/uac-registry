# Django imports
from django.urls import path

# Project imports
from user_client.views import UserClientAPIViewSet


urlpatterns = [
    path(
        '<int:user_id>/client/',
        UserClientAPIViewSet.as_view({
            'post': 'create',
            'get': 'retrieve',
            'patch': 'partial_update',
        }),
        name='user_client_retrieve_update'
    )
]
