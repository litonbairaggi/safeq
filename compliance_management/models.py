from django.db import models

# Create your models here.

class ServiceCM(models.Model):                                                                             # CM= Compliance Management
    service_img_cm = models.ImageField(upload_to='cm_service/service/',blank=False)               
    title_cm = models.CharField(max_length=200,blank=False)
    description_first_para_cm = models.TextField(max_length=1024,blank=False)
    description_second_para_cm = models.TextField(max_length=1024,blank=False)
    service_details_card_title_cm_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_cm_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_cm_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_cm_2 = models.CharField(max_length=200,blank=False)
    
     
class CardCM(models.Model):
    logo_img_cm = models.ImageField(upload_to='cm_service/card/',blank=False)
    title_slogan_cm = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitCM(models.Model):
    customer_benefit_img_cm = models.ImageField(upload_to='cm_service/customerBenefit/',blank=False)
    title_cm = models.CharField(max_length=200,blank=False)
    description_cm = models.TextField(max_length=1024,blank=False)
    customer_service_cm_1 = models.CharField(max_length=200,blank=False)
    customer_service_cm_2 = models.CharField(max_length=200,blank=False)
    customer_service_cm_3 = models.CharField(max_length=200,blank=False)