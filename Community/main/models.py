from django.db import models

# Create your models here.
class Review(models.Model):
    content = models.CharField(max_length=255)

class Catereview(models.Model):
    cate_id= models.CharField(max_length=25)
    content= models.CharField(max_length=255)