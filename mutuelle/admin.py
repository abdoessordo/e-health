from pyexpat import model
from django.contrib import admin
from . import models


@admin.register(models.AllMutuelle)
class AllMutuelleAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at',
                    'patient_id', 'visite_id', 'mutuelle_status']
