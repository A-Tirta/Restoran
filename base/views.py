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

  formBookTable = BookTableForm(request.POST or None)
  formContactUs = ContactUsForm(request.POST or None)

  context = {
    'postBookTable' : postBookTable,
    'postContactUs' : postContactUs,
    'formBookTable' : formBookTable,
    'formContactUs' : formContactUs
  }
  
  if 'BookTable' in request.POST:
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

  if 'ContactUs' in request.POST:
    ContactUs.objects.create(
    CUName = request.POST["CUName"],
    CUEmail = request.POST["CUEmail"],
    CUSubject = request.POST["CUSubject"],
    CUMessage = request.POST["CUMessage"]
  )
    return HttpResponseRedirect("/home/")

  return render(request, 'index.html', context)