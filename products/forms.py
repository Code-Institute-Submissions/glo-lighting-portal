from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','image','material','mains','height','width','diameter','colour', 'fitting', 'bulb',
        'kelvin','cri','lumens','energy_label','art_No','transformer_included','product_type' ,'bruto_price' ,'miscellaneous']
        

  
        



   





   
   

    

    
