"""Serializers para as models do app sections."""
from rest_framework import serializers

from section.models import Section, Subsection


class SubSectionSerializer(serializers.ModelSerializer):
    """Serializers para as subseções de uma seção."""
    class Meta:
        """Class Meta padrão."""
        model = Subsection
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    """Serializer para os seções."""
    sub_sections = SubSectionSerializer(many=True)

    class Meta:
        """Class Meta padrão."""
        model = Section
        fields = '__all__'
