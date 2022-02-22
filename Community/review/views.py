from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def review1(request):
    return render(request, 'main/review1.html')

def review2(request):
    return render(request, 'main/review2.html')

def review3(request):
    return render(request, 'main/review3.html')

def review4(request):
    return render(request, 'main/review4.html')