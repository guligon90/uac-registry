# Django imports
from django.urls import path

# Project imports
from user_address.views import UserAddressAPIViewSet, UserAddressDetailAPIViewSet


urlpatterns = [
    path(
        '<int:user_id>/address/<int:address_id>',
        UserAddressDetailAPIViewSet.as_view({
            'delete': 'destroy',
            'patch': 'partial_update',
            'get': 'retrieve',
        }),
        name='user_address_detail'
    ),
    path(
        '<int:user_id>/address/',
        UserAddressAPIViewSet.as_view({
            'post': 'create',
            'get': 'list',
        }),
        name='user_address_create_list'
    ),
]
