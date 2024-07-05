from django.contrib import admin
from . models import *



class LectureInline(admin.StackedInline):
    model = Lecture
    fields = ('title', 'description', 'stage')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [
        LectureInline,
    ]


class MaterialInline(admin.StackedInline):
    model = Material
    fields = ('title', 'text', 'file', 'material_type', 'stage')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    inlines = [
        MaterialInline,
    ]
    list_filter = ('course__title',)


admin.site.register(Material)
admin.site.register(Category)
