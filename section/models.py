from django.db import models


class Section(models.Model):
    """
    Model que abstrai de forma genérica todas as seções textuais do site.
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150, null=False, blank=False)
    photo = models.ImageField(upload_to='img/sections/', null=False)


class Subsection(models.Model):
    """
    Model responsável por abstrair as subseções da seção.
    """
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
