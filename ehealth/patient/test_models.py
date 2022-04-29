from model_bakery import baker
from patient.models import Patient
from doctor.models import Doctor
import random
# 1st form: app_label.model_name
#docs = baker.make('doctor.Doctor',_quantity=25,_create_files=True,_fill_optional=True,activated=random.choice([0,1]))
#pat = baker.make('patient.Patient',_quantity=25,_create_files=True,_fill_optional=True)


# pat=Patient.objects.get(pk=226)
# person = baker.make('landing.Person',_quantity=25,_create_files=True,_fill_optional=True,)
# for i in range(len(person)):
# 	docs = baker.make('doctor.Doctor',_create_files=True,_fill_optional=True,activated=1 ,person_id=person[i])
# 	visites = baker.make('doctor.Visite',_quantity=25,_fill_optional=True,_create_files=True,patient_id=pat,medcin_id=docs)

# 	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))

# 	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))
# 	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))


#pharmacies = baker.make('pharmacie.Pharmacie',_quantity=25,_fill_optional=True,_create_files=True,)

doc=Doctor.objects.get(pk=123456)
person = baker.make('landing.Person',_quantity=25,_create_files=True,_fill_optional=True,)
for i in range(len(person)):
	pats = baker.make('patient.Patient',_create_files=True,_fill_optional=True,person_id=person[i])
	visites = baker.make('doctor.Visite',_quantity=25,_fill_optional=True,_create_files=True,patient_id=pats,medcin_id=doc)

	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))

	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))
	ordonnaces = baker.make('ordonnance.Ordonnance',_quantity=random.randint(1,10),_fill_optional=True,_create_files=True,id_visite=random.choice(visites))

