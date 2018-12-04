from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import ProfileRegistrationForm

def signup_view(request):
    # this will create a standard django signin form and validate it.
    #then if it is valid it will be sent to db
    if request.method == "POST":
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
        # log user in
        return redirect("articles:list")
        
    else:
        form = UserCreationForm()
        
    return render(request,"blog_accounts/signup.html", {"form":form})
    
    

