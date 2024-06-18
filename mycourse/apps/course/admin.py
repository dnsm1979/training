from django.contrib import admin
from . models import *

class LectureInline(admin.StackedInline):
    model = Lecture
    fields = ('title', 'description', 'stage')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureInline,]


class MaterialInLine(admin.StackedInline):
    model = Material
    fields = ('title', 'text', 'file','material_type','stage')


@admin.register(Lecture)

class CourseAdmin(admin.ModelAdmin):
    inlines = [MaterialInLine, ]
    list_filter = ('course__title',)





admin.site.register(Material)

