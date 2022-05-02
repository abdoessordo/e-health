from django.contrib import admin
from ordonnance.models import Ordonnance
from med.models import Meds

class OrdonnanceAdmin(admin.ModelAdmin):
	list_display = ('nom_doc','nom_pat',"nom_traitement","le_type","quantite","description_de_traitement","nom_traitement","a_mutuelle")
	def nom_doc(self, x):
		return f"{x.id_visite.medcin_id.person_id.nom} {x.id_visite.medcin_id.person_id.prenom}"
	def nom_pat(self, x):
		return f"{x.id_visite.patient_id.person_id.nom} {x.id_visite.patient_id.person_id.prenom}"
	def nom_medicament(self, x):
				return f"{x.id_medicament.nom} "

class MedicamentAdmin(admin.ModelAdmin):
	
	list_display = ('nom',)
	# def nom_doc(self, x):
	# 	return f"{x.medcin_id.person.nom} {x.medcin_id.person.prenom}"
	# def nom_pat(self, x):
	# 	return f"{x.patient_id.person.nom} {x.patient_id.person.prenom}"
admin.site.register(Ordonnance,  OrdonnanceAdmin)
admin.site.register(Meds, MedicamentAdmin)