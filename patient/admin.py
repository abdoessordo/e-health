from django.contrib import admin
from patient.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('CIN','nom','prenom')
    def nom(self, x):
    	return x.person_id.nom
    def prenom(self, x):
    	return x.person_id.prenom
    def CIN(self, x):
    	return x.person_id.user.username
	
admin.site.register(Patient, PatientAdmin)
