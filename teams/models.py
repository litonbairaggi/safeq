from django.db import models

# Create your models here.

class Teams(models.Model):
    membar_img = models.ImageField(upload_to='teams/',blank=False)
    designation = models.CharField(max_length=200, blank=False)
    name = models.CharField(max_length=200, blank=False, null=True)
    my_self = models.TextField(max_length=700, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=100, unique=True, blank=True)
    instagram = models.URLField(max_length=100, unique=True, blank=True)
    linkedin = models.URLField(max_length=100, unique=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    professional_sd = models.TextField(max_length=700, blank=True, null=True)               # sd = skills detail
    educational_ed = models.TextField(max_length=700, blank=True, null=True)                # ed = experience detail
    top_1_skills = models.CharField(max_length=200, blank=True, null=True)
    top_1_sp = models.PositiveIntegerField(blank=True, null=True)                           # sp = skills percentage
    top_2_skills = models.CharField(max_length=200, blank=True, null=True)
    top_2_sp = models.PositiveIntegerField(blank=True, null=True)                           # sp = skills percentage
    top_3_skills = models.CharField(max_length=200, blank=True, null=True)
    top_3_sp = models.PositiveIntegerField(blank=True, null=True)                           # sp = skills percentage
    
    company_name = models.CharField(max_length=200, blank=True, null=True)
    time_period = models.CharField(max_length=200, blank=True, null=True)
    designation_previous = models.CharField(max_length=200, blank=True)