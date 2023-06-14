from django.contrib import admin
from django.urls import path, include
from .views import AboutPageView

urlpatterns = [
    path('', AboutPageView),
]