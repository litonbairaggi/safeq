from django.db import models

# Create your models here.

class ServiceIMA(models.Model):                                                                             # IMA= Internal / Management Audits
    service_img_ima = models.ImageField(upload_to='ima_service/service/',blank=False)               
    title_ima = models.CharField(max_length=200,blank=False)
    description_first_para_ima = models.TextField(max_length=1024,blank=False)
    description_second_para_ima = models.TextField(max_length=1024,blank=False)
    service_details_card_title_ima_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_ima_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_ima_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_ima_2 = models.CharField(max_length=200,blank=False)
    
     
class CardIMA(models.Model):
    logo_img_ima = models.ImageField(upload_to='ima_service/card/',blank=False)
    title_slogan_ima = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitIMA(models.Model):
    customer_benefit_img_ima = models.ImageField(upload_to='ima_service/customerBenefit/',blank=False)
    title_ima = models.CharField(max_length=200,blank=False)
    description_ima = models.TextField(max_length=1024,blank=False)
    customer_service_ima_1 = models.CharField(max_length=200,blank=False)
    customer_service_ima_2 = models.CharField(max_length=200,blank=False)
    customer_service_ima_3 = models.CharField(max_length=200,blank=False)