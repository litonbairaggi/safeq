from django.db import models

# Create your models here.


class ServiceAR(models.Model):                                                                             # AR= Short form of Accounting and Reporting
    service_img_ar = models.ImageField(upload_to='ar_service/service/',blank=False)               
    title_ar = models.CharField(max_length=200,blank=False)
    description_first_para_ar = models.TextField(max_length=1024,blank=False)
    description_second_para_ar = models.TextField(max_length=1024,blank=False)
    service_details_card_title_ar_1 = models.CharField(max_length=200,blank=False)
    service_details_card_details_ar_1 = models.CharField(max_length=200,blank=False)
    service_details_card_title_ar_2 = models.CharField(max_length=200,blank=False)
    service_details_card_details_ar_2 = models.CharField(max_length=200,blank=False)
    
     
class CardAR(models.Model):
    logo_img_ar = models.ImageField(upload_to='ar_service/card/',blank=False)
    title_slogan_ar = models.CharField(max_length=200,blank=False)
    
class CustomerBenefitAR(models.Model):
    customer_benefit_img_ar = models.ImageField(upload_to='ar_service/customerBenefit/',blank=False)
    title_ar = models.CharField(max_length=200,blank=False)
    description_ar = models.TextField(max_length=1024,blank=False)
    customer_service_ar_1 = models.CharField(max_length=200,blank=False)
    customer_service_ar_2 = models.CharField(max_length=200,blank=False)
    customer_service_ar_3 = models.CharField(max_length=200,blank=False)