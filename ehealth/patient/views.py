from django.shortcuts import render,redirect, get_object_or_404
from patient.models import Patient
from ordonnance.models import Ordonnance
from doctor.models import Visite,Doctor
from django.core import serializers
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from landing.models import Person 
from django.contrib import messages
import datetime,logging


def register(request):
	if request.method=="POST":
		params=request.POST

		a_mutuelle= (1 if  params.get("a_mutuelle",0)=="on" else 0)
		immatriculation=(None if params.get("immatriculation")=="" else params.get("immatriculation"))
		permission_privacy=(1 if  params.get("privacy",0)=="on" else 0)
		affiliation=params["n_affiliation"]
		phone=params["phone"]
		Adress=params["Adress"]
		ville=params["ville"]
		date_adhesion=params["date_adhesion"]
		if (date_adhesion in ["" , "None"] or immatriculation in ["" , "None"] or affiliation in ["" , "None"]) :
			date_adhesion=None
			immatriculation=None
			affiliation=None
			a_mutuelle=0
		obj=Patient.objects.update_or_create(
			person_id=request.user.person,
			defaults={"a_mutuelle":a_mutuelle,"immatriculation":immatriculation,
			"permission_privacy":permission_privacy,"date_adhesion":date_adhesion,"n_affiliation":affiliation})
		obj=Person.objects.update_or_create(
			pk=request.user.person.pk,
			defaults={"phone":phone,"ville":ville,"adresse":Adress})
		messages.add_message(request, messages.ERROR,"Good job")
		return  redirect("patient:register")
	else:
		return render(request,"patient/edit.html",{"patient":True,"title":"Register","profile_settings":True})


def get_patient_visites_history(request):
	visites = Visite.objects.filter( patient_id=request.user.person.patient.id)


	return render(request, "doctor/visites.html", {"data":visites,"patient":True,'visite_seek':True,"title":"My Consultations"})


def get_visite_details(request,visite):
	visite=get_object_or_404( Visite,pk=visite)
	return render(request,"doctor/visite_details.html",{
				"patient":True,
				"visite":visite,
		})
def dashboard(request):
	nums=[]
	ordos=[]
	count=0
	visites = Visite.objects.filter( patient_id=request.user.person.patient.pk).order_by("-date_created")
	for v in visites:
		ordo = Ordonnance.objects.filter( id_visite=v.pk)
		if len(ordo)>0:
			count+=1
			ordos.append(ordo[0])
			nums.append(len(ordo))
			
		if count >=3:break
	ordon_num=len(Ordonnance.objects.filter(id_visite__in=visites.values("pk")))
	logging.warning(ordos)
	return render(request,"patient/dashboard.html",{"dashboard":True,"patient":True,"visites":visites,"title":"Dashoard","ordo":ordos,'nums':nums,"ordon_num":ordon_num,"zipped":zip(ordos,nums)})
def get_doc(request):
	pat=request.user.person.patient
	doc = Visite.objects.filter(patient_id=pat.pk).order_by("-date_created").values("medcin_id").distinct()
	doc=Doctor.objects.filter(INP__in=doc)
	

	return render(request,"doctor/visites.html",{"patient":True,"data":doc,"title":"Doctors","get_patient":True,})
def profile(request,pk):
	if request.user.person.patient.permission_privacy or request.person.patient.pk==pk:
		return render(request,"patient/profile_active.html",)
	else:
		return render(request,"patient/profile.html",{})
