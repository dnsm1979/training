from django.shortcuts import render
from .models import Branch

def main(request):

    return render(request, "main.html")

def news(request):

    return render(request, "news.html")

def news_detail(request, news_id):
    news = Branch.objects.get(id=news_id)
    context = {'news': news}
    return render(request, "news_detail.html", context)


def management(request):

    return render(request, "management.html")

def about(request):

    return render(request, "about.html")

def contacts(request):

    return render(request, "contacts.html")

def branches(request):
    return render(request, "branches.html")

def branches_detail(request, branch_id):


    branch = Branch.objects.get(id=branch_id)
    context = {'branch': branch}
    return render(request, "branches_detail.html", context)

