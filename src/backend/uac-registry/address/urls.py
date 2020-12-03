# Django imports
from django.urls import path

# Project imports
from address import views


urlpatterns = [
    path('', views.list_addresses),
    path('create/', views.create_address),
    path('<int:pk>', views.address_detail),
]
