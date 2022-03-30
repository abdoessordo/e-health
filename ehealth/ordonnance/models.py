from django.db import models
from pharmacie.models import Pharmacie
from doctor.models import Visite
# Create your models here.
class Medicament(models.Model):
	pass
class Ordonnance(models.Model):
	id_visite=models.ForeignKey(Visite, on_delete=models.CASCADE)
	class typee(models.TextChoices):
		Traitement = 'Traitement'
		Medicaments = 'Medicaments'
	le_type=models.CharField(max_length=13,choices=typee.choices)
	id_medicament=models.OneToOneField(Medicament,on_delete=models.CASCADE,)
	duree_de_traitement=models.IntegerField()
	description_de_traitement=models.CharField(max_length=255)
	id_pharmacie=models.OneToOneField(Pharmacie,on_delete=models.CASCADE)
	price=models.IntegerField()
	a_mutuelle=models.BooleanField()
