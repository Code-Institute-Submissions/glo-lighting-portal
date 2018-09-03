from django.db import models
from accounts.models import Brand
# Create your models here.
MATERIAL_CHOICES = (
    	('X', 'choose material'),
    	('metal sprayed copper', 'metal sprayed copper'),	
    	('metal sprayed silver', 'metal sprayed silver'),
    	('metal','metal'),
    	('aluminium', 'aluminium'),
    	('copper', 'copper'),
    	('vineer', 'vineer')
    )   ('fibreglass','fibreglass')
    
LAMP_TYPE_CHOICES = (
    	('X', 'choose type'),
    	('suspension', 'suspension'),	
    	('floor', 'floor'),
    	('table', 'table'),
    	('wall/ceiling', 'wall/ceiling'),
    	('outside', 'outside'),
    )    

FITTING_CHOICES = (
    ( 'E27', 'E27'),
    ( 'E16', '16' ),
    ( 'GU10', 'GU10'),
    ( 'LED built in', 'LED built in')
    
    
    )
    
    
COLOUR_CHOICE = (
     ( 'black','white','grey','red', 'yellow')   
    )    


class Lamp(models.Model):
    image = models.ImageField(upload_to="images" , null=True, blank=True)
    name= models.CharField(max_length=40, blank=False, null=False)
    fitting= models.CharField(max_length=40, blank=True, null=True, default='X', choices=FITTING_CHOICES)
    material= models.CharField(max_length=40, blank=True, null=True,default='X', choices=MATERIAL_CHOICES)
    mains= models.CharField(max_length=40, blank=False, null=False)
    height= models.CharField(max_length=40, blank=True, null=True)
    width= models.CharField(max_length=40, blank=True, null=True)
    diameter= models.CharField(max_length=40, blank=True, null=True)
    colour= models.CharField(max_length=40, blank=True, null=True)
    art_No= models.CharField(max_length=40, blank=False, null=False)
    bruto_price= models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    transformer_included=models.BooleanField(default=True)
    lamp_type = models.CharField(max_length=15, blank=False, null=False, default='X', choices=LAMP_TYPE_CHOICES)
    miscellaneous = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, null=False, related_name="line_items", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
        
class LampImage(models.Model):
    image = models.ImageField(upload_to="images" , null=True, blank=True)
    lamp = models.ForeignKey(Lamp, null=False, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.lamp.name
        
        
        
