from django.contrib import admin

from config.models import *

@admin.register(Factory)
class SectionAdmin(admin.ModelAdmin):
    empty_value_display = 'Informação não existente'
    
