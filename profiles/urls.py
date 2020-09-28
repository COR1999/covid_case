from django.urls import path
from . import views

urlpatterns = [
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_user, name="logout_user"),
    path("my_profile/<user_name>", views.my_profile, name="my_profile"),
    path("edit_profile/<user_name>", views.edit_profile, name="edit_profile"),

]
