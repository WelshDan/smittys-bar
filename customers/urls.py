from django.urls import path
from . import views


urlpatterns = [
    path('account_login/', views.login_user, name="login"),
    path('account_logout/', views.logout_user, name="logout"),
    path('account_signup/', views.signup_user, name="signup"),
]