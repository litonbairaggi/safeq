from django.contrib import admin
from .models import OurClient
# Register your models here.



@admin.register(OurClient)
class OurClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'clients_img']