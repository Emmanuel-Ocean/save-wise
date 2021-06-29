from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
  if request.method == 'POST':
    Savenow.objects.create(
      name=request.POST['name'],
      amount=request.POST['amount'],
      purpose=request.POST['purpose'],
      saved_at=request.POST['saved_at'],
      )
  context = {}
  return render(request, 'index.html', context)

def myplan(request):
  context = {

  }
  return render(request,'myplan.html',context)