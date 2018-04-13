"""Serializers para as models do app content."""
from rest_framework import serializers

from content.models import Feature, Project, Members


class FeatureSerializer(serializers.ModelSerializer):
    """Serializer para os serviços."""
    class Meta:
        """Class Meta padrão."""
        model = Feature
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer para os projetos."""
    class Meta:
        """Class Meta padrão."""
        model = Project
        fields = '__all__'


class MembersSerializer(serializers.ModelSerializer):
    """Serializer para os integrantes."""
    class Meta:
        """Class Meta padrão."""
        model = Members
        fields = '__all__'
