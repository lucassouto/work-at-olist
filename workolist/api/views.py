from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class HealthCheckViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        return Response({'message': 'healthy'}, status=status.HTTP_200_OK)
