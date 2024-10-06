from rest_framework import viewsets, permissions

from . import serializers
from . import models


class SusumeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Susume class"""

    queryset = models.Susume.objects.all()
    serializer_class = serializers.SusumeSerializer
    permission_classes = [permissions.IsAuthenticated]


class SusupmtViewSet(viewsets.ModelViewSet):
    """ViewSet for the Susupmt class"""

    queryset = models.Susupmt.objects.all()
    serializer_class = serializers.SusupmtSerializer
    permission_classes = [permissions.IsAuthenticated]


class SusutypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Susutype class"""

    queryset = models.Susutype.objects.all()
    serializer_class = serializers.SusutypeSerializer
    permission_classes = [permissions.IsAuthenticated]