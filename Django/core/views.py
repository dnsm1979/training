from django.shortcuts import render, redirect
from .models import Branch

def main(request):

    return render(request, "main.html")

def news(request):

    return render(request, "news.html")

def management(request):

    return render(request, "management.html")

def about(request):

    return render(request, "about.html")

def contacts(request):

    return render(request, "contacts.html")

def branches(request):
    branches = Branch.objects.all()
    return render(request, "branches.html", {'branches': branches})

def add_branches(request):
    return render(request, "add_branches.html")

def add_branches_post(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    branch = Branch(title=title, text=text)
    branch.save()
    return redirect("branches")

def branches_detail(request, branch_id):


    branch = Branch.objects.get(id=branch_id)
    context = {'branch': branch}
    return render(request, "branches_detail.html", context)

