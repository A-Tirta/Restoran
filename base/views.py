from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return render(request, 'index.html')

def menu(request):
  return render(request, 'menu.html')

def login(request):
  return render(request, 'login.html')