from django.core.management.base import BaseCommand
from asgiref.sync import async_to_sync
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def _check_client():
    server_params = StdioServerParameters(
        command="python",
        args=[
            "manage.py",
            "stdio_server"
        ]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("Tools discovered in server:")
            tool_list = await session.list_tools()
            for tool in tool_list.tools:
                print(f'\n\t{tool.name}: {tool.description}')
                print(f'\tParameters: {tool.inputSchema}')

            print("Resources discovered in server:")
            resource_list = await session.list_resources()
            for resource in resource_list.resources:
                print(f'\n\t{resource.name}: {resource.description}')

            print("Prompts discovered in server:")
            prompt_list = await session.list_prompts()
            for prompt in prompt_list.prompts:
                print(f'\n\t{prompt.name}: {prompt.description}')


_check_client_sync = async_to_sync(_check_client)


class Command(BaseCommand):
    help = 'Inspect installed tools, resources and prompts'

    def handle(self, *args, **options):
        _check_client_sync()
