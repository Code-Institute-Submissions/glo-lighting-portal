from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Brand(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='brand')
    name= models.CharField("Brand Name", max_length=40, blank=False, null=False)
    logo= models.ImageField("Brand Logo",upload_to="logos" , null=True, blank=True)

    def __str__(self):
        return self.name