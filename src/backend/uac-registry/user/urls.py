# Django imports
from django.urls import path

# Project imports
from user import views


urlpatterns = [
    path('', views.list_users),
    path('create/', views.create_user),
    path('<int:pk>', views.user_detail),
    path('login/', views.login),
]
