from django.contrib import admin

from content.models import *


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    empty_value_display = 'Informação não existente'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    empty_value_display = 'Informação não existente'


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    empty_value_display = 'Informação não existente'
