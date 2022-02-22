from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_ind, name='index'),
    path('artHouse/', views.artHouse, name='artHouse'),
    path('reviewPage/', views.reviewPage, name='reviewPage'),
    path('reviewPage/createTodo/', views.createTodo, name='createTodo')
]