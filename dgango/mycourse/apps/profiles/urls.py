from django.urls import path

from .views import *


urlpatterns = [
    path('login',  login, name='login'),
    path('home',  home, name='home'),
    path('logout',  logout, name='logout'),
    path('register', register, name='register'),
    path('change_password', change_password, name='change_password'),
    path('change_password/success', change_password_success, name='change_password_success'),
    path('courses/<int:course_id>', profile_course, name='profile_course'),
]

