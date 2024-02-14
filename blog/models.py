from django.db import models


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=250)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
