from django.db import models

# Create your models here.

class BusinessGoal(models.Model):
    img = models.ImageField(upload_to='businessGoal/img/',blank=False)
    small_img = models.ImageField(upload_to='businessGoal/on_img/',blank=False)
    pre_title = models.CharField(max_length=200,blank=False)
    title = models.CharField(max_length=200,blank=False)
    support_title_1 = models.CharField(max_length=200,blank=False)
    description_1 = models.TextField(max_length=700,blank=False)
    support_title_2 = models.CharField(max_length=200,blank=False)
    description_2 = models.TextField(max_length=700,blank=False)