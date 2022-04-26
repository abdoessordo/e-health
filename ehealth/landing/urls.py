from . import views
from django.urls import path
app_name="landing"

urlpatterns = [
        path("", views.index, name="index"),
        path("login/", views.login_user, name="login"),
        path("register/", views.register_user, name="register"),
        path("redirect/<int:loginp>",views.re_redirect,name="redirect"),
]
