from django.urls import path
from .views import product_list, product_detail, add_product, edit_product


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:id>/', product_detail, name='product_detail'),
    path('add',add_product, name='add_product'),
    path('edit/<int:id>', edit_product, name='edit_product'),

  ]