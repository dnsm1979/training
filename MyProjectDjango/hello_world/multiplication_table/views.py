from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    tabl = "".join(
        ["".join([f"{x*y}\t" for x in range(1, 11)]) + "\n" for y in range(1, 11)]
    )
    return render(request, "index.html", context=tabl)
