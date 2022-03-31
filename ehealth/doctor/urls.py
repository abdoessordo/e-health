from django.urls import include, path
from . import views
app_name='doctor'
urlpatterns=[

	path("getmedhistory",views.get_meds_history),
	path("getvisiteshistory",views.get_visites_history),
	path("register",views.register),
	path("create_visite",views.create_visite),


]