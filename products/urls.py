from django.urls import path
from .views import *
from accounts.views import *


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:id>/', product_detail, name='product_detail'),
    path('add',add_product, name='add_product'),
    path('edit/<int:id>', edit_product, name='edit_product'),
    path('filter/<str:type>', filter_by_product_type , name='filter'),
    path('', project_list, name='project_list'),
    path('', logo_brand, name='logo_brand'),

  ]