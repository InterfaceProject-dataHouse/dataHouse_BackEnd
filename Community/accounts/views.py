from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm  # 회원가입 정보를 얻어와서 저장할 때 사용
from django.contrib.auth.hashers import make_password, check_password  # 비밀번호 암호화 / 패스워드 체크

# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')

    elif request.method == "POST":
        # username = request.POST.get['username', None]
        # userid = request.POST.get['userid', None]
        # password1 = request.POST.get['password1', None]
        # password2 = request.POST.get['password2', None]
        #
        # res_data = {}
        # if not (username and userid and password1 and password2):
        #     res_data['error'] = "모든 값을 입력해야 합니다."
        # if password1 != password2:
        #     res_data['error'] = "비밀번호가 다릅니다."
        # else:
        #     user = Member(username=username, userid=userid, password=make_password(password1))
        #     user.save()
        # return render(request, 'accounts/register.html', res_data)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            userid = form.cleaned_data.get('userid')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(userid=userid, password=raw_password)
            login(request, user)
            return redirect('main:index')
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})



def login(request):
    return render(request, 'main/index.html')
