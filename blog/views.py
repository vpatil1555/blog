from django.shortcuts import render
from .models import design  #import the class from models

# Create your views here.

# create a function to request from http
def index(request):
    
    types = design.objects.all()
    
    
    return render(request, "index.html",  {'types': types})


    
    

