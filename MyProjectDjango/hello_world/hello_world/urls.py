from django.urls import path
from multiplication_table import views

urlpatterns = [
    path('', views.index, name='home'),
]