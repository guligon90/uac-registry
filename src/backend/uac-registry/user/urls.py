# Django imports
from django.urls import path

# DRF imports
from rest_framework.urlpatterns import format_suffix_patterns

# Project imports
from user import views


urlpatterns = [
    path('list/', views.list_users),
    path('create/', views.create_user),
    path('detail/<int:pk>', views.user_detail),
    path('login/', views.login)
]