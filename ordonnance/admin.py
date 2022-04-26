from django.contrib import admin
from ordonnance.models import Ordonnance
from med.models import Meds

class OrdonnanceAdmin(admin.ModelAdmin):
	list_display = ('nom_doc','nom_pat',"nom_traitement","id_medicament","le_type","quantite","description_de_traitement","nom_traitement","a_mutuelle")
	def nom_doc(self, x):
		return f"{x.id_visite.medcin_id.person_id.nom} {x.id_visite.medcin_id.person_id.prenom}"
	def nom_pat(self, x):
		return f"{x.id_visite.patient_id.person_id.nom} {x.id_visite.patient_id.person_id.prenom}"
	
class MedicamentAdmin(admin.ModelAdmin):
	pass
	# list_display = ('id','nom_doc','nom_pat','date_created')
	# def nom_doc(self, x):
	# 	return f"{x.medcin_id.person.nom} {x.medcin_id.person.prenom}"
	# def nom_pat(self, x):
	# 	return f"{x.patient_id.person.nom} {x.patient_id.person.prenom}"
admin.site.register(Ordonnance,  OrdonnanceAdmin)
admin.site.register(Meds, MedicamentAdmin)