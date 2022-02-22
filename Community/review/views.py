from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def review1(request):
    return render(request, 'review/review1.html')

def review2(request):
    return render(request, 'review/review2.html')

def review3(request):
    return render(request, 'review/review3.html')

def review4(request):
    return render(request, 'review/review4.html')

def review5(request):
    return render(request, 'review/review5.html')