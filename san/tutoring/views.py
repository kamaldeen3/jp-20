from django.shortcuts import render, HttpResponse, redirect
from django.contrib import admin, messages
from django.urls import path
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'tutoring/home.html')

def services(request):
    return render(request, 'tutoring/services.html')

def profile(request):
    return render(request, 'tutoring/profile.html')

def about(request):
    return render(request, 'tutoring/about.html')

def login_users(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'tutoring/login.html')

def logout_users(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def register_users(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created!')
    context = {'page': page, 'form': form}
    return render(request, 'tutoring/login.html', context)