from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_1', 'Short_description_1', 'title_2', 'Short_description_2', 'title_3', 'Short_description_3', 'title_4', 'Short_description_4', 'title_5', 'Short_description_5', 'title_6', 'Short_description_6', 'title_7', 'Short_description_7']
    