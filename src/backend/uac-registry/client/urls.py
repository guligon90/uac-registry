# Django imports
from django.urls import path

# Project imports
from client import views


urlpatterns = [
    path('', views.list_clients),
    path('create/', views.create_client),
    path('<int:pk>', views.client_detail),
]
