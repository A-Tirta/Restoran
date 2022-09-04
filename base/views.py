from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render
from .models import BookTable, ContactUs
from .forms import BookTableForm, ContactUsForm

# Create your views here.

def index(request):
  postBookTable = BookTableForm()
  postContactUs = ContactUsForm()

  if request.method == 'POST':
    print(request.POST)

  context = {
    'postBookTable' : postBookTable,
    'postContactUs' : postContactUs
  }

  return render(request, 'index.html', context)