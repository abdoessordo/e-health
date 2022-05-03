from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from landing.models import Person
from doctor.models import Doctor
from pharmacie.models import Pharmacie
from patient.models import Patient
import logging
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


def re_redirect(request, loginp):
	if loginp == '1':
		request.session["role"] = "patient"
		try:
			request.user.person.patient.id is not None
			return redirect("patient:dashboard")
		except:
			return redirect("patient:register")
	elif loginp == '2':
		request.session["role"] = "medecin"
		try:
			request.user.person.doctor.INP is not None
			return redirect("doctor:dashboard")
		except:
			return redirect("doctor:register")

	elif loginp == '3':
		request.session["role"] = "pharmacist"

		try:
			request.user.person.pharmacie.INP is not None
			return redirect("pharmacist:dashboard")
		except:
			return redirect("pharmacist:register")
	else:
		logging.warning(loginp, type(loginp))

		messages.add_message(request, messages.ERROR, 'Something is Wrong')
		return redirect("patient:visites")


def login_user(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		loginp = request.POST["login"]

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			return re_redirect('landing:redirect', loginp)

		else:

			messages.add_message(request, messages.ERROR, username)

			return render(request, 'landing/login.html', {})

	else:
		return render(request, "landing/login.html", {})


# NEW LANGING PAGE
def index(request):
	return render(request, "landing/index.html")


def register_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password1']
		password2 = request.POST['password2']
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		sexe = request.POST["sexe"]
		datedenaissance = request.POST["date"]
		adresse = request.POST["adresse"]
		ville = request.POST["ville"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		if password == password2:
			us = User.objects.create_user(
				username=username, password=password, email=email)
			per = Person(user=us, nom=last_name, prenom=first_name, sexe=sexe,
			             datedenaissance=datedenaissance, ville=ville, adresse=adresse, phone=phone)
			per.save()
			pat = Patient(person_id=per)
			pat.save()
			messages.add_message(request, messages.ERROR, 'You can login now')
			return redirect('landing:login')
		else:

			messages.add_message(request, messages.ERROR, 'Something is Wrong')

			return render(request, 'landing/register.html', {})
	else:
		return render(request, 'landing/register.html', {})


@require_POST
def profile_register(request):
	# try:

	adresse = request.POST["adresse"]
	ville = request.POST["ville"]
	phone = request.POST["phone"]
	request.user.person.ville = ville
	request.user.person.adresse = adresse
	request.user.person.phone = phone
	request.user.person.save()
	messages.add_message(request, messages.SUCCESS, "Values Updated")
	return JsonResponse({"data": "Done"})
		# except :
		#  		messages.add_message(request, messages.ERROR, 'Something is Wrong')
		#  		return JsonResponse({"data":"Error"})


@require_POST
def changing_pic(request):
	try:
		img = request.FILES["img"]
		request.user.person.img = img
		request.user.person.save()
		return JsonResponse({"data": "Done"})
	except Exception as e:
		return JsonResponse({"data": str(e)})




def logout_view(request):
    logout(request)
    return redirect('landing:login')
