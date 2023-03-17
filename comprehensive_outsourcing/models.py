from django.db import models

# Create your models here.

class ServiceCO(models.Model):                                                                             # CO= Comprehensive Outsourcing
    service_img_co = models.ImageField(upload_to='co_service/service/',blank=False)               
    title_co = models.CharField(max_length=200,blank=False)
    description_first_para_co = models.TextField(max_length=1024,blank=False)
    description_second_para_co = models.TextField(max_length=1024,blank=False)
    service_details_card_title_co_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_co_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_co_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_co_2 = models.CharField(max_length=200,blank=False)
    
     
class CardCO(models.Model):
    logo_img_co = models.ImageField(upload_to='co_service/card/',blank=False)
    title_slogan_co = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitCO(models.Model):
    customer_benefit_img_co = models.ImageField(upload_to='co_service/customerBenefit/',blank=False)
    title_co = models.CharField(max_length=200,blank=False)
    description_co = models.TextField(max_length=1024,blank=False)
    customer_service_co_1 = models.CharField(max_length=200,blank=False)
    customer_service_co_2 = models.CharField(max_length=200,blank=False)
    customer_service_co_3 = models.CharField(max_length=200,blank=False)