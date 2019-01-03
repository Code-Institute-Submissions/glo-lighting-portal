from django.urls import path
from .views import *



urlpatterns = [
    path('', bathrooms_list, name='bathrooms_list'),

    
  ]