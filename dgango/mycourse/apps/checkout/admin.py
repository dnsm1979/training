from django.contrib import admin
from .models import *
from apps.profiles.models import ProfileCourse


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total_price", "created_date", "status")
    actions = ["add_course"]

    @admin.action(description="Добавить курсы из заказа")
    def add_course(self, request, queryset):
        for order in queryset:
            for line in order.basket.basket_lines.all():
                course = line.course
                ProfileCourse.objects.create(course=course, profile=order.user.profile)
                order.status = Order.Status.COMPLITE
                order.save()
