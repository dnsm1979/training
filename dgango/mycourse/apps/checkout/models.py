from django.db import models

from apps.basket.models import Basket
from apps.profiles.models import User


class Order(models.Model):
    class Status(models.TextChoices):
        WAITING = "waiting"
        COMPLITE = "complete"

    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status, default=Status.WAITING, max_length=20)
