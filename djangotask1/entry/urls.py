
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_page),
    path('login', views.login_page),
    path('signup', views.signup_page),
]
