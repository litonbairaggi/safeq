from django.db import models

# Create your models here.

class Feature(models.Model):
    feature_img = models.ImageField(upload_to='feature/', blank=False)               
    pre_title = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=700, blank=True)
    feature_1 = models.CharField(max_length=200, blank=True)
    feature_2 = models.CharField(max_length=200, blank=True)
    feature_3 = models.CharField(max_length=200, blank=True)
    feature_4 = models.CharField(max_length=200, blank=True)