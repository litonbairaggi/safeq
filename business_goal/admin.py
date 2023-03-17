from django.contrib import admin
from .models import BusinessGoal
# Register your models here.

@admin.register(BusinessGoal)
class BusinessGoalAdmin(admin.ModelAdmin):
    list_display = ['id', 'img', 'small_img', 'pre_title', 'title', 'support_title_1', 'description_1', 'support_title_2', 'description_2']