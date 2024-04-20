
from django.urls import path
from .views import client

urlpatterns = [
    path("client/", client, name="client"),
]
