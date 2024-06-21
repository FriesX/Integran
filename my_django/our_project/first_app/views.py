from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . import forms
from django.contrib.auth.models import User
# Create your views here.
def index(request):
  return render(request,'integran/index.html')

def about(request):
  return render(request,'integran/about.html')

def signin(request):
  return render(request,'integran/signin.html')

def service(request):
  return render(request, 'integran/service.html')

def team(request):
  return render(request, 'integran/team.html')

def why(request):
  return render(request, 'integran/why.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request, user,password)
            return redirect('index')  
        else:
            error_message = 'Invalid username or password'
            return render(request, 'integran/signin.html', {'error_message': error_message})
    else:
        return render(request, 'integran/signin.html')
      
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and email and password:
            if User.objects.filter(username=username).exists():
                error_message = 'Username already exists'
                return render(request, 'integran/register.html', {'error_message': error_message})
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                if user is not None:
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        print(request, user, password)
                        return redirect('index')  
                    else:
                        error_message = 'Authentication failed'
                        return render(request, 'integran/register.html', {'error_message': error_message})
                else:
                    error_message = 'User creation failed'
                    return render(request, 'integran/register.html', {'error_message': error_message})
        else:
            error_message = 'Please fill in all the fields'
            return render(request, 'integran/register.html', {'error_message': error_message})
    else:
        return render(request, 'integran/register.html')