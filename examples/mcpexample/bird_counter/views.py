from django.shortcuts import render
from rest_framework.generics import UpdateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.serializers import ModelSerializer

from mcp_server import drf_publish_create_mcp_tool
from .models import Location

# Create your views here.

class LocationSerializer(ModelSerializer):
    """
    Serializer for the Location model.
    """
    class Meta:
        model = Location
        fields = ('id', 'name','description','city')



class LocationAPIView(CreateAPIView):
    """
    API view to retrieve, update or delete a Location instance.
    """
    serializer_class = LocationSerializer

class LocationAPIUpdateView(RetrieveUpdateDestroyAPIView):
    """
    API view to update / deslete a Location instance.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationAPIListView(ListAPIView):
    """
    API view to list all Location instances.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

