from django.db import models


class Section(models.Model):
    """
    Model que abstrai de forma genérica todas as seções textuais do site.
    """
    class Meta:
        verbose_name = 'Seção'
        verbose_name_plural = 'Seções'
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Título'
    )
    description = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='Descrição'
    )
    photo = models.ImageField(
        upload_to='img/sections/',
        null=False,
        verbose_name='Foto'
    )

    def __str__(self):
        return self.title


class Subsection(models.Model):
    """
    Model responsável por abstrair as subseções da seção.
    """
    class Meta:
        verbose_name = 'Subseção'
        verbose_name_plural = 'Subseções'
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Título'
    )
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Descrição'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        verbose_name='Seção'
    )

    def __str__(self):
        return self.title
