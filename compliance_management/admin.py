from django.contrib import admin
from .models import ServiceCM, CardCM, CustomerBenefitCM

# Register your models here.



@admin.register(ServiceCM)
class ServiceCMAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_cm', 'title_cm', 'description_first_para_cm', 'description_second_para_cm', 'service_details_card_title_cm_1', 'service_details_card_details_cm_1', 'service_details_card_title_cm_2', 'service_details_card_details_cm_2']
    
@admin.register(CardCM)
class CardCMAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_cm', 'title_slogan_cm']
    
@admin.register(CustomerBenefitCM)
class CustomerBenefitCMAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_cm', 'title_cm', 'description_cm', 'customer_service_cm_1', 'customer_service_cm_2', 'customer_service_cm_3']