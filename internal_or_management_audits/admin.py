from django.contrib import admin
from .models import ServiceIMA, CardIMA, CustomerBenefitIMA

# Register your models here.



@admin.register(ServiceIMA)
class ServiceIMAAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_img_ima', 'title_ima', 'description_first_para_ima', 'description_second_para_ima', 'service_details_card_title_ima_1', 'service_details_card_details_ima_1', 'service_details_card_title_ima_2', 'service_details_card_details_ima_2']
    
@admin.register(CardIMA)
class CardIMAAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo_img_ima', 'title_slogan_ima']
    
@admin.register(CustomerBenefitIMA)
class CustomerBenefitIMAAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_benefit_img_ima', 'title_ima', 'description_ima', 'customer_service_ima_1', 'customer_service_ima_2', 'customer_service_ima_3']