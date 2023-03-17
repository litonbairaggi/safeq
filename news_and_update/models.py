from django.db import models
from django.utils.timezone import now

# Create your models here.

class NewsUpdate(models.Model):
    membar_img = models.ImageField(upload_to='news_update/',blank=False)
    organization = models.CharField(max_length=200, blank=False, null=True)
    headline = models.CharField(max_length=200, blank=False)
    
    descriptions_1 = models.TextField(max_length=700, blank=True, null=True)
    descriptions_2 = models.TextField(max_length=700, blank=True, null=True)
    descriptions_3 = models.TextField(max_length=700, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)  
    
    def __str__(self):
        return self.organization