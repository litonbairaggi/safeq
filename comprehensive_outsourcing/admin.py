from django.contrib import admin
from .models import ServiceCO, CardCO, CustomerBenefitCO

# Register your models here.

@admin.register(ServiceCO)
class ServiceCOAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_co', 'title_co', 'description_first_para_co', 'description_second_para_co', 'service_details_card_title_co_1', 'service_details_card_details_co_1', 'service_details_card_title_co_2', 'service_details_card_details_co_2']
    
@admin.register(CardCO)
class CardCOAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_co', 'title_slogan_co']
    
@admin.register(CustomerBenefitCO)
class CustomerBenefitCOAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_co', 'title_co', 'description_co', 'customer_service_co_1', 'customer_service_co_2', 'customer_service_co_3']