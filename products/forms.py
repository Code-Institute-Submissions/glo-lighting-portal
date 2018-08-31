from .models import Lamp
from django import forms

class LampForm(forms.ModelForm):
    class Meta:
        model = Lamp
        fields=['name','image','fitting','material','mains','height','width','diameter','colour','art_No','transformer_included','lamp_type' ,'bruto_price' ,'miscellaneous']
        


        
        
   





   
   

    

    
