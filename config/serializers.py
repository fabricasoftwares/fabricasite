"""Serializers para as models do app content."""
from rest_framework import serializers

from config.models import Factory


class FactorySerializer(serializers.ModelSerializer):
    """Serializer para os serviços."""
    class Meta:
        """Class Meta padrão."""
        model = Factory
        fields = '__all__'
