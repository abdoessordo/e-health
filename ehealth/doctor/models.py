from django.db import models
from patient.models import Patient
class Doctor(models.Model):
	class Gender(models.TextChoices):
		Male = 'M'
		Female = 'F'
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	ville = models.CharField(max_length=250)
	age = models.IntegerField()
	sexe=models.CharField(max_length=1,choices=Gender.choices)
	activated=models.BooleanField(null=False)
class Visite(models.Model):
	date_created=models.DateField(auto_now_add=True)
	ville = models.CharField(max_length=250)
	adresse=models.CharField(max_length=255)
	patient_id=models.OneToOneField(Doctor,on_delete=models.CASCADE)
	medcin_id=models.OneToOneField(Patient,on_delete=models.CASCADE)
