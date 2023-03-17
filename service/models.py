from django.db import models

# Create your models here.

class Service(models.Model):
    pre_title = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    
    title_1 = models.CharField(max_length=200, blank=True, null=True)
    Short_description_1 = models.TextField(max_length=700, blank=True, null=True)
    
    title_2 = models.CharField(max_length=200, blank=True, null=True)
    Short_description_2 = models.TextField(max_length=700, blank=True, null=True)
    
    title_3 = models.CharField(max_length=200, blank=True, null=True)
    Short_description_3 = models.TextField(max_length=700, blank=True, null=True)
    
    title_4 = models.CharField(max_length=200, blank=True, null=True)
    Short_description_4 = models.TextField(max_length=700, blank=True, null=True)
    
    title_5 = models.CharField(max_length=200, blank=True, null=True)
    Short_description_5 = models.TextField(max_length=700, blank=True, null=True)
    
    title_6 = models.CharField(max_length=200, blank=True, null=True)
    Short_description_6 = models.TextField(max_length=700, blank=True, null=True)
    
    title_7 = models.CharField(max_length=200, blank=True, null=True)
    Short_description_7 = models.TextField(max_length=700, blank=True, null=True)

    