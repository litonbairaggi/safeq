from django.db import models

# Create your models here.


class ServiceCR(models.Model):                                                                             # CR= Certificatio of Report
    service_img_cr = models.ImageField(upload_to='cr_service/service/',blank=False)               
    title_cr = models.CharField(max_length=200,blank=False)
    description_first_para_cr = models.TextField(max_length=1024,blank=False)
    description_second_para_cr = models.TextField(max_length=1024,blank=False)
    service_details_card_title_cr_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_cr_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_cr_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_cr_2 = models.CharField(max_length=200,blank=False)
    
     
class CardCR(models.Model):
    logo_img_cr = models.ImageField(upload_to='cr_service/card/',blank=False)
    title_slogan_cr = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitCR(models.Model):
    customer_benefit_img_cr = models.ImageField(upload_to='cr_service/customerBenefit/',blank=False)
    title_cr = models.CharField(max_length=200,blank=False)
    description_cr = models.TextField(max_length=1024,blank=False)
    customer_service_cr_1 = models.CharField(max_length=200,blank=False)
    customer_service_cr_2 = models.CharField(max_length=200,blank=False)
    customer_service_cr_3 = models.CharField(max_length=200,blank=False)