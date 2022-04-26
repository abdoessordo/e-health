from django.urls import  path
from . import views

app_name = 'mutuelle'

urlpatterns = [

	path("all_mutuelles/", views.all_mutuelles, name='all_mutuelles'),
]
