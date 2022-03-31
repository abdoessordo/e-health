from django.shortcuts import render
from patient.models import Patient
from ordonnance.models import Ordonnance
from doctor.models import Visite,Doctor
from django.core import serializers
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
@require_POST
@csrf_exempt
def register(request):
	
	params=request.POST
	card_id=params['card_id']
	nom=params["nom"]
	prenom=params["prenom"]
	datedenaissance=params["datedenaissance"]
	ville=params["ville"]
	sexe=params["sexe"]
	a_mutuelle=params["a_mutuelle"]
	immatriculation=params["immatriculation"]
	obj=Patient.objects.create(card_id=card_id,nom=nom,prenom=prenom,ville=ville,datedenaissance=datedenaissance,sexe=sexe,a_mutuelle=a_mutuelle,immatriculation=immatriculation)
	obj.save()
	data={"Done":"Patient created"}
	return  JsonResponse(data)
