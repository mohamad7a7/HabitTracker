from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm

''' define the rulse of register a user'''


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


'''define the rules of login a user'''


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


'''define the rules of log out a user'''


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('home')
