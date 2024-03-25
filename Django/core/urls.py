
from django.urls import path
from .views import *

urlpatterns = [
    path("", main, ),
    path("about", about, name="about"),
    path("contacts", contacts, name="contacts"),
    path("management", management, name="management"),
    path("news", news, name="news"),
    path("news/<int:news_id>", news_detail, name="news_detail"),
    path("news/add_news", add_news, name="add_news"),
    path("news/add_news_post", add_news_post, name="add_news_post"),
    path("branches", branches, name="branches"),
    path("branches/<int:branch_id>", branches_detail, name="branches_detail"),
    path("branches/add_branches", add_branches, name="add_branches"),
    path("branches/add_branches_post", add_branches_post, name="add_branches_post"),

]
