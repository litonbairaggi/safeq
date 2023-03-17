from django.db import models

# Create your models here.

class Slider(models.Model):
    welcome_text = models.CharField(max_length=200,blank=False)
    title = models.CharField(max_length=200,blank=False)
    with_title = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=700,blank=False)
    sliders_img = models.ImageField(upload_to='sliders/',blank=False)