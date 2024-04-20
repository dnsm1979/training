
from django.urls import path
from .views import Positions

urlpatterns = [
    path("positions/", positions, name="positions"),
]
