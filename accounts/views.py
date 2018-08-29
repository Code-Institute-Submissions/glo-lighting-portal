from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import BrandRegistrationForm


def register(request):
    if request.method == 'POST':
        # Load the HTTP Request into two forms, for the User, and the Profile
        user_form = UserCreationForm(request.POST)
        brand_form = BrandRegistrationForm(request.POST, request.FILES)
        

        # If both forms are valid, we create the User and Profile in the Database
        if user_form.is_valid() and brand_form.is_valid():
            # Save the User object to DB, by calling save directly on the Form.
            # Return the User object so that we can use it later to set the user of the Profile.
            user = user_form.save()

            brand = brand_form.save(commit=False)
            brand.user = user
            brand.save()
            
            # Now we can log in as the new user 
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        user_form = UserCreationForm()
        brand_form = BrandRegistrationForm()
    return render(request, 'accounts/register.html', { 'user_form': user_form, 'brand_form': brand_form })