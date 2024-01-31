from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm
from django.views.generic import DetailView


def news_home(request):
    news = Articles.objects.all()
    return render(request, "news/news_home.html", {"news": news})


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")

    form = ArticleForm()
    data = {"form": form}
    return render(request, "news/create.html", data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/details_view.html"
    context_object_name = "article"
