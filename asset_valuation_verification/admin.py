from django.contrib import admin
from .models import ServiceAVV, CardAVV, CustomerBenefitAVV

# Register your models here.

@admin.register(ServiceAVV)
class ServiceAVVAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_avv', 'title_avv', 'description_first_para_avv', 'description_second_para_avv', 'service_details_card_title_avv_1', 'service_details_card_details_avv_1', 'service_details_card_title_avv_2', 'service_details_card_details_avv_2']
    
@admin.register(CardAVV)
class CardAVVAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_avv', 'title_slogan_avv']
    
@admin.register(CustomerBenefitAVV)
class CustomerBenefitAVVAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_avv', 'title_avv', 'description_avv', 'customer_service_avv_1', 'customer_service_avv_2', 'customer_service_avv_3']