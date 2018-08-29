from django.shortcuts import render, get_object_or_404
from .models import Lamp


# Create your views here.
def product_list(request):
    products = Lamp.objects.all()
    return render(request, "products/product_list.html" , {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Lamp, pk=id)
    return render(request, "products/product_detail.html" , {'product': product})
    
