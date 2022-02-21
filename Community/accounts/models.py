from django.db import models


# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자이름')
    userid = models.CharField(max_length=64, verbose_name='아이디')
    password1 = models.CharField(max_length=64, verbose_name='비밀번호')
    password2 = models.CharField(max_length=64, verbose_name='비밀번호 확인')

    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'member_info'
