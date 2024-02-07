from django.urls import path
from . import views


urlpatterns = [
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    ]