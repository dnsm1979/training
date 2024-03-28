from django.db import models


class Countries(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", blank=True)

    def __str__(self):
        return self.title


class Branch(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True)
    text = models.TextField(verbose_name="описание")
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    anons = models.CharField(max_length=255, verbose_name="Анонс")
    text = models.TextField(verbose_name="Текст новости")

    def __str__(self):
        return self.title


class Feedback(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    text = models.TextField(verbose_name="описание")

    def __str__(self):
        return self.title
