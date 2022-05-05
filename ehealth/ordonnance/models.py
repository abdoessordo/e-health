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
	id_medicament=models.ForeignKey(Meds,null=True,blank=True,on_delete=models.CASCADE)
	description_de_traitement=models.CharField(max_length=255)
	id_pharmacie=models.ForeignKey(Pharmacie,on_delete=models.CASCADE,null=True,blank=True)
	quantite=models.IntegerField(null=True,blank=True)
	price=models.IntegerField(null=True,blank=True)
	a_mutuelle=models.BooleanField(default=False)
	nom_traitement=models.CharField(max_length=255,null=True,blank=True)
	date_purchase=models.DateTimeField(null=True,blank=True)
	date_created=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=["-date_created"]
	def save(self,*args, **kwargs):
		if self.le_type=="Medicaments":
			self.price=self.quantite*self.id_medicament.prix_br


		super(Ordonnance, self).save(*args, **kwargs)

