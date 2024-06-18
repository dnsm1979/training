from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='media')
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_image_url(self):
        return self.image.url

    class Meta:
        ordering = ('title',)


class Lecture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, related_name='course_lectures', on_delete=models.CASCADE)
    stage = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Material(models.Model):
    class MaterialType(models.TextChoices):
        TEXT = 'text'
        IMG = 'image'
        VIDEO = 'video'
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='media', blank=True, null=True)
    material_type = models.CharField(choices=MaterialType, default=MaterialType.TEXT, max_length=10)
    lecture = models.ForeignKey(Lecture, related_name='lecture_materials', on_delete=models.CASCADE)
    stage = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('text',)
