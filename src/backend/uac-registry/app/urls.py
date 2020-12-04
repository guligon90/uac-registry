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
    # Django Admin endpoints
    url(r'^admin/', admin.site.urls),
    # Address API endpoints
    url(r'^address/', include(('address.urls', 'addresses'), namespace='addresses')),
    # Swagger UI and text-mode endpoints (API documentation)
    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='docs-text-mode'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='docs-swagger-ui'),
    # Client API endpoints
    url(r'^client/', include(('client.urls', 'clients'), namespace='clients')),
    # User API endpoints
    url(r'^user/', include(('user.urls', 'users'), namespace='users')),
    url(r'^user/', include(('user_address.urls', 'user_addresses'), namespace='user_addresses')),
    url(r'^user/', include(('user_client.urls', 'user_client'), namespace='user_client')),
]
