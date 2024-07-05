
from django.urls import path
from.views import category

from .views import main, category, course

urlpatterns = [
    path('', main, name='main'),
    path('category/<int:category_id>', category, name='category'),
    path('course/<int:course_id>', course, name='course'),
]
