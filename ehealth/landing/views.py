from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import  User
from landing.models import Person
import logging
from django.contrib import messages
def login_user(request):
	login_bool=False
	if request.POST.get("login",0):
		login_bool=True

	if request.method=="POST" and  login_bool :
		logging.getLogger(__name__).warning('login')
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			return redirect("patient:register")
		else:

			messages.add_message(request, messages.ERROR, 'Wrong combination')
     
			return render(request, 'landing/index.html', {"toggle":True,"login":True})   
	elif request.method=="POST" and  not login_bool :
		logging.getLogger(__name__).warning('register')
		
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

				return render(request, 'landing/index.html', {"toggle":True,"login":True})
			else:
				toggle=1
				messages.add_message(request, messages.ERROR, 'Wrong combination')
	     
				return render(request, 'landing/index.html', {"toggle":True,"login":False})
	elif request.method!="POST":
		return render(request,"landing/index.html", {"toggle":False,"login":True})
	
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
