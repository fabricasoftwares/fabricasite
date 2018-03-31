from django.db import models


class Factory(models.Model):
    """ 
    Classe responsável por abstrair as informações padrões da fábrica.
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    logo = models.ImageField(upload_to='img/logos/', null=False)
    location = models.CharField(max_length= 40, null= False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    facebook = models.URLField(blank=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)