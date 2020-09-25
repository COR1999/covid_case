from django.urls import path
from . import views

urlpatterns = [
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_user, name="logout_user"),


]
