from django.db import models


class Feature(models.Model):
    """
    Model responsável por abstrair os serviços oferecidos pela fábrica.
    """
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    icon_class = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Classe do ícone'
    )
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Título'
    )
    description = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Descrição'
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    """
    Model responsável por abstrair os projeto realizados pela fábrica.
    """
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    STATUS_CHOICES = (
        ('A', 'Em andamento'),
        ('F', 'Finalizado'),
    )
    title = models.CharField(
        max_length=20,
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
    logo = models.ImageField(
        upload_to='img/portifolio/',
        null=False,
        verbose_name='Logo do Projeto'
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        null=False,
        blank=False,
        default='A',
        max_length=1,
        verbose_name='Status'
    )

    def __str__(self):
        return self.title


class Members(models.Model):
    """
    Model responsável por abstrair as informações dos membros da fábrica.

    """
    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'

    is_active = models.BooleanField(
        default=True,
        verbose_name='Ativo?'
    )
    photo = models.ImageField(
        upload_to='img/members/',
        null=False,
        verbose_name='Foto'
    )
    name = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        verbose_name='Nome'
    )
    profession = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        verbose_name='Profissão'
    )
    github = models.URLField(blank=True, verbose_name='Github')
    instagram = models.URLField(blank=True, verbose_name='Instagram')
    linkedin = models.URLField(blank=True, verbose_name='LinkedIn')

    @property
    def verbose_active(self):
        if self.is_active:
            return 'Ativo'
        return 'Inativo'

    def __str__(self):
        return '{} - {} ({})'.format(self.name, self.profession, self.verbose_active)
