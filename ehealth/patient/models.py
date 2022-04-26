from django.db import models
from landing.models import Person

class Patient(models.Model):
	person_id=models.OneToOneField(Person,on_delete=models.CASCADE)
	class Gender(models.TextChoices):
		Male = 'M'
		Female = 'F'
	card_id=models.IntegerField(null=True,blank=True)
	permission_privacy=models.BooleanField(default=False)
	a_mutuelle=models.BooleanField(default=False)
	immatriculation=models.IntegerField(null=True)
	date_adhesion=models.DateField( null=True)
	n_affiliation=models.IntegerField(null=True)

 