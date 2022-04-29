from django.urls import include, path
app_name="pharmacist"
from . import views
urlpatterns=[


	 path("dashboard/", views.dashboard, name="dashboard"),
	 path("register/", views.register, name="register"),
]