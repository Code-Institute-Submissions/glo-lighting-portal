from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('send_email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
]