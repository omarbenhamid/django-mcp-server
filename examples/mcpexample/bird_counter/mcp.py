from rest_framework.serializers import ModelSerializer

from mcp_server import MCPToolset, drf_serialize_output, drf_publish_create_mcp_tool, drf_publish_update_mcp_tool, \
    drf_publish_destroy_mcp_tool, drf_publish_list_mcp_tool
from mcp_server import QueryToolModel
from .models import Bird, Location, City
from .serializers import BirdSerializer
from .views import LocationAPIView, LocationAPIUpdateView, LocationAPIListView


class BirdQuery(QueryToolModel):
    model = Bird

    def get_queryset(self):
        """self.request can be used to filter the queryset"""
        return super().get_queryset().filter(location__isnull=False)

class LocationTool(QueryToolModel):
    model = Location

class CityTool(QueryToolModel):
    model = City


class LocationQuery(QueryToolModel):
    model = Location


class CityQuery(QueryToolModel):
    model = City


class SpeciesCount(MCPToolset):
    def _search_birds(self, search_string: str | None = None) -> Bird:
        """Get the queryset for birds,
        methods starting with _ are not registered as tools"""
        return Bird.objects.all() if search_string is None else Bird.objects.filter(species__icontains=search_string)

    @drf_serialize_output(BirdSerializer)
    def increment_species(self, name: str, amount: int = 1):
        """
        Increment the count of a bird species by a specified amount and returns tehe new count.
        The first argument ios species name the second is the mouunt to increment with (1) by default.
        """
        ret = self._search_birds(name).first()
        if ret is None:
            ret = Bird.objects.create(species=name)

        ret.count += amount
        ret.save()

        return ret

# For more advanced low level usage, you can use the mcp_server directly
from mcp_server import mcp_server as mcp

@mcp.tool()
async def get_species_count(name : str):
    """ Find the ID of a bird species by its name or part of name. Returns the count"""
    ret = await Bird.objects.filter(species__icontains=name).afirst()
    if ret is None:
        ret = await Bird.objects.acreate(species=name)

    return ret.count


drf_publish_create_mcp_tool(LocationAPIView)

drf_publish_update_mcp_tool(LocationAPIUpdateView)

drf_publish_destroy_mcp_tool(LocationAPIUpdateView, instructions="A tool to delete a location")

drf_publish_list_mcp_tool(LocationAPIListView, instructions="A tool to list all locations")
