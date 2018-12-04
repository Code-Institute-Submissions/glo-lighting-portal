from django.db import models
from django.contrib.auth.models import User
from articles.models import Article
# Create your models here.
class Profile(models.Model):
    
    GENDER_LIST = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="avatars", default="avatars/anonymous.png")
    gender = models.CharField(max_length=1, choices=GENDER_LIST, blank=False, null=False)
    
    def __str__(self):
        return self.user.username + ' Profile'