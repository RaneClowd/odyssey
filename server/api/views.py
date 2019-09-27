from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Trail
from .serializers import TrailSerializer

class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer

    permission_classes = [permissions.AllowAny]
