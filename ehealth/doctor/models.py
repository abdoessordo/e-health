from django.db import models
from patient.models import Patient
from landing.models import Person


class Doctor(models.Model):
	person_id=models.OneToOneField(Person,on_delete=models.CASCADE)
	ville = models.CharField(max_length=250)
	INP=models.IntegerField(primary_key=True)
	created=models.DateField(auto_now_add=True)
	activated=models.BooleanField(default=0)
class Visite(models.Model):
	date_created=models.DateField(auto_now_add=True)
	patient_id=models.OneToOneField(Patient,on_delete=models.CASCADE)
	medcin_id=models.OneToOneField(Doctor,on_delete=models.CASCADE)
