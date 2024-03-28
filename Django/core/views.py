from django.shortcuts import render, redirect
from .models import Branch, News, Feedback
from .forms import BranchForm, NewsForm, FeedBackForm, FeedBackModelForm


def main(request):

    return render(request, "main.html")

def news(request):
    news = News.objects.all()
    return render(request, "news.html", {'news': news})

def news_detail(request, news_id):
    news = News.objects.get(id=news_id)
    context = {'news': news}
    return render(request, "news_detail.html", context)
def management(request):

    return render(request, "management.html")

def about(request):

    return render(request, "about.html")

def contacts(request):

    return render(request, "contacts.html")

def branches(request):
    branches = Branch.objects.all()
    return render(request, "branches.html", {'branches': branches})

# def add_branches(request):
#     return render(request, "add_branches.html")

# def add_news(request):
#     return render(request, "add_news.html")

def branches_add(request):
    branch_form = BranchForm

    if request.method == "POST":
        branch_form = BranchForm(request.POST)
        if branch_form.is_valid():
            title = branch_form.cleaned_data.get('title')
            text = branch_form.cleaned_data.get('text')
            Branch(title=title, text=text).save()
            # branch_form.save()
            return redirect("branches")
    #     title = request.POST.get('title')
    #     if len(title) > 10:
    #         text = request.POST.get('text')
    #         branch = Branch(title=title, text=text)
    #         branch.save()
    #         return redirect("branches")

    return render(request, "add_branches.html", {'branch_form': branch_form})

def add_news_post(request):
    news_form = NewsForm
    if request.method == "POST":
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            title = request.POST.get('title')
            anons = request.POST.get('anons')
            text = request.POST.get('text')
            news = News(title=title, anons=anons, text=text).save()
            return redirect("news")
    return render(request, "add_news.html", {'news_form': news_form})

def branches_detail(request, branch_id):


    branch = Branch.objects.get(id=branch_id)
    context = {'branch': branch}
    return render(request, "branches_detail.html", context)

def feedbacks_details(request, feedbacks_id):


    feedbacks = Feedback.objects.get(id=feedbacks_id)
    context = {'feedbacks': feedbacks}
    return render(request, "feedbacks_details.html", context)

# def feedbacks(request):
#     feedbacks = Feedback.objects.all()
#     return render(request, "feedbacks.html", {'feedbacks': feedbacks})

def feedbacks(request):

    if request.method == "POST":
        feedbacks_form = FeedBackModelForm(request.POST)
        feedbacks_form.save()
        # if feedbacks_form.is_valid():
        #     title = request.POST.get('title')
        #     if len(title) < 100:
        #         text = request.POST.get('text')
        #         if len(text) < 500:
        #             feedbacks = Feedback(title=title, text=text)
        #             feedbacks.save()
    feedbacks = Feedback.objects.all()
    feedbacks_form = FeedBackModelForm()
    return render(request, "feedbacks.html", {'feedbacks': feedbacks, 'feedbacks_form': feedbacks_form})

# def add_branchform(request):
#     branch_form = BranchForm

