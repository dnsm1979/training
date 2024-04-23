from django.contrib.auth import authenticate, login as login_user, logout as logout_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrForm, SetPasswordForm
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
            login_user(request, user)
            return redirect('main')


    return render(request, 'register.html', {'form': form})


def set_password(request):
    from django.contrib.auth.models import User
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            password_old = request.POST.get("password_old")
            password_new = request.POST.get("password_new")
            password_re = request.POST.get("password_re")
            if check_password(password_old, user.password):
                user.set_password(user.password_new)
                user.save()
                return redirect(request, 'password_change_done.html')
            else:
                return redirect(request, 'set_password.html')
    else:
        form = SetPasswordForm()

    return render(request, 'set_password.html',
                  {'form': form, 'user': user})

def password_change_done(request):
    return render(request, 'password_change_done.html')

