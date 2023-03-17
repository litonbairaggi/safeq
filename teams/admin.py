from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'membar_img', 'designation', 'name', 'my_self', 'email', 'phone', 'twitter', 'instagram', 'linkedin', 'address', 'professional_sd', 'educational_ed', 'top_1_skills', 'top_1_sp', 'top_2_skills', 'top_2_sp', 'top_3_skills', 'top_3_sp', 'company_name', 'time_period', 'designation_previous']
    