from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_user, name="signup"),
]