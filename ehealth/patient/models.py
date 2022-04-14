from django.db import models
from landing.models import Person


class Patient(models.Model):
	person_id=models.OneToOneField(Person,on_delete=models.CASCADE)
	class Gender(models.TextChoices):
		Male = 'M'
		Female = 'F'
	card_id=models.IntegerField(null=True)
	permission_privacy=models.BooleanField(default=0)
	a_mutuelle=models.BooleanField()
	immatriculation=models.IntegerField()
 