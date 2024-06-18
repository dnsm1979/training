from django.shortcuts import render, redirect

from .models import Order
from .forms import OrderForm


def order(request):

    order = Order.objects.all()
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
    context = {"order": order, "form": form}
    return render(request, 'order.html', context)