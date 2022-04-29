from django.shortcuts import render
from doctor.models import Visite
from ordonnance.models import Ordonnance
from pharmacie.models import Pharmacie
import datetime
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.contrib import messages
# Create your views here.
def dashboard(request):
	filt=datetime.date.today()-datetime.timedelta(days=7)
	visites=Visite.objects.filter(id_pharmacie=request.user.person.pharmacie.pk,date_created__gte=filt)
	patients=visites.values('patient_id').distinct()
	ordonnances=Ordonnance.objects.filter(id_visite__in=visites)
	tot=sum(ordonnances.values("prix"))
	return render(request,"pharmacist/dashboard.html",{"dashboard":True,"pharmacist":True,"title":"Dashboard","pat_num":len(patients),"income":tot})

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
			except:
					messages.add_message(request, messages.ERROR, 'Something is Wrong')
					return JsonResponse({"data":"error"})
	else:
			return render(request,"pharmacist/edit.html",{"profile_settings":True,"pharmacist":True,"title":"Settings & Privacy"})
