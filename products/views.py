from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html" , {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product_detail.html" , {'product': product})
    
    
def add_product(request):
    return render(request, "products/product_form.html")
    

    
def add_product(request):
    if request.method=="POST":
        
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.brand = request.user.brand
            product.save()
            return redirect("product_list")
            
    else:
        form = ProductForm()
            
    
    return render(request, "products/product_form.html", {'form': form})
    
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if request.method=="POST":
         form = ProductForm(request.POST, request.FILES, instance=product)
         if form.is_valid():
             form.save()
             return redirect("product_detail", id=id)
    else:
        form = ProductForm(instance=product)
    
    return render(request, "products/product_form.html", {'form': form})
