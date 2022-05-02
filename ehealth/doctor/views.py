from django.shortcuts import render,get_object_or_404,redirect
from patient.models import Patient
from ordonnance.models import Ordonnance
from doctor.models import Visite,Doctor,Appointement
from med.models import Meds
from django.core import serializers
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import logging
import datetime
from django.db.models.aggregates import Count

def register(request):
	if request.method=="POST":
		params=request.POST
		INP=params["INP"]
		ville=params["ville"]
		speciality=params["speciality"]
		if INP=="" or ville=="" or ville=="":
			return render(request,"patient/edit.html",{"profile_settings":True})

		obj=Doctor.objects.update_or_create(
			person_id=request.user.person,
			defaults={"ville":ville,"INP":INP,"speciality":speciality})
		
		
		return  redirect("doctor:visites")
	else:
		return render(request,"patient/edit.html",{"profile_settings":True})

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
		visites = Visite.objects.filter( medcin_id=doctor.INP).order_by("-date_created")
		filt=datetime.date.today()-datetime.timedelta(days=7)
		pat = Visite.objects.filter( medcin_id=doctor.INP,date_created__gte=filt).order_by("-date_created")
		pats=Patient.objects.filter(id__in=pat.values_list("patient_id"))
		paginator=Paginator(visites, 25)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,"doctor/visites.html",{ "data":page_obj,"dist_pat":len(pats),"num_visite":len(pat),'visite_seek':True,"title":"Consultations"})
	else:
		return render(request,"ehealth/error.html",{'visite_seek':True,})

def get_visite_details(request,visite):
	visite=get_object_or_404( Visite,pk=visite)
	traitements=Ordonnance.objects.filter(id_visite=visite,le_type="Traitement")
	meds=Ordonnance.objects.filter(id_visite=visite,le_type="Medicaments").prefetch_related("id_medicament")
	privacy=visite.patient_id.permission_privacy
	modifiable=True
	
	condition=int(request.user.person.doctor.INP)!=visite.medcin_id.INP
	if condition:
		modifiable=False
	if modifiable ==False and privacy==0:
		return HttpResponse({"error":"you're not allowed"}, mimetype='application/json')

	return render(request,"doctor/visite_details.html",{
				"modifiable":modifiable,
				"visite":visite,
				"profile":True,
				"traitements":traitements,
				"meds":meds,

		})


def dashboard(request):
	doctor=request.user.person.doctor
	visites=[]
	pat=[]
	pat2=[]
	if doctor.activated:
		visites = Visite.objects.filter( medcin_id=doctor.INP).order_by("-date_created")
		filt=datetime.date.today()-datetime.timedelta(days=7)
		pat = Visite.objects.filter( medcin_id=doctor.INP,date_created__gte=filt).order_by("-date_created")
		pat2=pat.distinct()
		pat=Patient.objects.filter(id__in=pat.values_list("patient_id"))
		pat2=Patient.objects.filter(id__in=pat2.values_list("patient_id"))[:3]
		visites=Appointement.objects.filter(medcin_id=request.user.person.doctor)[0:10]
		appointements=Appointement.objects.filter(medcin_id=request.user.person.doctor,status="2")[0:3]

		num_appt=Appointement.objects.filter(medcin_id=request.user.person.doctor,status=2).aggregate(count=Count('id'))['count']
	return render(request,"doctor/dashboard.html",{"num_appt":num_appt,"appointements":appointements,"dashboard":True,"visites":visites,"title":"Dashoard","dist_pat":len(pat),"last_3":pat2})
def get_patient(request):
	doctor=request.user.person.doctor
	if doctor.activated:
		pat = Visite.objects.filter( medcin_id=doctor.INP).order_by("-date_created").values("patient_id").distinct()
		pat=Patient.objects.filter(id__in=pat)
		filt=datetime.date.today()-datetime.timedelta(days=7)

		pat_len=Visite.objects.filter( medcin_id=doctor.INP,date_created__gte=filt).order_by("-date_created")
		paginator=Paginator(pat, 25)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,"doctor/visites.html",{"num_visite":len(pat_len),"data":page_obj,"title":"Patients","dist_pat":len(pat),"get_patient":True})
	else:
		return render(request,"ehealth/error.html",{'get_patient':True,})

def fill(request):
	import sqlite3
	db=sqlite3.connect("meds.db")
	cur=db.cursor()
	sql="SELECT * FROM Meds"
	res=cur.execute(sql)

	for x in res:
		logging.warning(x)
		Meds.objects.create(
			code=x[1],
			nom=x[2] ,
			dci1=x[3],
			dosage1=x[4],
			unite_dosage1=x[5],
			forme=x[6],
			presentation=x[7],
			ppv=x[8],
			ph=x[9],
			prix_br=x[10],
			princeps_generique=x[11],
			taux_remboursement=x[12],)

	return render(request,"doctor/visites.html",{"title":"done"})