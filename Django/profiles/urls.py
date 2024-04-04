from django.urls import path
from .views import *

urlpatterns = [
    path("login", login, name="login"),
    path("home", home, name="home"),
    path("logout", logout, name="logout"),
    path("register", register, name="register"),
]