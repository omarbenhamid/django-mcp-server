def bird_counter_request_hook(mcp_request, drf_request):
    mcp_request.original_request = drf_request
