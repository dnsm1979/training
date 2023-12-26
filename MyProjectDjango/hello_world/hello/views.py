from django.http import HttpResponse
from datetime import datetime


def index(request):
    current_datetime = datetime.now()
    return HttpResponse(current_datetime)
