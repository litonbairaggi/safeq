from django.contrib import admin
from .models import Setting

# Register your models here.


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'working_time', 'phone', 'facebook', 'twitter', 'instagram', 'linkedin', 'weblink', 'logo_img', 'descriptions']