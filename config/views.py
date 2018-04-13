"""Enpoints para o conteúdo."""
from rest_framework import viewsets

from config.models import Factory
from config.serializers import FactorySerializer

class FactoryView(viewsets.ReadOnlyModelViewSet):
    """Endpoint que possibilita visualizações dos serviços."""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
