from apps.course.models import Category


def course_categories(request):
    categories = Category.objects.all()
    return {"categories": categories}
