from rest_framework.response import Response
from rest_framework.views import APIView

from content.services import homepage_payload


class HomepageView(APIView):
    """Public homepage content. Nothing rendered by Next.js is stored here as code."""

    def get(self, request):
        return Response(homepage_payload(request))
