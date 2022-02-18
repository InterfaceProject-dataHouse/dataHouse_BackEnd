from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm  # 회원가입 정보를 얻어와서 저장할 때 사용

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')
