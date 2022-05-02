from django.contrib import admin
from pharmacie.models import Pharmacie

class PharmacieAdmin(admin.ModelAdmin):
    list_display = ("INP",'nom',"ville","activated")
    
admin.site.register(Pharmacie, PharmacieAdmin)
