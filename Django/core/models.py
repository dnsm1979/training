from django.db import models

class Branch(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title
    

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    anons = models.CharField(max_length=250, verbose_name='Анонс')
    full_text = models.TextField(verbose_name='Статья')

    def __str__(self):
        return self.title

