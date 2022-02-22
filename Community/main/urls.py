from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_ind, name='index'),
    path('artHouse/', views.artHouse, name='artHouse'),
    path('review1/', views.review1, name='review1'),
    path('review2/', views.review2, name='review2'),
    path('review3/', views.review3, name='review3'),
    path('review4/', views.review4, name='review4'),
    path('reviewPage/', views.reviewPage, name='reviewPage'),
    path('reviewPage/createTodo/', views.createTodo, name='createTodo')
]