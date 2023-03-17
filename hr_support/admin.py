from django.contrib import admin
from .models import ServiceHS, CardHS, CustomerBenefitHS

# Register your models here.

@admin.register(ServiceHS)
class ServiceHSAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_hs', 'title_hs', 'description_first_para_hs', 'description_second_para_hs', 'service_details_card_title_hs_1', 'service_details_card_details_hs_1', 'service_details_card_title_hs_2', 'service_details_card_details_hs_2']
    
@admin.register(CardHS)
class CardHSAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_hs', 'title_slogan_hs']
    
@admin.register(CustomerBenefitHS)
class CustomerBenefitHSAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_hs', 'title_hs', 'description_hs', 'customer_service_hs_1', 'customer_service_hs_2', 'customer_service_hs_3']