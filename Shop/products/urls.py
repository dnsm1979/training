
from django.urls import path
<<<<<<< HEAD
from .views import products, products_detail, products_edit, products_delete

urlpatterns = [
    path("", products, name="products"),
    path("<int:product_id>", products_detail, name="products_detail"),
    path("<int:product_id>/edit", products_edit, name="products_edit"),
    path("<int:product_id>/delete", products_delete, name="products_delete"),
=======
from .views import products

urlpatterns = [
    path("products/", products, name="products"),
>>>>>>> d501b3992675a797640e7400aa0be0837b5125da
]
