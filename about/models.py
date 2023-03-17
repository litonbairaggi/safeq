from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title_slogan = models.CharField(max_length=200,blank=False)
    title = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=700,blank=False)
    detail_1 = models.CharField(max_length=200,blank=False)
    detail_2 = models.CharField(max_length=200,blank=False)
    detail_3 = models.CharField(max_length=200,blank=False)
    detail_4 = models.CharField(max_length=200,blank=False)
    detail_5 = models.CharField(max_length=200,blank=False)
    detail_6 = models.CharField(max_length=200,blank=False)
    
    
class FounderInfo(models.Model):
    founder_img = models.ImageField(upload_to='aboutUs/founder/',blank=False)
    name = models.CharField(max_length=200,blank=False)
    designation = models.CharField(max_length=200,blank=False)
    contact_no = models.CharField(max_length=200,blank=False)
    
class AboutTime(models.Model):
    img = models.ImageField(upload_to='aboutUs/img/',blank=False)
    small_img = models.ImageField(upload_to='aboutUs/on_img/',blank=False)
    time_no = models.IntegerField(blank=False)
    TIME = (
        ('', 'Select'),
        ('Days', 'Days'),
        ('Months', 'Months'),
        ('Years', 'Years'),
    )
    time = models.CharField(max_length=64, null=True, blank=False, choices=TIME)
    description = models.CharField(max_length=200,blank=False)
    