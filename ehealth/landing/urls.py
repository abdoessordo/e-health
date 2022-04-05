from . import views
from django.urls import path
app_name="landing"
urlpatterns = [
        
        path("",views.login_user,name="login"),

]
