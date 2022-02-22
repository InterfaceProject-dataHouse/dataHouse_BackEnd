from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.


def main_ind(request):
    return render(request, 'main/index.html')

def artHouse(request):
    return render(request, 'main/artHouse.html')


def review(request):
    # return render(request, 'main/reviewPage.html')
    reviews = Review.objects.all()
    content = {'reviews' : reviews}

    return render(request, 'main/reviewPage.html', content)

def reviewPage(request, res_id):
    # return render(request, 'main/reviewPage.html')
    reviews = Catereview.objects.filter(cate_id=res_id)
    content = {'reviews' : reviews, 'res_id': res_id}

    return render(request, 'main/reviewPage.html', content)

def createTodo(request):
    res_id = request.POST['cateid']
    input_str = request.POST['todoContent']
    print(input_str)
    new_review = Catereview(cate_id = res_id, content = input_str)
    new_review.save()
    return HttpResponseRedirect(reverse('main:reviewPage', kwargs= {'res_id':res_id}))