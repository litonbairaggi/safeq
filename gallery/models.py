from django.db import models

# Create your models here.

class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='gallery/',blank=False)               
    title = models.CharField(max_length=200,blank=True)
    sub_title = models.CharField(max_length=200,blank=True)
    description = models.TextField(max_length=400,blank=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)