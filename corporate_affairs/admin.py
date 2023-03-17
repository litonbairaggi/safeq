from django.contrib import admin
from .models import ServiceCA, CardCA, CustomerBenefitCA

# Register your models here.



@admin.register(ServiceCA)
class ServiceCAAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_ca', 'title_ca', 'description_first_para_ca', 'description_second_para_ca', 'service_details_card_title_ca_1', 'service_details_card_details_ca_1', 'service_details_card_title_ca_2', 'service_details_card_details_ca_2']
    
@admin.register(CardCA)
class CardCAAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_ca', 'title_slogan_ca']
    
@admin.register(CustomerBenefitCA)
class CustomerBenefitCAAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_ca', 'title_ca', 'description_ca', 'customer_service_ca_1', 'customer_service_ca_2', 'customer_service_ca_3']