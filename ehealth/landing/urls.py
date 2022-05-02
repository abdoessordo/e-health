from . import views
from django.urls import path
app_name="landing"

urlpatterns = [
        # path("", views.index, name="index"),
        path("", views.login_user, name="login"),
        path("register/", views.register_user, name="register"),
        path("redirect/<int:loginp>",views.re_redirect,name="redirect"),
        path("profileregister/",views.profile_register,name="profile_register"),
        path("changing_pic/",views.changing_pic,name="change_pic"),
        path("logout/",views.logout_view,name="logout")


]
