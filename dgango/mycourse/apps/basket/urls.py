from django.urls import path
from .views import basket_add

from .views import basket_add, basket_detail, basket_remove

urlpatterns = [
    path("add/<int:course_id>", basket_add, name="basket_add"),
    path("remove/<int:line_id>", basket_remove, name="basket_remove"),
    path("detail", basket_detail, name="basket_detail"),
]
