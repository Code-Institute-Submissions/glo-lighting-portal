from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import ProfileRegistrationForm

def signup_view(request):
    return render(request,"blog_accounts/signup.html")
    
    

