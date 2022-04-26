from django.contrib import admin
from doctor.models import Doctor,Visite
class DoctorAdmin(admin.ModelAdmin):
	list_display = ('INP','nom','prenom')
	def nom(self, x):
		return x.person_id.nom
	def prenom(self, x):
		return x.person_id.prenom
class VisiteAdmin(admin.ModelAdmin):
	list_display = ('id','nom_doc','nom_pat','date_created')
	def nom_doc(self, x):
		return f"{x.medcin_id.person_id.nom} {x.medcin_id.person_id.prenom}"
	def nom_pat(self, x):
		return f"{x.patient_id.person_id.nom} {x.patient_id.person_id.prenom}"
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Visite, VisiteAdmin)