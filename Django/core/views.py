from django.shortcuts import render, redirect, get_object_or_404
from .models import Branch, News, Feedback, Countries, NewsCategory
from .forms import BranchForm, NewsForm, FeedBackForm, FeedBackModelForm, NewsModelForm


def main(request):
    return render(request, "main.html")


def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    context = {"news": news}
    return render(request, "news_detail.html", context)


def management(request):
    return render(request, "management.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    return render(request, "contacts.html")


def branches(request, country_id=None):
    context = {}
    branches = Branch.objects.all()
    countries = Countries.objects.all()
    branch_form = BranchForm

    if request.method == "POST":
        branch_form = BranchForm(request.POST)
        if branch_form.is_valid():
            title = branch_form.cleaned_data.get("title")
            text = branch_form.cleaned_data.get("text")
            country_title = branch_form.cleaned_data.get("country")
            country = Countries.objects.get(title=country_title)
            Branch(title=title, text=text, country=country).save()
            return redirect("branches")

    if country_id:
        country = get_object_or_404(Countries, id=country_id)
        branches = Branch.objects.filter(country=country)
        context.update({"active_country": country})

    context.update({"branches": branches, "countries": countries, "branch_form": branch_form})
    return render(
        request, "branches.html", context
    )


def branches_add(request):
    branch_form = BranchForm

    if request.method == "POST":
        branch_form = BranchForm(request.POST)
        if branch_form.is_valid():
            title = branch_form.cleaned_data.get("title")
            text = branch_form.cleaned_data.get("text")
            country_title = branch_form.cleaned_data.get("country")
            country = Countries.objects.get(title=country_title)
            Branch(title=title, text=text, country=country).save()
            return redirect("branches")


    return render(request, "add_branches.html", {"branch_form": branch_form})


def news(request, category_id=None):
    news_form = NewsForm
    context = {}
    news = News.objects.all()
    categoris = NewsCategory.objects.all()

    if request.method == "POST":
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            title = news_form.cleaned_data.get("title")
            text = news_form.cleaned_data.get("text")
            anons = news_form.cleaned_data.get("anons")
            category_title = news_form.cleaned_data.get("category")
            category_sel = NewsCategory.objects.get(title=category_title)
            News(title=title, text=text, anons=anons, category=category_sel).save()
            return redirect("news")

    if category_id:
        category = get_object_or_404(NewsCategory, id=category_id)
        news = News.objects.filter(category=category)
        context.update({"active_category": category})

    context.update({"news": news, "categoris": categoris, "news_form": news_form})

    return render(request, "news.html", context)


def branches_detail(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    context = {"branch": branch}
    return render(request, "branches_detail.html", context)

from django.views.generic.detail import DetailView
class BranchesDetail(DetailView):
    model = Branch
    template_name = "branches_detail.html"
    pk_url_kwarg = 'branch_id'

def feedbacks_details(request, feedbacks_id):
    feedbacks = Feedback.objects.get(id=feedbacks_id)
    context = {"feedbacks": feedbacks}
    return render(request, "feedbacks_details.html", context)

class FeedBackDetail(DetailView):
    model = Feedback
    template_name = "feedbacks_details.html"
    pk_url_kwarg = 'feedbacks_id'


def feedbacks(request):
    if request.method == "POST":
        feedbacks_form = FeedBackModelForm(request.POST)
        feedbacks_form.save()

    feedbacks = Feedback.objects.all()
    feedbacks_form = FeedBackModelForm()
    return render(
        request,
        "feedbacks.html",
        {"feedbacks": feedbacks, "feedbacks_form": feedbacks_form}
    )
