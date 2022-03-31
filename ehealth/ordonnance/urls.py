from django.urls import include, path
from . import views
app_name="ordonnance"
urlpatterns=[

path('create_ordonnance',views.create_ordonnance),
path('create_med',views.create_med),

]