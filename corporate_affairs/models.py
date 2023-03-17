from django.db import models

# Create your models here.

class ServiceCA(models.Model):                                                                             # AR= Short form of Accounting and Reporting
    service_img_ca = models.ImageField(upload_to='ca_service/service/',blank=False)               
    title_ca = models.CharField(max_length=200,blank=False)
    description_first_para_ca = models.TextField(max_length=1024,blank=False)
    description_second_para_ca = models.TextField(max_length=1024,blank=False)
    service_details_card_title_ca_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_ca_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_ca_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_ca_2 = models.CharField(max_length=200,blank=False)
    
     
class CardCA(models.Model):
    logo_img_ca = models.ImageField(upload_to='ca_service/card/',blank=False)
    title_slogan_ca = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitCA(models.Model):
    customer_benefit_img_ca = models.ImageField(upload_to='ca_service/customerBenefit/',blank=False)
    title_ca = models.CharField(max_length=200,blank=False)
    description_ca = models.TextField(max_length=1024,blank=False)
    customer_service_ca_1 = models.CharField(max_length=200,blank=False)
    customer_service_ca_2 = models.CharField(max_length=200,blank=False)
    customer_service_ca_3 = models.CharField(max_length=200,blank=False)