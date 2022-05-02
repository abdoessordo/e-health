from django.shortcuts import render,redirect, get_object_or_404
from patient.models import Patient
from ordonnance.models import Ordonnance,Meds
from mutuelle.models import AllMutuelle
from doctor.models import Visite,Doctor,Appointement
from django.core import serializers
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q    

from landing.models import Person 
from django.contrib import messages
import datetime,logging
from django.db.models.aggregates import Count,Sum
from django.core.paginator import Paginator

def register(request):
	if request.method=="POST":
		params=request.POST

		immatriculation=(None if params.get("immatriculation")=="" else params.get("immatriculation"))
		permission_privacy=(1 if  params.get("privacy",0).strip()=="on" else 0)
		logging.warning(params.get("privacy",0))
		affiliation=params["n_affiliation"]
		date_adhesion=params["date_adhesion"]
		if (date_adhesion in ["" , "None"] or immatriculation in ["" , "None"] or affiliation in ["" , "None"]) :
			return render(request,"patient/edit.html",{"title":"Settings & Privacy","profile_settings":True})
		else:
			a_mutuelle=1
		obj=Patient.objects.update_or_create(
			person_id=request.user.person,
			defaults={"a_mutuelle":a_mutuelle,"immatriculation":immatriculation,
			"permission_privacy":permission_privacy,"date_adhesion":date_adhesion,"n_affiliation":affiliation})
		
		messages.add_message(request, messages.ERROR,"Good job")
		return  redirect("patient:register")
	else:
		return render(request,"patient/edit.html",{"title":"Settings & Privacy","profile_settings":True})


def get_patient_visites_history(request):
	visites = Visite.objects.filter( patient_id=request.user.person.patient.id).order_by("-date_created")
	filt=datetime.date.today()-datetime.timedelta(days=7)
	visites1=visites.filter(date_created__gte=filt)
	doc=visites.values("medcin_id").distinct()
	doc=Doctor.objects.filter(INP__in=doc)
	paginator=Paginator(visites, 25)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, "doctor/visites.html", {"data":page_obj,'visite_seek':True,"title":"My Consultations","num_doc":len(doc),"num_visite":len(visites1)})
def get_other_visites_history(request,pk):
	pat=Patient.objects.get(pk=pk)
	if pat.permission_privacy:
		visites = Visite.objects.filter( patient_id=pk)
		allowed=True
	else:
		visites=[]
		allowed=False
	logging.warning(pat.permission_privacy)
	return render(request, "doctor/visites.html", {"data":visites,"allowed":allowed,'other_visite_seek':True,"title":f"{pat.person_id.nom} {pat.person_id.prenom} Consultations"})


def get_visite_details(request,visite):
	visite=get_object_or_404( Visite,pk=visite)
	return render(request,"doctor/visite_details.html",{
				
				"visite":visite,
		})
def dashboard(request):
	

	count_visites = Visite.objects.filter( patient_id=request.user.person.patient.pk).count()
	pres=Visite.objects.filter( patient_id=request.user.person.patient).annotate(count=Count("ordonnance__id_medicament"),filter=Q(count__gt=0)).select_related("medcin_id").order_by("-date_created")[:3]

		
	ordon_num=Ordonnance.objects.filter(id_visite__patient_id=request.user.person.patient).count()
	
	query_set = AllMutuelle.objects.filter(patient_id=request.user.person.patient)[:3]
	visites=Appointement.objects.filter(patient_id=request.user.person.patient).order_by("-date").select_related("medcin_id")
	total = AllMutuelle.objects.filter(patient_id=request.user.person.patient).aggregate(total=Count("id"))

	return render(request,"patient/dashboard.html",{"count_visites":count_visites,"insurances_query":query_set,"insurances":total,"dashboard":True,"visites":visites,"title":"Dashoard","pres":pres})
def get_doc(request):
	pat=request.user.person.patient
	filt=datetime.date.today()-datetime.timedelta(days=7)
	#visites = Visite.objects.filter(patient_id=pat.pk).order_by("-date_created")
	#visites1=visites.filter(date_created__gte=filt)
	
	doc=Doctor.objects.filter(visites__patient_id=pat).order_by('-visites__date_created').prefetch_related("visites")
	doc_stat=Doctor.objects.filter(visites__patient_id=pat,visites__date_created__gte=filt).aggregate(tot=Count("INP"),appoint=Count("appointements__pk"),visites_count=Count("visites"))
	
	
	paginator=Paginator(doc, 25)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request,"doctor/visites.html",{"data":page_obj,"title":"Doctors","get_patient":True,"num_doc":doc_stat["tot"],"num_visite":doc_stat["visites_count"],"num_appointement":doc_stat["appoint"]})
def profile(request,pk):
	pat=Patient.objects.get(pk=pk)
	visites = Visite.objects.filter( patient_id=pk).order_by("-date_created").select_related("medcin_id")[:6]
	pres=Visite.objects.filter( patient_id=pk).annotate(count=Count("ordonnance__id_medicament"),filter=Q(count__gt=0)).select_related("medcin_id").order_by("-date_created")[:3]
	appointements_waiting=Appointement.objects.filter(status="2").aggregate(count=Count("id"))
	appointements_done=Appointement.objects.filter(status="1").aggregate(count=Count("id"))
	meds=Meds.objects.filter(ordonnance__id_visite__patient_id=pat).order_by("-ordonnance__date_purchase")[:6]
	if pat.permission_privacy or request.user.person.patient.pk==pk:
		return render(request,"patient/profile_active.html",{"profile":True,"patient":pat,"title":f"{pat.person_id.nom} {pat.person_id.prenom}","visites":visites,"meds":meds,"appointements_waiting":appointements_waiting,"appointements_done":appointements_done,"pres":pres})
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
	return render(request, "doctor/visites.html", {"data":ords,"allowed":allowed,'other_visite_seek':True,"title":f"{pat.person_id.nom} {pat.person_id.prenom} Consultations"})
def book_appointement(request,doc):
	doc=Doctor.objects.get(pk=doc)
	if request.method=="POST":
		params=request.POST
	

		app=Appointement(medcin_id=doc,patient_id=request.user.person.patient,date=params["date"],heure=params["time"])
		app.save()
		return redirect("patient:dashboard")
	else:
		return render(request,"patient/book_doctor.html",{"doc":doc,"book":True})
def search_doc(request):
	
	if request.method=="POST":
		params=request.POST
		name=params.get("nom",None)

		ville=params.get("ville",None)
		docs=[]
		if ville != None or name != None:
			filters={}
			if name:
				filters["person_id__nom__icontains"]=name
			if ville:
				filters["ville"]=ville

			logging.warning(filters)
			docs=Doctor.objects.filter(**filters)
		return render(request,"patient/search_result.html",{"book":True,"docs":docs})
	else:
		return render(request,"patient/search.html",{"book":True})