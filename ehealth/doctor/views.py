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
	nom=params["nom"]
	prenom=params["prenom"]
	ville=params["ville"]
	age=params["age"]
	sexe=params["sexe"]
	obj=Doctor.objects.create(nom=nom,prenom=prenom,ville=ville,age=age,sexe=sexe)
	obj.save()
	data={"Done":"doctor created"}
	return  JsonResponse(data)
@require_POST
@csrf_exempt
def create_visite(request):
	"""
	date_created=models.DateField(auto_now_add=True)
	patient_id=models.OneToOneField(Doctor,on_delete=models.CASCADE)
	medcin_id=models.OneToOneField(Patient,on_delete=models.CASCADE)"""
	params=request.POST
	patient=params["patient"]
	medcin=params["medcin"]
	patient=Patient.objects.get(pk=patient)
	medcin=Doctor.objects.get(pk=medcin)
	obj=Visite.objects.create(patient_id=patient,medcin_id=medcin)
	obj.save()
	data={"Done":"Visite created"}
	return  JsonResponse(data)
@require_POST
@csrf_exempt
def get_meds_history(request):
	params=request.POST
	patient=params["patient"]
	visites = Visite.objects.filter(patient_id=patient).values("id")
	privacy = Patient.objects.get(pk=patient,activated=True).permission_privacy
	data={"error":"you're not allowed"}
	if privacy==False:
		return JsonResponse(data)
	meds=Ordonnance.objects.filter(id_visite__in=visites,le_type="Medicaments").values()
	# res={}
	# i=0
	# for med in meds:
	# # 	x=Ordonnance.objects.filter(id_visite=visite.id,le_type="Medicaments")
	#  	res[f"{i}"]=med
	#  	i+=1
	return JsonResponse({"result":list(meds)})

@require_POST
@csrf_exempt
def get_visites_history(request):
	params=request.POST
	patient=params["patient"]
	visites = Visite.objects.filter(patient_id=patient).values()
	privacy = Patient.objects.get(pk=patient).permission_privacy
	data={"error":"you're not allowed"}
	if privacy==False:
		return HttpResponse(data, mimetype='application/json')
	
	return JsonResponse({"result":list(visites)})
@require_POST
def ecrire_ordonnance(request):
	pass

