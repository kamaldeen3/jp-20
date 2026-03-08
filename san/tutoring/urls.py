from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('login/', views.login_users, name='login'),
    path('logout/', views.logout_users, name='logout'),
    path('register/', views.register_users, name='register'),
]