from django.urls import include, path
from . import views
app_name='doctor'
urlpatterns=[

	path("getmedhistory",views.get_meds_history),
	path("getvisiteshistory",views.get_visites_history),
	path("register",views.register,name="register"),
	path("create_visite",views.create_visite),
	path("get_doctor_visite",views.get_doc_visites_history,name="visites"),
	path("get_visite_details/<int:visite>/",views.get_visite_details,name='get_visite_details'),
	path("dashboard",views.dashboard,name="dashboard"),
	path("patients",views.get_patient,name="patients"),
	path("fill",views.fill)

]