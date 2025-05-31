from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession


async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://localhost:8000/mcpunsecured") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # Call a tool
            tool_result = await session.call_tool("list_species", {"search_string": "e"})
            print(tool_result)
            tool_result = await session.call_tool("list_species", {"search_string": "e"})
            print(tool_result)
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())