
from django.shortcuts import render
from products.models import Product


# Create your models here.

def do_search(request):
    # search = Products.object.filter(name__icontains=request.GET[''])
    return render(request, "../products.html", {"products", products})