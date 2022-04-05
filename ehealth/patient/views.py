from django.shortcuts import render,redirect
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
		a_mutuelle=params["a_mutuelle"]
		immatriculation=params["immatriculation"]
		permission_privacy=params["permission_privacy"]
		obj=Patient.objects.update_or_create(
			person_id=request.user.person,
			defaults={"a_mutuelle":a_mutuelle,"immatriculation":immatriculation,
			"permission_privacy":permission_privacy})
		
		return  redirect("patient:visites")
	else:
		return render(request,"patient/edit.html",{})
def get_patient_visites_history(request):
	visites = Visite.objects.filter( patient_id=request.user.person.patient.id)
	return render(request,"doctor/visites.html",{"data":visites})

def get_visite_details(request,visite):
	visite=get_object_or_404( Visite,pk=visite)
	return render(request,"doctor/visite_details.html",{
				"patient":True,
				"visite":visite,
		})
