from django.contrib import admin
from .models import ServiceCR, CardCR, CustomerBenefitCR

# Register your models here.

@admin.register(ServiceCR)
class ServiceCRAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_cr', 'title_cr', 'description_first_para_cr', 'description_second_para_cr', 'service_details_card_title_cr_1', 'service_details_card_details_cr_1', 'service_details_card_title_cr_2', 'service_details_card_details_cr_2']
    
@admin.register(CardCR)
class CardCRAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_cr', 'title_slogan_cr']
    
@admin.register(CustomerBenefitCR)
class CustomerBenefitCRAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_cr', 'title_cr', 'description_cr', 'customer_service_cr_1', 'customer_service_cr_2', 'customer_service_cr_3']