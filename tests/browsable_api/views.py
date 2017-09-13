from __future__ import unicode_literals

from rest_framework_tm import authentication, renderers
from rest_framework_tm.response import Response
from rest_framework_tm.views import APIView


class MockView(APIView):

    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = (renderers.BrowsableAPIRenderer,)

    def get(self, request):
        return Response({'a': 1, 'b': 2, 'c': 3})
