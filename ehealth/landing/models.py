from django.db import models

from django.conf import settings
class Person(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	class Gender(models.TextChoices):
		Male = 'M'
		Female = 'F'
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	ville = models.CharField(max_length=250)
	datedenaissance = models.DateField()
	sexe=models.CharField(max_length=1,choices=Gender.choices)
