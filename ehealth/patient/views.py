from django.shortcuts import render,redirect, get_object_or_404
from patient.models import Patient
from ordonnance.models import Ordonnance
from mutuelle.models import AllMutuelle
from doctor.models import Visite,Doctor
from django.core import serializers
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from landing.models import Person 
from django.contrib import messages
import datetime,logging
from django.db.models.aggregates import Count

def register(request):
	if request.method=="POST":
		params=request.POST

		a_mutuelle= (1 if  params.get("a_mutuelle",0)=="on" else 0)
		immatriculation=(None if params.get("immatriculation")=="" else params.get("immatriculation"))
		permission_privacy=(1 if  params.get("privacy",0)=="on" else 0)
		affiliation=params["n_affiliation"]
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
		
		messages.add_message(request, messages.ERROR,"Good job")
		return  redirect("patient:register")
	else:
		return render(request,"patient/edit.html",{"patient":True,"title":"Settings & Privacy","profile_settings":True})


def get_patient_visites_history(request):
	visites = Visite.objects.filter( patient_id=request.user.person.patient.id).order_by("-date_created")
	filt=datetime.date.today()-datetime.timedelta(days=7)
	visites1=visites.filter(date_created__gte=filt)
	doc=visites.values("medcin_id").distinct()
	doc=Doctor.objects.filter(INP__in=doc)


	return render(request, "doctor/visites.html", {"data":visites,"patient":True,'visite_seek':True,"title":"My Consultations","num_doc":len(doc),"num_visite":len(visites1)})
def get_other_visites_history(request,pk):
	pat=Patient.objects.get(pk=pk)
	if pat.permission_privacy:
		visites = Visite.objects.filter( patient_id=pk)
		allowed=True
	else:
		visites=[]
		allowed=False
	return render(request, "doctor/visites.html", {"data":visites,"allowed":allowed,"patient":True,'other_visite_seek':True,"title":f"{pat.person_id.nom} {pat.person_id.prenom} Consultations"})


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
	query_set = AllMutuelle.objects.filter(patient_id=request.user.person.patient)
	total = AllMutuelle.objects.aggregate(total=Count("id"))
   
	return render(request,"patient/dashboard.html",{"insurances":total,"dashboard":True,"patient":True,"visites":visites,"title":"Dashoard","ordo":ordos,'nums':nums,"ordon_num":ordon_num,"zipped":zip(ordos,nums)})
def get_doc(request):
	pat=request.user.person.patient
	filt=datetime.date.today()-datetime.timedelta(days=7)
	visites = Visite.objects.filter(patient_id=pat.pk).order_by("-date_created")
	visites1=visites.filter(date_created__gte=filt)
	doc=visites.values("medcin_id").distinct()
	doc=Doctor.objects.filter(INP__in=doc)
	

	return render(request,"doctor/visites.html",{"patient":True,"data":doc,"title":"Doctors","get_patient":True,"num_doc":len(doc),"num_visite":len(visites1)})
def profile(request,pk):
	nums=[]
	ordos=[]
	ords=[]
	count=0
	pat=Patient.objects.get(pk=pk)
	visites = Visite.objects.filter( patient_id=pk).order_by("-date_created")
	for v in visites:
		ordo = Ordonnance.objects.filter( id_visite=v.pk)
		if len(ordo)>0:
			count+=1
			ordos.append(ordo[0])
			nums.append(len(ordo))
			if len(ords)<10:
				for i in ordo:
					ords.append(i)
			
		if count >=5:break
	ordon_num=len(Ordonnance.objects.filter(id_visite__in=visites.values("pk")))
	if pat.permission_privacy or request.user.person.patient.pk==pk:
		return render(request,"patient/profile_active.html",{"profile":True,"patient":pat,"title":f"{pat.person_id.nom} {pat.person_id.prenom}","visites":visites,"zipped":zip(ordos,nums),"ords":ords})
	else:
		return render(request,"patient/profile.html",{"patient":pat,"title":f"{pat.person_id.nom} {pat.person_id.prenom}" })
def get_other_presc(request,pk):
	ords=[]
	pat=Patient.objects.get(pk=pk)
	if pat.permission_privacy:
		visites = Visite.objects.filter( patient_id=pk)
		allowed=True
		for v in visites:
			ordo = Ordonnance.objects.filter( id_visite=v.pk)
			if len(ordo)>0:
				for i in ordo:
						ords.append(i)
	else:
		ords=[]
		allowed=False
	return render(request, "doctor/visites.html", {"data":ords,"allowed":allowed,"patient":True,'other_visite_seek':True,"title":f"{pat.person_id.nom} {pat.person_id.prenom} Consultations"})
