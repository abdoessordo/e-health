from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import  User
from landing.models import Person
from doctor.models import Doctor
from pharmacie.models import Pharmacie

import logging
from django.contrib import messages

def login_user(request):
	

	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		loginp = request.POST["login"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			if loginp=="1":
				try:
					if user.person.patient.id is not None:
						return redirect("patient:visites")
				except :
					return redirect("patient:register")
			elif loginp=="2":
				try: 
					if user.person.doctor.id is not None:
						return redirect("doctor:visites")
				except:
					return redirect("doctor:register")
				

			elif loginp=="3":
				pass
				#return redirect("pharmacist:register")
			else:
				messages.add_message(request, messages.ERROR, 'Something is Wrong')
				return render(request,"patient:register")
		else:

			messages.add_message(request, messages.ERROR, 'Wrong combination')
     
			return render(request, 'landing/login.html', {})

	else:
		return render(request,"landing/login.html", {})
	
# def get_type(request):
# 	user=request.user
# 	doctor=user.doctor
# 	patient=user.patient
# 	pharmacie=user.pharmacie
# 	if doctor:
# 		return render(request, 'doctor/visites.html', {"role":"doctor"})
# 	if patient:
# 		return render(request, 'doctor/visites.html', {"role":"patient"})

# 	if pharmacie:
# 		return render(request, 'doctor/visites.html', {"role":"pharmacie"})


# NEW LANGING PAGE
def index(request):
	return render(request, "landing/index.html")


def register_user(request):
	if request.method=="POST" :
			username = request.POST['username']
			password = request.POST['password1']
			password2 = request.POST['password2']
			first_name=request.POST["first_name"]
			last_name=request.POST["last_name"]
			sexe=request.POST["sexe"]
			datedenaissance=request.POST["date"]
			if password==password2:
				us=User.objects.create_user(username=username,password=password)
				per=Person(user=us,nom=last_name,prenom=first_name,sexe=sexe,datedenaissance=datedenaissance)
				per.save()
				messages.add_message(request, messages.ERROR, 'You can login now')
				return redirect('landing:login')
			else:
				
				messages.add_message(request, messages.ERROR, 'Something is Wrong')
	     	
				return render(request, 'landing/register.html', {})
	else:
		return render(request, 'landing/register.html', {})

