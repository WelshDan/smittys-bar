"""
URL configuration for smittys_bar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookings import views as bookings_views
from users import views
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('base/', views.get_base, name='base'),
    path('booktable/', bookings_views.reserve_table, name='booktable'),
    path('bookings/', include('bookings.urls')),
    path('users/', include('users.urls')),
]

handler404 = 'users.views.error_404'

# Admin titles and headings"
admin.site.index_title = "Smitty's Bar & Restaurant"
admin.site.site_header = "Smitty's Bar & Restaurant Admin"
admin.site.site_title = "Smitty's Bar & Restaurant Admin"

admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)