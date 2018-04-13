"""Enpoints para o conteúdo."""
from rest_framework import viewsets

from content.models import Feature, Members, Project
from content.serializers import (FeatureSerializer,
        ProjectSerializer, MembersSerializer)

class FeatureView(viewsets.ReadOnlyModelViewSet):
    """Endpoint que possibilita visualizações dos serviços."""
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class ProjectView(viewsets.ReadOnlyModelViewSet):
    """Endpoint que possibilita visualizações dos projetos."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MembersView(viewsets.ReadOnlyModelViewSet):
    """Endpoint que possibilita visualizações de membros."""
    serializer_class = MembersSerializer

    def get_queryset(self):
        """Método para filtrar membros."""
        queryset = Members.objects.all()
        active = self.request.query_params.get('active', None)
        if active is not None:
            queryset = queryset.filter(is_active=active)
        return queryset
