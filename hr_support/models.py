from django.db import models

# Create your models here.

class ServiceHS(models.Model):                                                                             # HS = HR Support
    service_img_hs = models.ImageField(upload_to='hs_service/service/',blank=False)               
    title_hs = models.CharField(max_length=200,blank=False)
    description_first_para_hs = models.TextField(max_length=1024,blank=False)
    description_second_para_hs = models.TextField(max_length=1024,blank=False)
    service_details_card_title_hs_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_hs_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_hs_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_hs_2 = models.CharField(max_length=200,blank=False)
    
     
class CardHS(models.Model):
    logo_img_hs = models.ImageField(upload_to='hs_service/card/',blank=False)
    title_slogan_hs = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitHS(models.Model):
    customer_benefit_img_hs = models.ImageField(upload_to='hs_service/customerBenefit/',blank=False)
    title_hs = models.CharField(max_length=200,blank=False)
    description_hs = models.TextField(max_length=1024,blank=False)
    customer_service_hs_1 = models.CharField(max_length=200,blank=False)
    customer_service_hs_2 = models.CharField(max_length=200,blank=False)
    customer_service_hs_3 = models.CharField(max_length=200,blank=False)