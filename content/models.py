from django.db import models


class Feature(models.Model):
    """
    Model responsável por abstrair os serviços oferecidos pela fábrica.
    """
    icon_class = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)


class Project(models.Model):
    """
    Model responsável por abstrair os projeto realizados pela fábrica.
    """
    STATUS_CHOICES = (
        ('A', 'Em andamento'),
        ('F', 'Finalizado'),
    )
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=150, null=False, blank=False)
    logo = models.ImageField(upload_to='img/portifolio/', null=False)
    status = models.CharField(
        choices=STATUS_CHOICES,
        null=False,
        blank=False,
        default='A',
        max_length=1,
    )


class Members(models.Model):
    """
    Model responsável por abstrair as informações dos membros da fábrica.

    """
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='img/members/', null=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    profession = models.CharField(max_length=35, null=False, blank=False)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)






