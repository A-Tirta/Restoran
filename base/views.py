from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render
from .models import BookTable
from .forms import BookTableForm

# Create your views here.

def index(request):
  postBookTable = BookTableForm()

  if request.method == 'POST':
    print(request.POST)

  context = {
    'postBookTable' : postBookTable
  }

  return render(request, 'index.html', context)