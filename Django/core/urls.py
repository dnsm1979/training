
from django.urls import path
from .views import *

urlpatterns = [
    path("", main, ),
    path("about", about, name="about"),
    path("contacts", contacts, name="contacts"),
    path("management", management, name="management"),
    path("news", news, name="news"),
    path("news/<int:news_id", news_detail, name="news_detail"),
    path("branches", branches, name="branches"),
    path("branches/<int:branch_id>", branches_detail, name="branches_detail"),

]
