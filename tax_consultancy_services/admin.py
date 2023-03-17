from django.contrib import admin
from .models import ServiceTC, CardTC, CustomerBenefitTC

# Register your models here.



@admin.register(ServiceTC)
class ServiceTCAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_tc', 'title_tc', 'description_first_para_tc', 'description_second_para_tc', 'service_details_card_title_tc_1', 'service_details_card_details_tc_1', 'service_details_card_title_tc_2', 'service_details_card_details_tc_2']
    
@admin.register(CardTC)
class CardTCAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_tc', 'title_slogan_tc']
    
@admin.register(CustomerBenefitTC)
class CustomerBenefitTCAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_tc', 'title_tc', 'description_tc', 'customer_service_tc_1', 'customer_service_tc_2', 'customer_service_tc_3']