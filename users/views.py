from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.core.exceptions import ValidationError


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are now logged in"))
            return redirect('index')
        else:
            messages.error(request, ("Your username or password was incorrect, please try again"))
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out"))
    return redirect('index')


def signup_user(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                if Customer.objects.filter(username=username).exists():
                    raise ValidationError("This username is already registered, please try another.")
                else:
                    form.save()
                    user = authenticate(request, username=email, password=password)
                    login(request, user)
                    return redirect('index')
    else:
        form = RegisterForm()
        messages.error(request, "Something went wrong, please try again.")
        
    return render(request, 'signup.html', {'form':form})


def get_booktable(request):
    return render(request, 'booktable.html')


def get_base(request):
    return render(request, 'base.html')


def get_index(request):
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'signup.html')


def get_login(request):
    return render(request, 'login.html')


def error_404(request, exception):
    return render(request, '404.html')