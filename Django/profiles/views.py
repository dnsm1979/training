from django.contrib.auth import authenticate, login as login_user, logout as logout_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrForm, ChangePasswordForm
from .models import Profile


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
    u = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = request.POST.get("old_password")
            new_pass = request.POST.get("new_password")
            new_pass_rep = request.POST.get("new_password_repeat")
            if check_password(old_password, u.password):
                return HttpResponse('ok')
            else:
                return HttpResponse('bad')
    else:
        form = ChangePasswordForm()

    return render(request, 'login/set_password.html',
                  {'form': form, 'user': u})

