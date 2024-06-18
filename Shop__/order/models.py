from django.db import models

from products.models import Products
from sellers.models import Sellers
from client.models import Client


class Order(models.Model):
    seller = models.ForeignKey(Sellers, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Продавец')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='покупатель')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Товар')
    datatime = models.DateTimeField(verbose_name='Дата продажи')



    def __str__(self):
        return f'{self.seller} {self.client} {self.product} {self.datatime}'

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'