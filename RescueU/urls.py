"""RescueU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.urls import path, reverse
import volunteers.views
import donors.views
import users.views

urlpatterns = [
    path('',users.views.home,name='home'),
    path('admin/', admin.site.urls),
    path('volunteer/', volunteers.views.index, name='index'),
    path('volunteer/register/', volunteers.views.register, name='register'),
    path('volunteer/list/', volunteers.views.list, name='list'),
    path('donors/',donors.views.index,name='index'),
    path('donors/donate/',donors.views.donate,name='donate'),
    path('users/signup/',users.views.signup,name='signup'),
    path('users/sos/',users.views.sos,name='sos'),
    url(r'^accounts/login/$',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('hospitals/',users.views.hospitals,name='hospitals')
#    url(r'^login/$',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
#   url(r'^logout/$',auth_views.LogoutView,{'next_page':'/volunteer'},name='logout'),
]