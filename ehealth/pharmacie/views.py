from django.shortcuts import render
from doctor.models import Visite
from ordonnance.models import Ordonnance
from pharmacie.models import Pharmacie
import datetime
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.db.models.aggregates import Count,Sum
import logging
# Create your views here.
def dashboard(request):
	filt=datetime.date.today()-datetime.timedelta(days=7)
	ordonnances=Ordonnance.objects.filter(
		le_type="Medicaments",id_pharmacie=request.user.person.pharmacie.pk,date_purchase__gte=filt
		).annotate(
		count=Count("id_medicament"),prix=Sum("id_medicament__prix_br")
		).order_by("-date_purchase").select_related("id_visite__patient_id")[:3]
	
	logging.warning(ordonnances[0].prix)
	pat_num=Ordonnance.objects.filter(
		le_type="Medicaments",id_pharmacie=request.user.person.pharmacie.pk,id_visite__date_created__gte=filt
		).aggregate(
		count=Count("id_visite__patient_id" ,distinct=True),
		tot=Sum("id_medicament__prix_br")
		)
	
	
	return render(request,"pharmacist/dashboard.html",{"dashboard":True,"title":"Dashboard","pat_num":pat_num["count"],"income":pat_num["tot"],"ordonnances":ordonnances})

def register(request):
	if request.method=="POST":
			try:
				INP=request.POST["INP"]
				ville=request.POST["ville"]
				adresse=request.POST["adresse"]
				nom=request.POST["nom"]
				
				Pharmacie.objects.update_or_create(
					person_id=request.user.person,
					defaults={"INP":INP,"ville":ville,"adresse":adresse,"nom":nom}
					)
				messages.add_message(request,messages.SUCCESS,"Values Updated")
				return JsonResponse({"data":"Done"})
			except Exception as e:
					messages.add_message(request, messages.ERROR, 'Something is Wrong')
					return JsonResponse({"data":str(e)})
	else:
			return render(request,"patient/edit.html",{"profile_settings":True,"title":"Settings & Privacy"})
