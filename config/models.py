from django.db import models


class Factory(models.Model):
    """ 
    Classe responsável por abstrair as informações padrões da fábrica.
    """
    class Meta:
        verbose_name = 'Fábrica Configuração'
        verbose_name_plural = 'Fábrica Configurações'
    name = models.CharField(
        verbose_name='Nome',
        max_length=30, 
        null=False,
        blank=False
    )
    logo = models.ImageField(
        verbose_name='Logo'   ,  
        upload_to='img/logos/', 
        null=False
    )
    location = models.CharField(
        verbose_name='Localização',      
        max_length=40,
        null=False, 
        blank=False
    )
    email = models.EmailField(
        verbose_name='e-mail' ,       
        max_length=250,
        null=False,
        blank=False
    )
    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=20,
        null=False,
        blank=False
    )
    facebook = models.URLField(blank=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    

    def __str__(self):
        return '{}Configurações'.format(self.name) 