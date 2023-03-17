from django.db import models

# Create your models here.


class ServiceAVV(models.Model):                                                                             # AVV= Asset Valuation & Verification
    service_img_avv = models.ImageField(upload_to='avv_service/service/',blank=False)               
    title_avv = models.CharField(max_length=200,blank=False)
    description_first_para_avv = models.TextField(max_length=1024,blank=False)
    description_second_para_avv = models.TextField(max_length=1024,blank=False)
    service_details_card_title_avv_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_avv_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_avv_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_avv_2 = models.CharField(max_length=200,blank=False)
    
     
class CardAVV(models.Model):
    logo_img_avv = models.ImageField(upload_to='avv_service/card/',blank=False)
    title_slogan_avv = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitAVV(models.Model):
    customer_benefit_img_avv = models.ImageField(upload_to='avv_service/customerBenefit/',blank=False)
    title_avv = models.CharField(max_length=200,blank=False)
    description_avv = models.TextField(max_length=1024,blank=False)
    customer_service_avv_1 = models.CharField(max_length=200,blank=False)
    customer_service_avv_2 = models.CharField(max_length=200,blank=False)
    customer_service_avv_3 = models.CharField(max_length=200,blank=False)