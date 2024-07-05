from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Basket, Line
from apps.course.models import Course


def basket_add(request, course_id):
    user = request.user

    if request.method == "POST":
        course = get_object_or_404(Course, id=course_id)

        # получение или создание корзины
        basket = request.basket
        if not basket:
            basket = Basket.objects.create(owner=user)

        Line.objects.create(basket=basket, course=course, price=course.price)

        return redirect("basket_detail")


def basket_detail(request):
    user = request.user
    basket = request.basket

    return render(request, "basket/detail.html", {"basket": basket})


def basket_remove(request, line_id):
    user = request.user

    if request.method == "POST":

        # получение или создание корзины
        basket = request.basket
        basket.basket_lines.filter(id=line_id).delete()

        return redirect("basket_detail")
