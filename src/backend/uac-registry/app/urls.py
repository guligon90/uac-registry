"""UAC Registry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# Django imports
from django.conf.urls import url, include
from django.contrib import admin

# DRF Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# DRF imports
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
   openapi.Info(
      title="UAC Registry API",
      default_version='v1',
      description="A REST API, built with Django, which provides CRUD operations for addresses, clients and users.",
      contact=openapi.Contact(email="guligon90@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(('user.urls', 'users'), namespace='users')),
    url(r'^clients/', include(('client.urls', 'clients'), namespace='clients')),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
