from django.shortcuts import render
from django.http import HttpResponse
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

