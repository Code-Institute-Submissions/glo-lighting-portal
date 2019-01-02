from django.urls import path
from .views import *



urlpatterns = [
    path('', furniture_list, name='furniture_list'),
   
    
  ]