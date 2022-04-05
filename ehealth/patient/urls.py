from django.urls import include, path
from . import views
app_name="patient"
urlpatterns=[

	path("register",views.register,name="register"),
	path("visites",views.get_patient_visites_history,name="visites"),
	path("visite/<int:visite>/",views.get_visite_details,name="get_visite_details"),
]