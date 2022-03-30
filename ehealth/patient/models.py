from django.db import models

class Patient(models.Model):
	class Gender(models.TextChoices):
		Male = 'M'
		Female = 'F'
	card_id=models.IntegerField()
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	datedenaissance=models.DateField()
	created=models.DateField(auto_now_add=True)
	ville = models.CharField(max_length=30)
	age = models.IntegerField()
	sexe=models.CharField(max_length=1,choices=Gender.choices)
	permission_privacy=models.BooleanField()
	a_mutuelle=models.BooleanField()
	immatriculation=models.IntegerField()
	activated=models.BooleanField(null=False)
 