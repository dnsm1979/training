from django.contrib.auth import authenticate, login as login_user, logout as logout_user, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrForm, ChangePasswordForm
from .models import Profile
from django.contrib.auth.hashers import check_password


def login(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            # User = get_user_model()
            # user = User.objects.get(user)

            user = authenticate(username=username, password=password)
            if user:
                login_user(request, user)
                return redirect('home')


        #         login(request, user)
        #         return redirect('home')
        #     else:
        #         return render(request, 'login.html', {'login_form': login_form})
        # else:
        #     return render(request, 'login.html', {'login_form': login_form})



    return render(request, 'login.html', {'login_form': login_form})



@login_required
def home(request):
    return render(request, 'home.html')


def logout(request):
    logout_user(request)
    return redirect('login')


def register(request):

    form = RegistrForm()
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User = get_user_model()
            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user)
            login_user(request, user, 'profiles.auth.email_backend.EmailBackend')
            return redirect('main')


    return render(request, 'register.html', {'form': form})

@login_required
def change_password(request):
    form = ChangePasswordForm()

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            password_new = form.cleaned_data.get('password_new')
            request.user.set_password(password_new)
            request.user.save()
            update_session_auth_hash(request, request.user)
            return redirect('password_change_done')

    return render(request, 'change_password.html', {'form': form})


@login_required
def password_change_done(request):
    return render(request, 'password_change_done.html')

