from django.db import models
from pharmacie.models import Pharmacie
from doctor.models import Visite
from med.models import Meds
# Create your models here.

class Ordonnance(models.Model):
	id_visite=models.ForeignKey(Visite, on_delete=models.CASCADE,related_name="ordonnance")
	class typee(models.TextChoices):
		Traitement = 'Traitement'
		Medicaments = 'Medicaments'
	le_type=models.CharField(max_length=13,choices=typee.choices)
	id_medicament=models.ManyToManyField(Meds,blank=True)
	description_de_traitement=models.CharField(max_length=255)
	id_pharmacie=models.ForeignKey(Pharmacie,on_delete=models.CASCADE,null=True,blank=True)
	quantite=models.IntegerField(null=True,blank=True)
	price=models.IntegerField(null=True,blank=True)
	a_mutuelle=models.BooleanField(default=False)
	nom_traitement=models.CharField(max_length=255,null=True,blank=True)
	date_purchase=models.DateTimeField(auto_now_add=True)

