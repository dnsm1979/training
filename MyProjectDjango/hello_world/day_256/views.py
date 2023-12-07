from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    now = datetime.datetime.now()

    year = now.year

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        day_256 = f"13/09/{year}"
    else:
        day_256 = f"12/09/{year}"
    return HttpResponse(day_256)
