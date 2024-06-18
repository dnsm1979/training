
from django.urls import path
from .views import sellers

urlpatterns = [
    path("sellers/", sellers, name="sellers"),
]
