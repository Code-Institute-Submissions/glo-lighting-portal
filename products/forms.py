from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','image','fitting','material','mains','height','width','diameter','colour','art_No','transformer_included','product_type' ,'bruto_price' ,'miscellaneous']
        


        
        
   





   
   

    

    
