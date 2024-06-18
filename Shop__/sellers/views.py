from django.shortcuts import render, redirect

from .models import Sellers
from .forms import SellersForm


def sellers(request):

    sellers = Sellers.objects.all()
    form = SellersForm()
    if request.method == "POST":
        form = SellersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sellers')
    context = {"sellers": sellers, "form": form}
    return render(request, 'sellers.html', context)
