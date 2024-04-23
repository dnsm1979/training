from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    text = models.CharField(max_length=255, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.title} {self.price} {self.quantity}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
