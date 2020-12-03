# Django imports
from django.urls import path

# DRF imports
from rest_framework.urlpatterns import format_suffix_patterns

# Project imports
from client import views


urlpatterns = [
    path('list/', views.list_clients),
    path('create/', views.create_client),
    path('detail/<int:pk>', views.client_detail),
]
