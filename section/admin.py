from django.contrib import admin

from section.models import *


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    empty_value_display = 'Informação não existente'


@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    empty_value_display = 'Informação não existente'
