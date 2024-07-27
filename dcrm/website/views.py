from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Customers

def home(request):
    # Check to see if user is logged in
    
    customers = Customers.objects.all()
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("home")
        else:
            messages.success(request, "Wrong username or password, try again!")
            return redirect("home")
    else:
        return render(request, 'home.html', {'customers':customers})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auth and login
            password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer = Customers.objects.get(id=pk)
        return render(request, 'customer.html', {'customer':customer})
    else:
        messages.success(request, "You must be logged in to view this page!")
        return redirect('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_it = Customers.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Customer has been deleted!")
        return redirect('home')
    else:
        return redirect('home')