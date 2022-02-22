from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.


def main_ind(request):
    return render(request, 'main/index.html')

def artHouse(request):
    return render(request, 'main/artHouse.html')

def review1(request):
    return render(request, 'main/review1.html')

def review2(request):
    return render(request, 'main/review2.html')

def review3(request):
    return render(request, 'main/review3.html')

def review4(request):
    return render(request, 'main/review4.html')

def reviewPage(request):
    # return render(request, 'main/reviewPage.html')
    reviews = Review.objects.all()
    review_cont = {'reviews' : reviews}

    return render(request, 'main/reviewPage.html', review_cont)

def createTodo(request):
    input_str = request.POST['todoContent']
    new_memo = Review(content=input_str)
    new_memo.save()
    return HttpResponseRedirect(reverse('main:reviewPage'))