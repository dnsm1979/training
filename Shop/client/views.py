from django.shortcuts import render, redirect, get_object_or_404

from .models import Client
from .forms import ClientForm
from django.core.paginator import Paginator


def client(request):

    clients = Client.objects.all()

    order_by = request.GET.get('order_by', 's_name')
    range = request.GET.get('range', 'desc')
    if order_by == 'name':
        clients = clients.order_by('first_name')
    elif order_by == 's_name':
        clients = clients.order_by('last_name')

    if range == 'asc':
        clients = clients.reverse()

    page_number = request.GET.get('page', 1)
    p = Paginator(clients, 2)
    page = p.page(page_number)
    clients = page.object_list

    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    context = {"clients": clients, "form": form, "order_by": order_by, "range": range, "page": page}
    return render(request, 'client.html', context)

def edit_client(request, pk):
    # clients = Client.objects.all()
    clients = Client.objects.get(pk=pk)
    # form = ClientForm(request.POST, request.FILES)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=clients)
        if form.is_valid():
            # obj = form.save(commit=False)
            # obj.client = Client.objects.get(id=pk)

            form.save()
            return redirect('client')
    else:
        form = ClientForm(instance=clients)

    context = {"clients": clients, "form": form}

    return render(request, 'edit_client.html', context)


def delete_client(request, pk):
    clients = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        clients.delete()
        return redirect('client')

    context = {"clients": clients}
    return render(request, 'delete_client.html', context)

