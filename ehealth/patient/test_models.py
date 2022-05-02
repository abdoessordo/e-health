from model_bakery import baker
from patient.models import Patient
from doctor.models import Doctor,Visite
from med.models import Meds
from pharmacie.models import Pharmacie
import os

import random,itertools
meds=itertools.cycle(random.sample(list(Meds.objects.all()),5))
def ret_med():
	print("z")
	return meds.__next__()
doc=Doctor.objects.get(pk=9)
pat=Patient.objects.get(pk=1)
phar=Pharmacie.objects.get(pk=1)
visite=Visite.objects.get(pk=754)
med=Meds.objects.get(pk=6118001230068)
ordonnaces = baker.make('ordonnance.Ordonnance',price=random.randint(10,300),make_m2m=True,id_pharmacie=phar,_quantity=5,_fill_optional=True,_create_files=True,id_visite=visite)

"""
names=open('/home/salaheddine/essordo/e-health/ehealth/patient/names.txt',"r").readlines()

		
cins=itertools.cycle(random.sample(range(10000,999999),800))
phones=itertools.cycle(random.sample(range(10000000,99999999),300))
names1=itertools.cycle(random.sample(range(0,len(names)),300))
names2=itertools.cycle(random.sample(range(0,len(names)),300))

def ret():
	x=str(cins.__next__())
	print(x)
	return  x
def ret_phone():
	return "06"+str(phones.__next__())
def ret_nom():
	a=random.randint(0,len(names))
	
	return names[names2.__next__()].strip()
def ret_prenom():
	
	
	return names[names1.__next__()].strip()
imgs=os.listdir("/home/salaheddine/essordo/e-health/ehealth/media/profile_pics")

person = baker.make('landing.Person',user__username=ret,nom=ret_nom,
									prenom=ret_prenom,
									user__email=f"{random.choice(names)}_{random.choice(names)}@gmail.com",
									phone=ret_phone,
									img=f"profile_pics/{random.choice(imgs)}",
									_quantity=30,_fill_optional=True,)
persons1=itertools.cycle(person)
persons2=itertools.cycle(person)
def ret_pers1():
	return (persons1.__next__())
def ret_pers2():
	return (persons2.__next__())
def ret_privacy():
	return random.choice([0,1])
doctors=baker.make("doctor.Doctor",_quantity=15,_fill_optional=True,person_id=ret_pers1,activated=1)
patients=baker.make("patient.Patient",_quantity=15,_fill_optional=True,person_id=ret_pers2,permission_privacy=ret_privacy)
doctors1=itertools.cycle(doctors)
patients1=itertools.cycle(patients)
def ret_pat1():
	return (patients1.__next__())
def ret_doc1():
	return (doctors1.__next__())
def ret_stat():
	return random.choice([1,2,3])
visites_doc=baker.make("doctor.Visite",_quantity=25,medcin_id=doc,patient_id=ret_pat1)
visites_pat=baker.make("doctor.Visite",_quantity=25,medcin_id=ret_doc1,patient_id=pat)
appointement_doc=baker.make("doctor.Appointement",_quantity=24,medcin_id=doc,patient_id=ret_pat1,status=ret_stat)
appointement_pat=baker.make("doctor.Appointement",_quantity=24,medcin_id=ret_doc1,patient_id=pat,status=ret_stat)

ordonnaces = baker.make('ordonnance.Ordonnance',price=random.randint(10,300),id_medicament=ret_med,id_pharmacie=phar,_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites_doc))
ordonnaces = baker.make('ordonnance.Ordonnance',price=random.randint(10,300),id_medicament=ret_med,id_pharmacie=phar,_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites_doc))
ordonnaces = baker.make('ordonnance.Ordonnance',price=random.randint(10,300),id_medicament=ret_med,id_pharmacie=phar,_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites_doc))
ordonnaces = baker.make('ordonnance.Ordonnance',price=random.randint(10,300),id_medicament=ret_med,id_pharmacie=phar,_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites_pat))
ordonnaces = baker.make('ordonnance.Ordonnance',price=random.randint(10,300),id_medicament=ret_med,id_pharmacie=phar,_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites_pat))
ordonnaces = baker.make('ordonnance.Ordonnance',price=random.randint(10,300),id_medicament=ret_med,id_pharmacie=phar,_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites_pat))


person = baker.make('landing.Person',_quantity=250,_create_files=True,_fill_optional=True,)


#person = baker.make('landing.Person',_quantity=250,_create_files=True,_fill_optional=True,)
for i in range(len(person)):
	pats = baker.make('patient.Patient',_create_files=True,_fill_optional=True,person_id=person[i])
	visites = baker.make('doctor.Visite',_quantity=25,_fill_optional=True,_create_files=True,patient_id=pats,medcin_id=doc)

	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))

	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))
	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))

"""