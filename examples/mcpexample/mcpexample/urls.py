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
from django.contrib import admin
from django.urls import path, include
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from mcp_server.views import MCPServerStreamableHttpView
from bird_counter.mcp import second_mcp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('mcp_server.urls')),
    path("mcpunsecured", MCPServerStreamableHttpView.as_view()),
    path("altmcp", MCPServerStreamableHttpView.as_view(mcp_server=second_mcp))
]
