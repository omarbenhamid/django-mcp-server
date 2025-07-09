"""
URL configuration for mcpexample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.utils.module_loading import import_string
from rest_framework.permissions import IsAuthenticated

from mcp_server.views import MCPServerStreamableHttpView


# Register MCP Server View and bypass default DRF default permission / authentication classes
base_url = getattr(settings, "DJANGO_MCP_ENDPOINT", "mcp")

urlpatterns = [
    path(base_url, MCPServerStreamableHttpView.as_view(
        permission_classes=[IsAuthenticated] if getattr(settings, 'DJANGO_MCP_AUTHENTICATION_CLASSES', None) else [],
        authentication_classes=[import_string(cls) for cls in getattr(settings, 'DJANGO_MCP_AUTHENTICATION_CLASSES', [])]
    ), name="mcp_server_streamable_http_endpoint"),
]
