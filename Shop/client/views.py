from django.shortcuts import render, redirect, get_object_or_404

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

def edit_client(request, pk):
    clients = Client.objects.all()
    sluz = get_object_or_404(Client, pk=pk)
    # form = ClientForm(request.POST, request.FILES)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=sluz)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.client = Client.objects.get(id=pk)

            obj.save()
            return redirect('client')
    context = {"clients": clients, "form": form}
    return render(request, 'edit_client.html', context)

