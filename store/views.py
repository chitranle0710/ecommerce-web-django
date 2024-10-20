from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm
from django import forms

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "User Has Been Updated!!")
            return redirect('home')
        return render(request, "update_user.html", {'user_form':user_form})
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('home')


def category(request, foo):
    foo = foo.replace('-',' ')
    try:
        category = Category.objects.get(name = foo)
        products = Product.objects.filter(category = category)
        return render(request, 'category.html',{'products':products,'category': category})
    except:
        messages.error(request, "That's category does not exist")
        return redirect('home')


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


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        # Did they fill out the form
        if request.method  == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            # Is the form valid
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password Has Been Updated...")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')


