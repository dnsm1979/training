
from django.urls import path
from .views import products

urlpatterns = [
    path("products/", products, name="products"),
]
