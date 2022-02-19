# Generated by Django 4.0.2 on 2022-02-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자이름')),
                ('userid', models.CharField(max_length=64, verbose_name='아이디')),
                ('password1', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('password2', models.CharField(max_length=64, verbose_name='비밀번호 확인')),
            ],
            options={
                'db_table': 'member_info',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]