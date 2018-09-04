from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='brand')
    name= models.CharField("Brand Name", max_length=40, blank=False, null=False)
    logo= models.ImageField("Brand Logo",upload_to="logos" , null=True, blank=True)

    def __str__(self):
        return self.name
        
class Professional(models.Model):
    companyName= models.CharField("Company Name", max_length=40, blank=False, null=False)
    chamberOfCommerceNo =  models.CharField("second Name", max_length=40, blank=False, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professional')
    firstName= models.CharField("First Name", max_length=40, blank=False, null=False)
    secondName= models.CharField("Second Name", max_length=40, blank=False, null=False)    
    address= models.CharField("Address", max_length=40, blank=False, null=False) 
    city= models.CharField("City", max_length=40, blank=False, null=False) 
    postcode= models.CharField("Postcode", max_length=40, blank=False, null=False) 
    Land= models.CharField("Land", max_length=40, blank=False, null=False) 
    OrderHistory= models.CharField("OrderHistory", max_length=40, blank=False, null=False)



    def __str__(self):
        return self.name