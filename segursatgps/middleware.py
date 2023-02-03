from django.contrib.auth import logout
from django.shortcuts import redirect

import re

class ManagementForbiddenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if re.search("^/management*", request.get_full_path()):
            if response.status_code == 403:
                logout(request)
                return redirect('login')

        return response