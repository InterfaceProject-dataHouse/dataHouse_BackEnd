# 장고가 제공하는 auth db를 사용하기 위해서는 auth form 기능을 사용하면 편리하다
# auth form을 사용하기 위해서는 일반 forms 모듈을 import 해야 함
from django import forms
# 개발자가 직접 auth form을 수정할 것이기 때문에 UserCreationForm 모듈도 필요함
from django.contrib.auth.forms import UserCreationForm
# auth db 중 사용자 계정으 담당하는 model인 User 클래스도 필요 (User table)
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")  # 이메일은 EmailField로 수정하여 형식체크 기능 사용

    class Meta :  # 기존에 장고에서 제공하는 User모델(table)을 그대로 사용
        model = User  # username, email, password
        fields = ("username", "password1", "password2", "email")