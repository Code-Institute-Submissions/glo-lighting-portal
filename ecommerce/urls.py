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
from checkout import urls as checkout_urls
from sendemail import urls as sendemail_urls
from articles import urls as articles_urls





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sendemail.urls')),
    path('', product_list, name='home'),
    path('checkout/', include(checkout_urls)),
    path('cart/', include(cart_urls)),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
    path('sendemail/', include(sendemail_urls)),
     path('articles/', include(articles_urls)),


    # path('blog_accounts/register/', register, name='register'),
    # path('blog_accounts/', include('django.contrib.auth.urls'),
    # path('', articals_list, name="home"),

    # path('blog_accounts/password-reset/', password_reset,
    #     {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    # path('blog_accounts/password-reset/done/', password_reset_done, name='password_reset_done'),
    # url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
    #     {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    # path('blog_accounts/password-reset/complete/', password_reset_complete, name='password_reset_complete'),

    # path('articles/<int:id>', post_detail, name="post_detail"),
    # path('articles/<int:id>/edit', edit_post, name="edit_article"),
    # path('articles/add', add_post, name="add_article"),
    # path('search', search_posts, name='search_article'),
    # path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('articles/<int:id>/like', like_post, name="like_article"),
    # path('articles/<int:id>/unlike', unlike_post, name="unlike_article"),

]

