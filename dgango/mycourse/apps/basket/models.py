from django.db import models
from apps.profiles.models import User
from apps.course.models import Course


class Basket(models.Model):
    class Status(models.TextChoices):
        OPEN = 'open'
        CLOSE = 'close'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='baskets', null=True, blank=True)
    status = models.CharField(choices=Status, default=Status.OPEN, max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        price = 0
        for line in self.basket_lines.all():
            price += line.course.price
        return price

    def get_course_id(self):
        course_ids = []
        for line in self.basket_lines.all():
            course_ids.append(line.course.id)
        return course_ids



class Line(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_lines')
