from django.urls import path, include


urlpatterns = [
    # path('', include('multiplication_table.urls')),
    path("", include("day_256.urls"))
]
