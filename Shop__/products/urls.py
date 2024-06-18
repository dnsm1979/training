
from django.urls import path
from .views import products, products_detail, products_edit, products_delete

urlpatterns = [
    path("", products, name="products"),
    path("<int:product_id>", products_detail, name="products_detail"),
    path("<int:product_id>/edit", products_edit, name="products_edit"),
    path("<int:product_id>/delete", products_delete, name="products_delete"),
]
