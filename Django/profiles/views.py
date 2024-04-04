from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm

def login(request):

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
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


    login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})



@login_required
def home(request):
    return render(request, 'home.html')


def logout(request):
    logout_user(request)
    return redirect('login')
