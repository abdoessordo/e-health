from django.shortcuts import render
from patient.models import Patient
from ordonnance.models import Ordonnance
from med.models import Meds
from doctor.models import Visite,Doctor
from pharmacie.models import Pharmacie
from django.core import serializers
from django.views.decorators.http import require_POST
from  django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
@require_POST
@csrf_exempt
def create_med(request):
	params=request.POST
	name=params["name"]
	med=Medicament.objects.create(nom=name)
	med.save()
	data={"Done":"med created"}
	return  JsonResponse(data)
@require_POST
@csrf_exempt
def create_ordonnance(request):
	"""
	id_visite=models.ForeignKey(Visite, on_delete=models.CASCADE)
	class typee(models.TextChoices):
		Traitement = 'Traitement'
		Medicaments = 'Medicaments'
	le_type=models.CharField(max_length=13,choices=typee.choices)
	id_medicament=models.OneToOneField(Medicament,on_delete=models.CASCADE,)
	duree_de_traitement=models.IntegerField()
	description_de_traitement=models.CharField(max_length=255)
	id_pharmacie=models.OneToOneField(Pharmacie,on_delete=models.CASCADE)
	price=models.IntegerField()
	a_mutuelle=models.BooleanField()
	"""
	params=request.POST
	visite=Visite.objects.get(pk=params['id_visite'])
	patient=Patient.objects.get(pk=visite.patient_id.pk)
	a_mutuelle=patient.a_mutuelle
	types=params.getlist("type")
	traitements=params.getlist("traitements")
	duree_de_traitement=params.getlist("duree")
	desc=params.getlist("desc")
	id_pharmacie=params["id_pharmacie"]
	num=len(types)
	for i in range(num):
		med=Medicament.objects.get(pk=traitements[i])
		phar=Pharmacie.objects.get(pk=id_pharmacie)
		p=Ordonnance.objects.create(id_visite=visite,le_type=types[i],
			id_medicament=med,duree_de_traitement=duree_de_traitement[i],
			description_de_traitement=desc[i],a_mutuelle=a_mutuelle,id_pharmacie=phar
			)
		p.save()
	data={"Done":"ordo created"}
	return  JsonResponse(data)


def add_medicaments(request,visite):
	if request.method=="POST":
		params=request.POST
		visite=Visite.objects.get(pk=visite)
		patient=Patient.objects.get(pk=visite.patient_id.pk)
		a_mutuelle=patient.a_mutuelle
		#types=params.getlist("type")
		meds=params.getlist("med")
		duree_de_traitement=params.getlist("duree")
		desc=params.getlist("desc")
		quantite=params.getlist("quant")
		num=len(quantite)
		for i in range(num):
			med=Meds.objects.get(index=meds[i])
			#phar=Pharmacie.objects.get(pk=id_pharmacie)
			p=Ordonnance(id_visite=visite,le_type="Medicaments",
				id_medicament=med,duree_de_traitement=duree_de_traitement[i],
				description_de_traitement=desc[i],a_mutuelle=a_mutuelle,quantite=quantite[i]
				)
			p.save()
		data={"Done":"ordo created"}
		return  JsonResponse(data)
	
	else:

		return render(request, "add_medicaments.html")


def add_traitement(request,visite):
	if request.method=="POST":
		params=request.POST
		visite=Visite.objects.get(pk=visite)
		patient=Patient.objects.get(pk=visite.patient_id.pk)
		a_mutuelle=patient.a_mutuelle
		#types=params.getlist("type")
		traitement=params.getlist("traitements")
		desc=params.getlist("desc")
		num=len(desc)
		for i in range(num):
			#med=Medicament.objects.get(pk=1)
			#phar=Pharmacie.objects.get(pk=id_pharmacie)
			p=Ordonnance(id_visite=visite,le_type="Traitement",
				description_de_traitement=desc[i],a_mutuelle=a_mutuelle,nom_traitement=traitement[i]
				)
			p.save()
		data={"Done":"traitement created"}
		return  JsonResponse(data)

	else:

		return render(request, "add_traitement.html")