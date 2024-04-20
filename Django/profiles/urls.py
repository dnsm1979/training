from django.urls import path
from .views import *

urlpatterns = [
    path("login", login, name="login"),
    path("home", home, name="home"),
    path("logout", logout, name="logout"),
    path("register", register, name="register"),
    path("set_password", set_password, name="set_password"),
    path("password_change_none", password_change_done, name="password_change_none"),
]