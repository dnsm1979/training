from django.urls import path, include


urlpatterns = [
    path('', include('multiplication_table.urls')),
]