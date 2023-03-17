from django.db import models
from django.utils.timezone import now

# Create your models here.

class HotlineInfo(models.Model):   
    hotline_title = models.CharField(max_length=200,blank=False)          
    contact_img = models.ImageField(upload_to='contact/',blank=False)               
    title = models.CharField(max_length=200,blank=True)
    telephone_no = models.CharField(max_length=200,blank=True)
    opening_title = models.CharField(max_length=200,blank=True)
    day = models.CharField(max_length=200,blank=True)
    time = models.CharField(max_length=200,blank=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)  
    
    def __str__(self):
        return self.hotline_title
    
class OfficeAddress(models.Model):
    address_title = models.CharField(max_length=200,blank=False) 
    sub_office = models.CharField(max_length=200,blank=False)
    sub_office_location = models.CharField(max_length=200,blank=True)
    head_office = models.CharField(max_length=200,blank=True)
    head_office_location = models.CharField(max_length=200,blank=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)  
    
    def __str__(self):
        return self.address_title