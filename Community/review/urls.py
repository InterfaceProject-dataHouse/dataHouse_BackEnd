from django.urls import path, include
from . import views

app_name = 'review'

urlpatterns = [
    path('review1/', views.review1, name='review1'),
    path('review2/', views.review2, name='review2'),
    path('review3/', views.review3, name='review3'),
    path('review4/', views.review4, name='review4'),
    path('review5/', views.review5, name='review5'),
]


