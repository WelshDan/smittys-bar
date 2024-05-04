from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm
from django.core.exceptions import ValidationError


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                raise ValidationError("Your email or password was incorrect, please try again.")
        except ValidationError as e:
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('index')


def signup_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if CustomUser.objects.filter(email=email).exists():
                raise ValidationError("This email address is already registered, please try another.")
            else:
                form.save()
                password = form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                login(request, user)
                return redirect('index')
    else:
        form = RegisterForm()
        
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