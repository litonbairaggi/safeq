from django.db import models

# Create your models here.

class ServiceTC(models.Model):
    service_img_tc = models.ImageField(upload_to='tc_service/service/',blank=False)
    title_tc = models.CharField(max_length=200,blank=False)
    description_first_para_tc = models.TextField(max_length=700,blank=False)
    description_second_para_tc = models.TextField(max_length=700,blank=False)
    service_details_card_title_tc_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_tc_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_tc_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_tc_2 = models.CharField(max_length=200,blank=False)
    
     
class CardTC(models.Model):
    logo_img_tc = models.ImageField(upload_to='tc_service/card/',blank=False)
    title_slogan_tc = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitTC(models.Model):
    customer_benefit_img_tc = models.ImageField(upload_to='tc_service/customerBenefit/',blank=False)
    title_tc = models.CharField(max_length=200,blank=False)
    description_tc = models.TextField(max_length=700,blank=False)
    customer_service_tc_1 = models.CharField(max_length=200,blank=False)
    customer_service_tc_2 = models.CharField(max_length=200,blank=False)
    customer_service_tc_3 = models.CharField(max_length=200,blank=False)