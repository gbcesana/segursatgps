from django.contrib.auth import logout
from django.shortcuts import redirect

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

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
            if request.user.profile.is_superadmin == False:
                logout(request)
                return redirect('login')
        elif re.search("^/web/api/management*", request.get_full_path()):
            if request.user.profile.is_superadmin == False:
                error = {
                    'detail':'Largate de aca'
                }
                response = Response(
                    error,
                    status=status.HTTP_403_FORBIDDEN
                )
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                return response

        return response