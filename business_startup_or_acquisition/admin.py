from django.contrib import admin
from .models import ServiceBSA, CardBSA, CustomerBenefitBSA

# Register your models here.

@admin.register(ServiceBSA)
class ServiceBSAAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_bsa', 'title_bsa', 'description_first_para_bsa', 'description_second_para_bsa', 'service_details_card_title_bsa_1', 'service_details_card_details_bsa_1', 'service_details_card_title_bsa_2', 'service_details_card_details_bsa_2']
    
@admin.register(CardBSA)
class CardBSAAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_bsa', 'title_slogan_bsa']
    
@admin.register(CustomerBenefitBSA)
class CustomerBenefitBSAAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_bsa', 'title_bsa', 'description_bsa', 'customer_service_bsa_1', 'customer_service_bsa_2', 'customer_service_bsa_3']