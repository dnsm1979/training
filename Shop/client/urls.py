
from django.urls import path
from .views import client

urlpatterns = [
    path("", client, name="client"),
]
