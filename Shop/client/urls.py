
from django.urls import path
from .views import client, edit_client

urlpatterns = [
    path("", client, name="client"),
    path("edit_client/<int:pk>/", edit_client, name="edit_client"),
]
