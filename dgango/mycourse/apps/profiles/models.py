from django.db import models

from django.contrib.auth.models import User
from apps.course.models import Course


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def get_courses(self):
        profile_courses = self.profile_courses.all()
        return [profile_course.course for profile_course in profile_courses]


class ProfileCourse(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_courses"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
