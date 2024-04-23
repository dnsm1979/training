from django.shortcuts import render, redirect

from .models import Products
from .forms import ProductsForm


def products(request):

    products = Products.objects.all()
    form = ProductsForm()
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {"products": products, "form": form}
    return render(request, 'products.html', context)