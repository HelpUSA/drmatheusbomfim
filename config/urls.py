# File: config/urls.py
# Purpose:
# Root URL configuration for the Dr. Matheus Bomfim website.
from django.contrib import admin
from django.urls import path
from website.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
