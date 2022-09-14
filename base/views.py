from ast import If
from http.client import HTTPResponse
from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render
from .models import BookTable, ContactUs
from .forms import BookTableForm, ContactUsForm
from django.http import HttpResponseRedirect
from django.contrib import auth

# Create your views here.

def index(request):
  postContactUs = ContactUsForm()
  postBookTable = BookTableForm()

  context = {
    'postBookTable' : postBookTable,
    'postContactUs' : postContactUs
  }

  if request.method == 'POST':
    BookTable.objects.create(
    Name = request.POST["Name"],
    Email = request.POST["Email"],
    Phone = request.POST["Phone"],
    Date = request.POST["Date"],
    Time = request.POST["Time"],
    ManyPeople = request.POST["ManyPeople"],
    Message = request.POST["Message"]
  )

    return HttpResponseRedirect("/home/")

  return render(request, 'index.html', context)