from django.urls import path
from .views import preview

from .views import preview, success

urlpatterns = [
    path("preview", preview, name="checkout_preview"),
    path("success", success, name="checkout_success"),
]
