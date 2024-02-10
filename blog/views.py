from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BlogSearchView(ListView):
    model = Post
    template_name = 'blog/search.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list

class BlogPersonalView(ListView):
    model = Post
    template_name = 'blog/personal_account.html'