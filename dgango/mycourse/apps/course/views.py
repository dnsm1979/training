from django.shortcuts import render, get_object_or_404

from .models import Course, Category
from ..basket.models import Basket


def main(request):

    courses = Course.objects.all()
    categories = Category.objects.all()

    return render(request, 'main.html', {"courses": courses, "categories": categories})

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)


    return render(request, 'category/detail.html', {"active_category": category})

def course(request, course_id):

    course = get_object_or_404(Course, id=course_id)
    basket = request.basket


    return render(request, 'course/detail.html', {"course": course, "basket":basket})