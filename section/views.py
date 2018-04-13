"""Enpoints para as seções."""
from rest_framework import viewsets

from section.models import Section
from section.serializers import SectionSerializer

class SectionView(viewsets.ReadOnlyModelViewSet):
    """Endpoint que possibilita visualizações das seções."""
    serializer_class = SectionSerializer

    def get_queryset(self):
        """Método para seções."""
        queryset = Section.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset
