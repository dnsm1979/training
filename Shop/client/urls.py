
from django.urls import path
from .views import client, edit_client, delete_client

urlpatterns = [
    path("", client, name="client"),
    path("edit_client/<int:pk>/", edit_client, name="edit_client"),
    path("delete_client/<int:pk>/", delete_client, name="delete_client"),
]
