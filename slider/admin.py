from django.contrib import admin
from .models import Slider
# Register your models here.



@admin.register(Slider)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ['id', 'welcome_text', 'title', 'with_title', 'description', 'sliders_img']