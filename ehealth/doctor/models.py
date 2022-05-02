from django.db import models
from patient.models import Patient
from landing.models import Person


class Doctor(models.Model):
	person_id=models.OneToOneField(Person,on_delete=models.CASCADE)
	ville = models.CharField(max_length=250)
	INP=models.IntegerField(primary_key=True)
	speciality=models.CharField(max_length=255)
	created=models.DateField(auto_now_add=True)
	activated=models.BooleanField(default=0)
class Visite(models.Model):
	date_created=models.DateTimeField(auto_now_add=True)
	patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="visites")
	medcin_id=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="visites")
class Appointement(models.Model):
	class time(models.TextChoices):
		Matin = "09h - 12h"
		Midi = "12h - 14h"
		apres = "14h - 17h"
	class status_choices(models.TextChoices):
		accepted = "1"
		waiting = "2"
		refused = "3"
	patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="appointements")
	medcin_id=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="appointements")
	date=models.DateField()
	heure=models.CharField(max_length=255,choices=time.choices)
	status=models.CharField(max_length=1,choices=status_choices.choices)