from django.urls import include, path
from . import views
app_name="ordonnance"
urlpatterns=[

    path('create_ordonnance',views.create_ordonnance,name="create_ordonnance"),
    path('create_med',views.create_med),
    path("add_medicaments/<int:visite>", views.add_medicaments, name="add_medicaments"),
    path("add_traitements/<int:visite>", views.add_traitement, name="add_traitements"),

]