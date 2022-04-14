from django.shortcuts import render,get_object_or_404,redirect
from patient.models import Patient
from ordonnance.models import Ordonnance
from doctor.models import Visite,Doctor
from django.core import serializers
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
def register(request):
	if request.method=="POST":
		params=request.POST
		INP=params["INP"]
		ville=params["ville"]
		obj=Doctor.objects.update_or_create(
			person_id=request.user.person,
			defaults={"ville":ville,"INP":INP})
		
		
		return  redirect("doctor:visites")
	else:
		return render(request,"doctor/edit.html",{})

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
	visites = Visite.objects.filter(patient_id=patient)
	privacy = Patient.objects.get(pk=patient).permission_privacy
	data={"error":"you're not allowed"}
	if privacy==False:
		return HttpResponse(data, mimetype='application/json')
	
	return render(request,"visites.html",{"result":visites})


def get_doc_visites_history(request):
	doctor=request.user.person.doctor
	if doctor.activated:
		visites = Visite.objects.filter( medcin_id=doctor.INP)
		return render(request,"doctor/visites.html",{"data":visites})
	else:
		return render(request,"ehealth/error.html")
def get_visite_details(request,visite):
	visite=get_object_or_404( Visite,pk=visite)
	privacy=visite.patient_id.permission_privacy
	modifiable=True
	
	condition=int(request.user.person.doctor.INP)!=visite.medcin_id
	if condition:
		modifiable=False
	if modifiable ==False and privacy==0:
		return HttpResponse({"error":"you're not allowed"}, mimetype='application/json')

	return render(request,"doctor/visite_details.html",{
				"modifiable":modifiable,
				"visite":visite,
				"doctor":True
		})