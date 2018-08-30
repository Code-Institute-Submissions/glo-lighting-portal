from .models import Brand
from django import forms

class BrandRegistrationForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields=['name','logo']
        
        
        
    
    





   
   

   

  
        
        
        
