from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as login_user, logout as logout_user, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, ChangePasswordForm
from .models import Profile, ProfileCourse
from apps.course.models import Course


def login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # User = get_user_model()
            # user = User.objects.get(user)
            user = authenticate(request, username=username, password=password)

            if user:
                login_user(request, user)
                return redirect('home')

    return render(request, 'profiles/login.html', {"login_form": form})


@login_required
def home(request):

    return render(request, 'profiles/home.html')


@login_required
def logout(request):
    logout_user(request)
    return redirect('main')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password_one')

            User = get_user_model()
            User.objects.create_user(username=username, password=password)
            user = authenticate(request, username=username, password=password)

            login_user(request, user)

            return redirect('home')

    return render(request, 'profiles/register.html', {"form": form})


@login_required
def change_password(request):
    form = ChangePasswordForm()

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            # достали пароль
            new_password = form.cleaned_data.get('password_one')

            # обновили пароль и сохранили
            request.user.set_password(new_password)
            request.user.save()

            # обновили сессию, чтобы больше нельзя было зайти под старым паролем
            update_session_auth_hash(request, request.user)

            return redirect('change_password_success')

    return render(request, 'profiles/change_password.html',  {"form": form})


@login_required
def change_password_success(request):
    return render(request, 'profiles/change_password_success.html')


def profile_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)


    if course not in request.user.profile.get_courses():
        raise Http404

    return render(request, 'profiles/profile_course.html', {"course": course})