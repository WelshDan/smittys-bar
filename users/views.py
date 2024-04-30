from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm
from django.contrib.core.exceptions import ValidationError


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
        return render(requesr, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('index')


def get_index(request):
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'signup.html')


def get_login(request):
    return render(request, 'login.html')


def logout_user(request):
    pass


def login_user(request):
    pass


def signup_user(request):
    pass