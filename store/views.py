from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def product(request,pk):
    product = Product.objects.get(id = pk)  
    return render(request, 'product.html', {'product':product})

# Create your views here.
def home(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products':products});

def about(request):
	return render(request, 'about.html', {});

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.error(request, "Get an error!!! Please check again")
            return redirect('login')

    else: 
        return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You have logged out..."))
	return redirect('home')

def register_user(request):
    form = SignUpForm() 

    if request.method == "POST":
        form = SignUpForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            user = form.save()  # Save the user instance
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            # Authenticate the user after saving
            user = authenticate(username=username, password=password)  # Fixed the argument passing
            if user is not None:  # Check if authentication was successful
                login(request, user)  # Log the user in
                messages.success(request, "You have registered successfully.")
                return redirect('home')  # Redirect to home after registration
            else:
                messages.error(request, "Error during authentication. Please try again.")
                return redirect('register')
        else:
            messages.error(request, "Error: Please correct the errors in the form.")
            return render(request, 'register.html', {'form': form})  # Render form with errors for correction

    return render(request, 'register.html', {'form': form}) 





