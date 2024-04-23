from django.shortcuts import render, redirect

from .models import Client
from .forms import ClientForm


def client(request):

    clients = Client.objects.all()
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    context = {"clients": clients, "form": form}
    return render(request, 'client.html', context)
