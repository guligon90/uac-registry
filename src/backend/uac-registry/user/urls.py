# Django imports
from django.conf.urls import url

# Project imports
from .views import UserLoginAPIView, CreateUserAPIView, UserRetrieveUpdateAPIView


urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^login/$', UserLoginAPIView.as_view()),
]
