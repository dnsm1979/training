from django.shortcuts import render, redirect

from apps.basket.models import Basket
from .models import Order

def preview(request):
    basket = request.basket
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        order = Order.objects.create(user=request.user, basket=basket, total_price=basket.get_total_price())

        basket.status = Basket.Status.CLOSE
        basket.save()

        request.session['order_id'] = order.id

        return redirect('checkout_success')

    return render(request, 'checkout/detail.html', {'basket':basket})

def success(request):
    return render(request, 'checkout/success.html')
