from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def login_user(request):
    if request.method == "POST":
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in")
                return redirect('index')
            else:
                messages.error(request, "Your username or password was incorrect, please try again")

    else:
        return render(request, 'account_login.html', {})


def signup_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                messages.success(request, "You are now signed up!")
                return redirect('index')
    else:
        form = RegisterForm()
        
    return render(request, 'account_signup.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('index')


def get_booktable(request):
    return render(request, 'booktable.html')


def get_base(request):
    return render(request, 'base.html')


def get_index(request):
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'account_signup.html')


def get_login(request):
    return render(request, 'account_login.html')


def error_404(request, exception):
    return render(request, '404.html')