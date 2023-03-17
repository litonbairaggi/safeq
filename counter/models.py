from django.db import models

# Create your models here.

class Counter(models.Model):
    value_1 = models.PositiveIntegerField(blank=True, null=True)
    subject_1 = models.CharField(max_length=200,blank=False)
    
    value_2 = models.PositiveIntegerField(blank=True, null=True)
    subject_2 = models.CharField(max_length=200,blank=False)
    value_3 = models.PositiveIntegerField(blank=True, null=True)
    subject_3 = models.CharField(max_length=200,blank=False)
    value_4 = models.PositiveIntegerField(blank=True, null=True)
    subject_4 = models.CharField(max_length=200,blank=False)