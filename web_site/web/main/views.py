from django.shortcuts import render


def index(request):
    data = {
        "title": "Главная страница",
        "values": ["hi", "world", "cars"],
        "car": {"car": "bmw", "model": "m5", "power": "600"},
    }
    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html")


def contacts(request):
    return render(request, "main/contacts.html")
