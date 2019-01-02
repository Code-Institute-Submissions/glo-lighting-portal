from django.shortcuts import render


# Create your views here.

   
def bathrooms_list(request):
    # bathrooms = Product.bathrooms()
    return render(request, "bathrooms/bathroom_list.html")   