from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        if username is None or password is None:
            return
        try:
            User = get_user_model()
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return
        if user.check_password(password):
            return user

