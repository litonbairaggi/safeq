from django.contrib import admin
from .models import ServiceAR, CardAR, CustomerBenefitAR

# Register your models here.

@admin.register(ServiceAR)
class ServiceARAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_ar', 'title_ar', 'description_first_para_ar', 'description_second_para_ar', 'service_details_card_title_ar_1', 'service_details_card_details_ar_1', 'service_details_card_title_ar_2', 'service_details_card_details_ar_2']
    
@admin.register(CardAR)
class CardARAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_ar', 'title_slogan_ar']
    
@admin.register(CustomerBenefitAR)
class CustomerBenefitARAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_ar', 'title_ar', 'description_ar', 'customer_service_ar_1', 'customer_service_ar_2', 'customer_service_ar_3']