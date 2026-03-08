from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tutoring/home.html')

def services(request):
    return render(request, 'tutoring/services.html')