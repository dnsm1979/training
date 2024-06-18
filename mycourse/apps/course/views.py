from django.shortcuts import render
from .models import Course

def main(request):

    courses = Course.objects.all()

    return render(request, 'main.html', {"courses": courses})
