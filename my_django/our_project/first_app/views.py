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
            # Authentication successful
            login(request, user)
            print(request, user,password)
            return redirect('index')  # Redirect to the home page or any other success page
        else:
            # Authentication failed
            error_message = 'Invalid username or password'
            return render(request, 'integran/signin.html', {'error_message': error_message})
    else:
        # Render the signin template if the request method is GET
        return render(request, 'integran/signin.html')
      
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and email and password:
            # Check if a user with the same username already exists
            if User.objects.filter(username=username).exists():
                error_message = 'Username already exists'
                return render(request, 'integran/register.html', {'error_message': error_message})
            else:
                # Create a new user
                user = User.objects.create_user(username=username, email=email, password=password)
                if user is not None:
                    # Authenticate the new user
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        # Authentication successful
                        login(request, user)
                        print(request, user, password)
                        return redirect('index')  # Redirect to the home page or any other success page
                    else:
                        # Authentication failed
                        error_message = 'Authentication failed'
                        return render(request, 'integran/register.html', {'error_message': error_message})
                else:
                    # User creation failed
                    error_message = 'User creation failed'
                    return render(request, 'integran/register.html', {'error_message': error_message})
        else:
            # Missing form data
            error_message = 'Please fill in all the fields'
            return render(request, 'integran/register.html', {'error_message': error_message})
    else:
        # Render the register template if the request method is GET
        return render(request, 'integran/register.html')