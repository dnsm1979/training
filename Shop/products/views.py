from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Products
from .models import Products
from .forms import ProductsForm


def products(request):

    products = Products.objects.all()


    order_by = request.GET.get('order_by', 'count')
    range = request.GET.get('range', 'desc')
    if order_by == 'count':
        products = products.order_by('quantity')
    elif order_by == 'price':
        products = products.order_by('price')

    if range == 'asc':
        products = products.reverse()

    page_number = request.GET.get('page', 1)
    p = Paginator(products, 2)
    page = p.page(page_number)
    products = page.object_list


    form = ProductsForm()

    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {"products": products, "form": form, "order_by": order_by, "range": range, "page": page}
    return render(request, 'products.html', context)

def products_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    context = {"product": product}
    return render(request, 'products_detail.html', context)

def products_edit(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    form = ProductsForm(instance=product)
    if request.method == "POST":
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_detail', product_id=product.id)

    context = {"product": product, "form": form}
    return render(request, 'products_edit.html', context)

def products_delete(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.delete()
    return redirect('products')