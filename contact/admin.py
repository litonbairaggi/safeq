from django.contrib import admin
from .models import HotlineInfo, OfficeAddress

# Register your models here.

@admin.register(HotlineInfo)
class HotlineInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotline_title', 'contact_img', 'title', 'telephone_no', 'opening_title', 'day', 'time']
    
@admin.register(OfficeAddress)
class OfficeAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'address_title', 'sub_office', 'sub_office_location', 'head_office', 'head_office_location']