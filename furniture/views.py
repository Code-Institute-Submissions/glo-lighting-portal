from django.shortcuts import render


# Create your views here.

   
def furniture_list(request):
    # furniture = Furniture.furniture()
    return render(request, "furniture/furniture_list.html")   