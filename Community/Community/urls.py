from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('review/', include('review.urls'), name='review'),
    path('admin/', admin.site.urls),
]
