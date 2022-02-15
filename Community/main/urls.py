from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_ind, name='index'),
    path('artHouse.html/', views.artHouse, name='artHouse'),
]