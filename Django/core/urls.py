from django.urls import path
from .views import *

urlpatterns = [
    path("", main, name="main"),
    path("about", about, name="about"),
    path("contacts", contacts, name="contacts"),
    path("management", management, name="management"),
    path("news", news, name="news"),
    path("news/<int:news_id>", news_detail, name="news_detail"),
    path("news/category/<int:category_id>", news, name="news_category"),
    path("branches", branches, name="branches"),
    path("branches/<int:branch_id>", branches_detail, name="branches_detail"),
    path("branches/country/<int:country_id>", branches, name="branches_country"),
    path("branches/add", branches_add, name="branches_add"),
    path("feedbacks", feedbacks, name="feedbacks"),
    path("feedbacks/<int:feedbacks_id>", feedbacks_details, name="feedbacks_details"),
]
