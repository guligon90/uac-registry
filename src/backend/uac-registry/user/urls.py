# Django imports
from django.urls import path, include

# DRF imports
from rest_framework.urlpatterns import format_suffix_patterns

# Project imports
from user import views
from address.views import UserAddressAPIViewSet, UserAddressDetailAPIViewSet
from client.views import ClientUserAPIViewSet



urlpatterns = [
    path('', views.list_users),
    path('create/', views.create_user),
    path('<int:pk>', views.user_detail),
    path(
        '<int:user_pk>/address/<int:address_pk>',
        UserAddressDetailAPIViewSet.as_view({
            'delete': 'destroy',
            'patch': 'partial_update',            
            'get': 'retrieve',
        }),
        name='user_address'
    ),
    path('login/', views.login),
    path(
        '<int:user_pk>/addresses/',
        UserAddressAPIViewSet.as_view({      
            'post': 'create',
            'get': 'list',
        }),
        name='user_addresses'
    ),
    path(
        '<int:user_pk>/client/<int:client_pk>',
        ClientUserAPIViewSet.as_view({
            'post': 'create',
            'get': 'retrieve',
            'patch': 'partial_update',
        }),
        name='user_client'
    )
]
