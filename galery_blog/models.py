from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
