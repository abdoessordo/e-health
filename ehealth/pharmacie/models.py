from django.db import models

class Pharmacie(models.Model):
	nom = models.CharField(max_length=30)
	ville = models.CharField(max_length=30)
	adresse=models.CharField(max_length=255)
	activated=models.BooleanField(null=False)