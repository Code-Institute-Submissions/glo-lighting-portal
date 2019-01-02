"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from accounts import urls as accounts_urls
from products import urls as products_urls
from products.views import product_list
from cart import urls as cart_urls
from search import urls as search_urls
from checkout import urls as checkout_urls
from sendemail import urls as sendemail_urls
from articles import urls as articles_urls
from bathrooms import urls as bathrooms_urls
from furniture import urls as furniture_urls






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sendemail.urls')),
    path('', product_list, name='home'),
    path('checkout/', include(checkout_urls)),
    path('cart/', include(cart_urls)),
    path('search/', include(search_urls)),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
    path('sendemail/', include(sendemail_urls)),
    path('articles/', include(articles_urls)),
    path('bathrooms/',include(bathrooms_urls)),
    path('furniture/',include(furniture_urls)),


   

]

