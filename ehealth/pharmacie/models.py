from django.db import models
from django.conf import settings

class Pharmacie(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	img=models.ImageField(upload_to="profile_pics", max_length=100,null=True)

	nom = models.CharField(max_length=30)
	ville = models.CharField(max_length=30)
	adresse=models.CharField(max_length=255)
	activated=models.BooleanField(null=False)
