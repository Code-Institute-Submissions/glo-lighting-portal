from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models. TextField()
    date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User, related_name='article', null=False, default=1, on_delete=models.SET_DEFAULT) 
    image = models.ImageField(upload_to="article_images" , null=True, blank=True)
def __str__(self):
    return self.title
    
    
