from django.urls import path, include
from .views import BlogListView, BlogDetailView, BlogSearchView, BlogPersonalView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("search/", BlogSearchView.as_view(), name="search"),
    path("", BlogListView.as_view(), name="home"),
    path("personal_account/", BlogPersonalView.as_view(), name="personal_account"),

    ]