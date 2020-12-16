from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(request, username = name, password =password)
        if user is not None:
            login(request,user)
            return redirect('service')
        else:
            messages.error(request,'Username or password Invalid!')
        
    
    return render(request,'authentication/login.html')

def authregistration(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("login")
    else:
	    form = RegisterForm()

    return render(response, "authentication/registration.html", {"form":form})

def authforgotpassword(request):
    
    return render(request,'authentication/forgot.html')

def userlogout(request):
    
    logout(request)
    messages.success(request,'successfully logout!')
    return redirect('login')


