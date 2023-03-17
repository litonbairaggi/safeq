from django.contrib import admin
from .models import NewsUpdate
# Register your models here.



@admin.register(NewsUpdate)
class NewsUpdateAdmin(admin.ModelAdmin):
    list_display = ['id', 'membar_img', 'organization', 'headline', 'descriptions_1', 'descriptions_2', 'descriptions_3', 'updated_at']
    