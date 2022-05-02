from django.db import models
from django.conf import settings
from landing.models import Person

class Pharmacie(models.Model):
	person_id=models.OneToOneField(Person,on_delete=models.CASCADE)
	INP=models.IntegerField(primary_key=True)
	nom = models.CharField(max_length=30)
	ville = models.CharField(max_length=30)
	adresse=models.CharField(max_length=255)
	activated=models.BooleanField(default=False)
