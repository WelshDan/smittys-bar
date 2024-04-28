from django.shortcuts import render


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