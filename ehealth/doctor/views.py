from django.shortcuts import render
from patient.models import Patient
from ordonnance.models import Ordonnance
from doctor.models import Visite
from django.core import serializers
from django.views.decorators.http import require_POST
@require_POST
def get_meds_history(request):
	params=request.post
	patient=params["patient"]
	visites = Visite.objects.filter(patient_id=patient)
	privacy = Patient.get(pk=patient).permission_privacy
	data={"error":"you're not allowed"}
	if privacy==False:
		return HttpResponse(data, mimetype='application/json')
	meds=[]
	for visite in visites:
		x=Ordonnance.objects.filter(id_visite=visite.id,le_type="Medicaments")
		meds.append(x)
	data=serializers.serialize("json",meds)
	return HttpResponse(data, mimetype='application/json')

@require_POST
def get_visites_history(request):
	params=request.post
	patient=params["patient"]
	visites = Visite.objects.filter(patient_id=patient)
	privacy = Patient.get(pk=patient).permission_privacy
	data={"error":"you're not allowed"}
	if privacy==False:
		return HttpResponse(data, mimetype='application/json')
	
	data=serializers.serialize("json",visites)
	return HttpResponse(data, mimetype='application/json')
@require_POST
def ecrire_ordonnance(request):
	pass

