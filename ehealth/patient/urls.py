from django.urls import include, path
from . import views
app_name="patient"
urlpatterns=[

	path("register",views.register,name="register"),
	path("visites",views.get_patient_visites_history,name="visites"),
	path("visite/<int:visite>/",views.get_visite_details,name="get_visite_details"),
	path("dashboard",views.dashboard,name="dashboard"),
	path("doctors",views.get_doc,name="doctors"),
	path("profile/<int:pk>",views.profile,name="profile"),
	path("visites/<int:pk>",views.get_other_visites_history,name="others_visite"),
	path("presc/<int:pk>",views.get_other_presc,name="others_presc"),
	path("book/<int:doc>",views.book_appointement,name="book"),
	path("search",views.search_doc,name="search")
]