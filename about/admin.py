from django.contrib import admin
from .models import AboutUs, FounderInfo, AboutTime
# Register your models here.



@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_slogan', 'title', 'description', 'detail_1', 'detail_2', 'detail_3', 'detail_4', 'detail_5', 'detail_6']
    
@admin.register(FounderInfo)
class FounderInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'founder_img', 'name', 'designation', 'contact_no']
    
@admin.register(AboutTime)
class AboutTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'img', 'small_img', 'time_no', 'time', 'description']