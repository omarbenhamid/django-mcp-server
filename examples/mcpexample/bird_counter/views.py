from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

from .models import Location


# Create your views here.

class LocationSerializer(ModelSerializer):
    """
    Serializer for the Location model.
    """

    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'city')


class LocationAPIView(CreateAPIView):
    """
    API view to retrieve, update or delete a Location instance.
    """
    serializer_class = LocationSerializer


class LocationAPIUpdateView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve / update / delete a Location instance.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationAPIUpdateViewSet(GenericViewSet, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    """
    API viewset to retrieve / update / delete a Location instance.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationAPIListView(ListAPIView):
    """
    API view to list all Location instances.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationAPIListViewSet(GenericViewSet, ListModelMixin):
    """
    API view set to list all Location instances.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
