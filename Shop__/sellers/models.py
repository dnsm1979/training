from django.db import models

class Positions(models.Model):
    position = models.CharField(primary_key=True, max_length=255, verbose_name='Позиция в фирме')

    def __str__(self):
        return f'{self.position}'

    class Meta:
        verbose_name = 'Позиция в фирме'
        verbose_name_plural = 'Позиции в фирме'

class Sellers(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    data_in = models.DateField(verbose_name='Дата приема на работу')
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'