from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def main_ind(request):
    return render(request, 'main/index.html')

def artHouse(request):
    return render(request, 'main/artHouse.html')

