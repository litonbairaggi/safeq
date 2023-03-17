from django.db import models

# Create your models here.

class ServiceBSA(models.Model):                                                                             # BSA= Business Startup or Acquisition
    service_img_bsa = models.ImageField(upload_to='bsa_service/service/',blank=False)               
    title_bsa = models.CharField(max_length=200,blank=False)
    description_first_para_bsa = models.TextField(max_length=1024,blank=False)
    description_second_para_bsa = models.TextField(max_length=1024,blank=False)
    service_details_card_title_bsa_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_bsa_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_bsa_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_bsa_2 = models.CharField(max_length=200,blank=False)
    
     
class CardBSA(models.Model):
    logo_img_bsa = models.ImageField(upload_to='bsa_service/card/',blank=False)
    title_slogan_bsa = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitBSA(models.Model):
    customer_benefit_img_bsa = models.ImageField(upload_to='bsa_service/customerBenefit/',blank=False)
    title_bsa = models.CharField(max_length=200,blank=False)
    description_bsa = models.TextField(max_length=1024,blank=False)
    customer_service_bsa_1 = models.CharField(max_length=200,blank=False)
    customer_service_bsa_2 = models.CharField(max_length=200,blank=False)
    customer_service_bsa_3 = models.CharField(max_length=200,blank=False)