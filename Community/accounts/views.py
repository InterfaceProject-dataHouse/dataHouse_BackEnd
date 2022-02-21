from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm  # 회원가입 정보를 얻어와서 저장할 때 사용
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호 암호화 / 패스워드 체크
from django.urls import reverse

# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')

    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:index')
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})



# def login(request):
#     return render(request, 'main/index.html')